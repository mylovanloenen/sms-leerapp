import os
from datetime import timezone

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from twilio.twiml.messaging_response import MessagingResponse

from app.database import Base, engine, get_db
from app.models import User
from app.sms_logic import process_message
from app.curriculum import CURRICULUM, LANGUAGES

load_dotenv()

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SMS Leerapp")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")


# ─── Twilio webhook ──────────────────────────────────────────────────────────

@app.post("/webhook")
async def webhook(
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db),
):
    reply = process_message(phone=From, body=Body, db=db)
    resp = MessagingResponse()
    resp.message(reply)
    return Response(content=str(resp), media_type="application/xml")


# ─── Dashboard ───────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.last_active.desc()).all()

    # Enrich with computed fields
    enriched = []
    for u in users:
        total_steps = sum(len(m["steps"]) for m in CURRICULUM)
        completed_steps = sum(
            len(m["steps"])
            for m in CURRICULUM
            if m["module"] < u.module
        ) + (u.step - 1)
        progress_pct = round((completed_steps / total_steps) * 100) if total_steps else 0

        score_pct = (
            round((u.correct_answers / u.total_questions) * 100)
            if u.total_questions
            else None
        )

        current_module_title = ""
        for m in CURRICULUM:
            if m["module"] == u.module:
                current_module_title = m["title"].get(u.language or "EN", "")
                break

        enriched.append({
            "phone": u.phone,
            "language": LANGUAGES.get(u.language, "?") if u.language else "?",
            "state": u.state,
            "module": u.module,
            "step": u.step,
            "module_title": current_module_title,
            "progress_pct": progress_pct,
            "correct": u.correct_answers,
            "total_q": u.total_questions,
            "score_pct": score_pct,
            "created_at": u.created_at,
            "last_active": u.last_active,
        })

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "users": enriched, "total_users": len(enriched)},
    )


@app.get("/user/{phone:path}", response_class=HTMLResponse)
def user_detail(phone: str, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        return HTMLResponse("<h1>User not found</h1>", status_code=404)

    # Build step progress for all modules
    module_progress = []
    for m in CURRICULUM:
        steps = []
        for s in m["steps"]:
            if m["module"] < user.module:
                status = "done"
            elif m["module"] == user.module and s["step"] < user.step:
                status = "done"
            elif m["module"] == user.module and s["step"] == user.step:
                status = "current"
            else:
                status = "pending"
            steps.append({"step": s["step"], "type": s["type"], "status": status})
        module_progress.append({
            "module": m["module"],
            "title": m["title"].get(user.language or "EN", ""),
            "steps": steps,
        })

    score_pct = (
        round((user.correct_answers / user.total_questions) * 100)
        if user.total_questions
        else None
    )

    return templates.TemplateResponse(
        "user.html",
        {
            "request": request,
            "user": user,
            "language_name": LANGUAGES.get(user.language, "?") if user.language else "?",
            "module_progress": module_progress,
            "score_pct": score_pct,
        },
    )
