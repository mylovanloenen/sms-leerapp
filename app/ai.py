"""
Claude AI — genereert alle lesinhoud, quizvragen en feedback dynamisch.
Gebruikt claude-haiku-4-5 voor snelle, goedkope antwoorden.
Alle berichten worden kort gehouden (<320 tekens = max 2 SMS).
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
    "DE": "Antworten Sie JA um fortzufahren!",
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


# ── Content generation ────────────────────────────────────────────────────────

def generate_lesson(topic: str, lesson_nr: int, lang: str) -> str:
    """Genereer een korte les over het onderwerp. Max 1 SMS (160 tekens)."""
    lang_name = LANG_NAMES.get(lang, "English")
    hint = CONTINUE_HINTS.get(lang, CONTINUE_HINTS["EN"])

    text = _call(
        system=(
            f"You are a warm phone trainer teaching elderly people via SMS. "
            f"Write ONLY in {lang_name}. "
            f"Keep your response under 130 characters. "
            f"Use simple words, 1 emoji, short sentences."
        ),
        user=f"Lesson {lesson_nr} about: {topic}. Max 130 chars.",
        max_tokens=80,
    )

    if not text:
        # Fallback
        fallbacks = {
            "EN": f"📱 Lesson {lesson_nr}: Let's learn about {topic}!",
            "NL": f"📱 Les {lesson_nr}: We leren over {topic}!",
            "DE": f"📱 Lektion {lesson_nr}: Wir lernen über {topic}!",
            "FR": f"📱 Leçon {lesson_nr}: Apprenons sur {topic}!",
            "ES": f"📱 Lección {lesson_nr}: ¡Aprendamos sobre {topic}!",
        }
        text = fallbacks.get(lang, fallbacks["EN"])

    return f"{text}\n\n{hint}"


def generate_quiz(topic: str, quiz_nr: int, lang: str) -> dict | None:
    """
    Genereer een meerkeuze quizvraag.
    Returnt: {text: str, correct: A/B/C}
    """
    lang_name = LANG_NAMES.get(lang, "English")
    hint = QUIZ_HINTS.get(lang, QUIZ_HINTS["EN"])

    raw = _call(
        system=(
            f"Create a simple multiple choice quiz for elderly phone learners. "
            f"Write ONLY in {lang_name}. Keep it short and clear."
        ),
        user=(
            f"Quiz {quiz_nr} about: {topic}\n"
            f"Format exactly like this (nothing else):\n"
            f"Q: [short question, max 60 chars]\n"
            f"A) [option]\n"
            f"B) [option]\n"
            f"C) [option]\n"
            f"CORRECT: [A or B or C]"
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
            correct = line.split("CORRECT:")[-1].strip().upper()
            if correct and correct[0] in "ABC":
                correct = correct[0]

    if not (q and a and b and c and correct in ("A", "B", "C")):
        return None

    text = f"🎯 {q}\n\nA) {a}\nB) {b}\nC) {c}\n\n{hint}"
    return {"text": text, "correct": correct}


def generate_feedback(correct: bool, chosen: str, right: str, lang: str) -> str:
    """Korte feedback na een quizantwoord. Max 100 tekens."""
    lang_name = LANG_NAMES.get(lang, "English")

    text = _call(
        system=f"Respond ONLY in {lang_name}. Max 90 characters. Use 1 emoji.",
        user=(
            f"Quiz answer: {'CORRECT ✅' if correct else f'WRONG ❌ (right answer: {right})'}. "
            f"Give {'encouraging' if correct else 'gentle corrective'} feedback. Max 90 chars."
        ),
        max_tokens=60,
    )

    if not text:
        if correct:
            return {"EN": "✅ Correct!", "NL": "✅ Goed zo!", "DE": "✅ Richtig!", "FR": "✅ Correct!", "ES": "✅ ¡Correcto!"}.get(lang, "✅ Correct!")
        else:
            return {"EN": f"❌ Wrong! Answer: {right}", "NL": f"❌ Fout! Antwoord: {right}", "DE": f"❌ Falsch! Antwort: {right}", "FR": f"❌ Faux! Réponse: {right}", "ES": f"❌ ¡Mal! Respuesta: {right}"}.get(lang, f"❌ Wrong! Answer: {right}")

    return text


def generate_module_complete(module_title: str, next_title: str | None, lang: str) -> str:
    """Module afrondingsbericht. Max 160 tekens."""
    lang_name = LANG_NAMES.get(lang, "English")

    if next_title:
        hint = YES_HINTS.get(lang, YES_HINTS["EN"])
        text = _call(
            system=f"Respond ONLY in {lang_name}. Max 100 characters. Use 1 emoji.",
            user=f"Module '{module_title}' done! Next: '{next_title}'. Short congratulation. Max 100 chars.",
            max_tokens=60,
        )
        if not text:
            text = {"EN": f"🏆 {module_title} complete!", "NL": f"🏆 {module_title} klaar!", "DE": f"🏆 {module_title} fertig!", "FR": f"🏆 {module_title} terminé!", "ES": f"🏆 ¡{module_title} completado!"}.get(lang, f"🏆 {module_title} done!")
        return f"{text}\n\n{hint}"
    else:
        restart = {"EN": "Reply RESTART to start over.", "NL": "Antwoord OPNIEUW om opnieuw te beginnen.", "DE": "Antworten Sie NEU.", "FR": "Répondez RECOMMENCER.", "ES": "Responda REINICIAR."}.get(lang, "Reply RESTART.")
        text = _call(
            system=f"Respond ONLY in {lang_name}. Max 130 characters. Use emojis. Be celebratory!",
            user="All 4 phone training modules complete! Big celebration message. Max 130 chars.",
            max_tokens=80,
        )
        if not text:
            text = {"EN": "🎉 You did it! All modules complete! You're a phone pro! 🌟", "NL": "🎉 Gelukt! Alle modules klaar! Je bent een telefoonpro! 🌟"}.get(lang, "🎉 All done! 🌟")
        return f"{text}\n\n{restart}"


# ── Natural language understanding ────────────────────────────────────────────

def interpret_quiz_answer(user_text: str, quiz_question: str, lang: str) -> str | None:
    """Begrijpt een vrij-tekst antwoord als A, B of C."""
    try:
        r = get_client().messages.create(
            model="claude-haiku-4-5",
            max_tokens=5,
            messages=[{
                "role": "user",
                "content": (
                    f"Quiz question:\n{quiz_question}\n\n"
                    f"User replied: \"{user_text}\"\n\n"
                    "Which option is the user choosing? Reply ONLY with A, B, C or UNCLEAR."
                )
            }]
        )
        result = r.content[0].text.strip().upper()
        return result if result in ("A", "B", "C") else None
    except Exception:
        return None


def detect_language_from_text(text: str) -> str | None:
    """Detecteert taalvoorkeur uit vrije tekst."""
    try:
        r = get_client().messages.create(
            model="claude-haiku-4-5",
            max_tokens=5,
            messages=[{
                "role": "user",
                "content": (
                    f"User was asked language preference (EN/NL/DE/FR/ES). "
                    f"They said: \"{text}\". "
                    "Return ONLY the 2-letter code or NONE."
                )
            }]
        )
        result = r.content[0].text.strip().upper()
        return result if result in ("EN", "NL", "DE", "FR", "ES") else None
    except Exception:
        return None


def answer_free_question(question: str, context: str, lang: str) -> str | None:
    """Beantwoordt een vrije vraag van de gebruiker. Max 120 tekens."""
    lang_name = LANG_NAMES.get(lang, "English")
    hint = CONTINUE_HINTS.get(lang, CONTINUE_HINTS["EN"])

    text = _call(
        system=(
            f"You are a friendly phone trainer for elderly people. "
            f"Respond ONLY in {lang_name}. Max 100 characters. Simple words, 1 emoji."
        ),
        user=f"Context: {context}\nQuestion: {question}\nAnswer briefly. Max 100 chars.",
        max_tokens=70,
    )

    if not text:
        return None

    return f"{text}\n\n{hint}"
