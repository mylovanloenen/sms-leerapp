"""
Claude AI — genereert gepersonaliseerde lesinhoud, quizvragen en feedback.
Gebruikt claude-haiku-4-5 voor snelle, goedkope antwoorden.
Max ~160 tekens per bericht (1 SMS).
"""
import os
import anthropic

_client = None

LANG_NAMES = {
    "EN": "English", "NL": "Dutch",
    "DE": "German", "FR": "French", "ES": "Spanish",
}

CONTINUE_HINTS = {
    "EN": "Reply OK to continue.",
    "NL": "Antwoord OK om door te gaan.",
    "DE": "Antworten Sie OK.",
    "FR": "Répondez OK pour continuer.",
    "ES": "Responda OK para continuar.",
}

QUIZ_HINTS = {
    "EN": "Reply A, B or C:",
    "NL": "Antwoord A, B of C:",
    "DE": "Antworten Sie A, B oder C:",
    "FR": "Répondez A, B ou C:",
    "ES": "Responda A, B o C:",
}

YES_HINTS = {
    "EN": "Reply YES to continue!",
    "NL": "Antwoord JA om door te gaan!",
    "DE": "Antworten Sie JA!",
    "FR": "Répondez OUI pour continuer!",
    "ES": "¡Responda SÍ para continuar!",
}


def get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    return _client


def _call(system: str, user: str, max_tokens: int = 100) -> str | None:
    try:
        r = get_client().messages.create(
            model="claude-haiku-4-5",
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return r.content[0].text.strip()
    except Exception as e:
        print(f"AI error: {e}")
        return None


def _persona(lang: str, name: str | None = None, skill: str | None = None) -> str:
    """Bouw een systeem-prompt op basis van naam en niveau."""
    lang_name = LANG_NAMES.get(lang, "English")
    base = (
        f"You are a warm, patient phone trainer teaching elderly people via SMS. "
        f"Write ONLY in {lang_name}. Keep responses under 140 characters. "
        f"Use simple words and 1 emoji. Be encouraging and personal."
    )
    if name:
        base += f" The learner's name is {name}. Use their name occasionally."
    if skill:
        base += f" Their current phone skill: {skill}. Adapt your teaching accordingly."
    return base


# ── Onboarding ────────────────────────────────────────────────────────────────

def ask_name(lang: str) -> str:
    """Vraag de naam van de gebruiker."""
    msgs = {
        "EN": "😊 Nice to meet you! What is your name?",
        "NL": "😊 Leuk je te ontmoeten! Wat is jouw naam?",
        "DE": "😊 Schön, Sie kennenzulernen! Wie heißen Sie?",
        "FR": "😊 Ravi de vous rencontrer! Quel est votre prénom?",
        "ES": "😊 ¡Encantado de conocerte! ¿Cuál es tu nombre?",
    }
    return msgs.get(lang, msgs["EN"])


def ask_skills(lang: str, name: str) -> str:
    """Vraag wat de gebruiker al kan met de telefoon."""
    msgs = {
        "EN": f"Hi {name}! 📱 What can you already do on your phone?\n\nExamples: nothing yet / send SMS / make calls / use WhatsApp / use email",
        "NL": f"Hoi {name}! 📱 Wat kun je al met je telefoon?\n\nVoorbeelden: nog niets / SMS sturen / bellen / WhatsApp / e-mail",
        "DE": f"Hallo {name}! 📱 Was können Sie schon mit Ihrem Telefon?\n\nBeispiele: nichts / SMS senden / telefonieren / WhatsApp / E-Mail",
        "FR": f"Bonjour {name}! 📱 Que savez-vous déjà faire avec votre téléphone?\n\nExemples: rien / envoyer SMS / appeler / WhatsApp / email",
        "ES": f"¡Hola {name}! 📱 ¿Qué ya sabes hacer con tu teléfono?\n\nEjemplos: nada / enviar SMS / llamar / WhatsApp / correo",
    }
    return msgs.get(lang, msgs["EN"])


def assess_starting_module(skill_text: str, lang: str) -> int:
    """
    Bepaal het startmodule op basis van wat de gebruiker al kan.
    Returnt 1, 2, 3 of 4.
    """
    result = _call(
        system=(
            "You determine the starting module for a phone training program. "
            "Modules: 1=SMS basics, 2=calling & contacts, 3=WhatsApp, 4=email. "
            "Reply with ONLY a single digit: 1, 2, 3, or 4."
        ),
        user=(
            f"The learner says about their phone skills: \"{skill_text}\"\n"
            "Which module should they start at? "
            "If they know nothing → 1. If they can SMS → 2. "
            "If they can call/contacts → 3. If they can WhatsApp → 4. "
            "Reply ONLY with 1, 2, 3, or 4."
        ),
        max_tokens=5,
    )
    if result and result.strip() in ("1", "2", "3", "4"):
        return int(result.strip())
    return 1


def welcome_to_module(module_title: str, name: str, lang: str) -> str:
    """Welkomstbericht voor een module na skill assessment."""
    lang_name = LANG_NAMES.get(lang, "English")
    hint = CONTINUE_HINTS.get(lang, CONTINUE_HINTS["EN"])

    text = _call(
        system=f"Respond ONLY in {lang_name}. Max 120 chars. 1 emoji. Warm and encouraging.",
        user=f"Welcome {name} to their first lesson: '{module_title}'. Short welcome. Max 120 chars.",
        max_tokens=70,
    )
    if not text:
        return f"🎉 Welcome {name}! Let's start: {module_title}\n\n{hint}"
    return f"{text}\n\n{hint}"


# ── Les generatie ─────────────────────────────────────────────────────────────

def generate_lesson(
    topic: str,
    lesson_nr: int,
    lang: str,
    name: str | None = None,
    skill: str | None = None,
) -> str:
    hint = CONTINUE_HINTS.get(lang, CONTINUE_HINTS["EN"])

    text = _call(
        system=_persona(lang, name, skill),
        user=(
            f"Teach lesson {lesson_nr} about: {topic}. "
            f"Make it practical and specific. "
            f"Different angle than previous lessons. Max 130 chars."
        ),
        max_tokens=80,
    )

    if not text:
        fallback = {
            "EN": f"📱 Lesson {lesson_nr}: {topic}",
            "NL": f"📱 Les {lesson_nr}: {topic}",
            "DE": f"📱 Lektion {lesson_nr}: {topic}",
            "FR": f"📱 Leçon {lesson_nr}: {topic}",
            "ES": f"📱 Lección {lesson_nr}: {topic}",
        }
        text = fallback.get(lang, fallback["EN"])

    return f"{text}\n\n{hint}"


# ── Quiz generatie ────────────────────────────────────────────────────────────

def generate_quiz(
    topic: str,
    quiz_nr: int,
    lang: str,
    name: str | None = None,
    skill: str | None = None,
) -> dict | None:
    hint = QUIZ_HINTS.get(lang, QUIZ_HINTS["EN"])
    lang_name = LANG_NAMES.get(lang, "English")

    raw = _call(
        system=(
            f"Create a quiz for elderly phone learners. "
            f"Write ONLY in {lang_name}. Short and practical."
            + (f" Learner: {name}." if name else "")
        ),
        user=(
            f"Quiz {quiz_nr} about: {topic}\n"
            f"Exact format (nothing else):\n"
            f"Q: [max 60 chars]\n"
            f"A) [short option]\n"
            f"B) [short option]\n"
            f"C) [short option]\n"
            f"CORRECT: [A/B/C]"
        ),
        max_tokens=120,
    )

    if not raw:
        return None
    return _parse_quiz(raw, hint)


def _parse_quiz(raw: str, hint: str) -> dict | None:
    lines = [l.strip() for l in raw.strip().splitlines() if l.strip()]
    q, a, b, c, correct = "", "", "", "", ""

    for line in lines:
        if line.startswith("Q:"):
            q = line[2:].strip()
        elif line.startswith("A)"):
            a = line[2:].strip()
        elif line.startswith("B)"):
            b = line[2:].strip()
        elif line.startswith("C)"):
            c = line[2:].strip()
        elif "CORRECT:" in line:
            val = line.split("CORRECT:")[-1].strip().upper()
            if val and val[0] in "ABC":
                correct = val[0]

    if not (q and a and b and c and correct in ("A", "B", "C")):
        return None

    text = f"🎯 {q}\n\nA) {a}\nB) {b}\nC) {c}\n\n{hint}"
    return {"text": text, "correct": correct}


# ── Feedback ──────────────────────────────────────────────────────────────────

def generate_feedback(
    correct: bool,
    chosen: str,
    right: str,
    lang: str,
    name: str | None = None,
) -> str:
    lang_name = LANG_NAMES.get(lang, "English")

    text = _call(
        system=f"Respond ONLY in {lang_name}. Max 90 chars. 1 emoji."
               + (f" Learner: {name}." if name else ""),
        user=(
            f"{'CORRECT ✅' if correct else f'WRONG ❌ correct answer: {right}'}. "
            f"Give {'encouraging' if correct else 'gentle corrective'} feedback. Max 90 chars."
        ),
        max_tokens=60,
    )

    if not text:
        if correct:
            return {"EN": "✅ Correct!", "NL": "✅ Goed zo!", "DE": "✅ Richtig!", "FR": "✅ Correct!", "ES": "✅ ¡Correcto!"}.get(lang, "✅ Correct!")
        return {"EN": f"❌ Wrong! Answer: {right}", "NL": f"❌ Fout! Antwoord: {right}", "DE": f"❌ Falsch! Antwort: {right}", "FR": f"❌ Faux! Réponse: {right}", "ES": f"❌ ¡Mal! Respuesta: {right}"}.get(lang, f"❌ Wrong! Answer: {right}")

    return text


# ── Module afronden ───────────────────────────────────────────────────────────

def generate_module_complete(
    module_title: str,
    next_title: str | None,
    lang: str,
    name: str | None = None,
) -> str:
    lang_name = LANG_NAMES.get(lang, "English")

    if next_title:
        hint = YES_HINTS.get(lang, YES_HINTS["EN"])
        text = _call(
            system=f"Respond ONLY in {lang_name}. Max 110 chars. 1 emoji. Encouraging."
                   + (f" Learner: {name}." if name else ""),
            user=f"Module '{module_title}' complete! Next: '{next_title}'. Short congratulation.",
            max_tokens=70,
        )
        if not text:
            text = f"🏆 {module_title} complete!"
        return f"{text}\n\n{hint}"
    else:
        restart = {"EN": "Reply RESTART to start over.", "NL": "Antwoord OPNIEUW.", "DE": "Antworten Sie NEU.", "FR": "Répondez RECOMMENCER.", "ES": "Responda REINICIAR."}.get(lang, "Reply RESTART.")
        text = _call(
            system=f"Respond ONLY in {lang_name}. Max 130 chars. Use emojis. Very celebratory!"
                   + (f" Learner: {name}." if name else ""),
            user="All 4 phone training modules complete! Big celebration! Max 130 chars.",
            max_tokens=80,
        )
        if not text:
            text = "🎉 All done! You're a phone pro! 🌟"
        return f"{text}\n\n{restart}"


# ── Vrije vragen ──────────────────────────────────────────────────────────────

def interpret_quiz_answer(user_text: str, quiz_question: str, lang: str) -> str | None:
    try:
        r = get_client().messages.create(
            model="claude-haiku-4-5",
            max_tokens=5,
            messages=[{"role": "user", "content": (
                f"Quiz:\n{quiz_question}\n\nUser replied: \"{user_text}\"\n"
                "Which option? Reply ONLY A, B, C or UNCLEAR."
            )}]
        )
        result = r.content[0].text.strip().upper()
        return result if result in ("A", "B", "C") else None
    except Exception:
        return None


def detect_language_from_text(text: str) -> str | None:
    try:
        r = get_client().messages.create(
            model="claude-haiku-4-5",
            max_tokens=5,
            messages=[{"role": "user", "content": (
                f"User was asked language (EN/NL/DE/FR/ES). "
                f"They said: \"{text}\". Return ONLY the code or NONE."
            )}]
        )
        result = r.content[0].text.strip().upper()
        return result if result in ("EN", "NL", "DE", "FR", "ES") else None
    except Exception:
        return None


def answer_free_question(question: str, context: str, lang: str, name: str | None = None) -> str | None:
    hint = CONTINUE_HINTS.get(lang, CONTINUE_HINTS["EN"])
    text = _call(
        system=_persona(lang, name),
        user=f"Context: {context}\nQuestion: {question}\nAnswer briefly. Max 100 chars.",
        max_tokens=70,
    )
    if not text:
        return None
    return f"{text}\n\n{hint}"
