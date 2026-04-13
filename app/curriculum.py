LANGUAGES = {
    "EN": "English",
    "NL": "Dutch",
    "DE": "German",
    "FR": "French",
    "ES": "Spanish",
}

WELCOME_MESSAGE = (
    "Welcome! 👋 What language?\n"
    "Welke taal? / Quelle langue?\n"
    "¿Idioma? / Welche Sprache?\n\n"
    "Reply: EN / NL / DE / FR / ES"
)

YES_WORDS = {
    "EN": ["YES", "Y", "OK", "OKAY", "SURE", "NEXT"],
    "NL": ["JA", "J", "OK", "OKEY", "ZEKER", "VOLGENDE"],
    "DE": ["JA", "J", "OK", "OKAY", "SICHER", "WEITER"],
    "FR": ["OUI", "O", "OK", "SUIVANT"],
    "ES": ["SÍ", "SI", "S", "OK", "CLARO"],
}

MODULES = [
    {
        "id": 1,
        "title": {"EN": "SMS", "NL": "SMS", "DE": "SMS", "FR": "SMS", "ES": "SMS"},
        "topic": {
            "EN": "sending and reading SMS text messages on a smartphone",
            "NL": "SMS-berichten sturen en lezen op een smartphone",
            "DE": "SMS-Nachrichten auf einem Smartphone senden und lesen",
            "FR": "envoyer et lire des SMS sur un smartphone",
            "ES": "enviar y leer SMS en un smartphone",
        },
        "steps": ["lesson", "quiz", "lesson", "quiz", "module_complete"],
    },
    {
        "id": 2,
        "title": {"EN": "Calling", "NL": "Bellen", "DE": "Telefonieren", "FR": "Appels", "ES": "Llamadas"},
        "topic": {
            "EN": "making phone calls and saving contacts on a smartphone",
            "NL": "bellen en contacten opslaan op een smartphone",
            "DE": "Telefonieren und Kontakte auf dem Smartphone speichern",
            "FR": "passer des appels et enregistrer des contacts",
            "ES": "hacer llamadas y guardar contactos en el teléfono",
        },
        "steps": ["lesson", "quiz", "lesson", "quiz", "module_complete"],
    },
    {
        "id": 3,
        "title": {"EN": "WhatsApp", "NL": "WhatsApp", "DE": "WhatsApp", "FR": "WhatsApp", "ES": "WhatsApp"},
        "topic": {
            "EN": "using WhatsApp to send free messages, photos and make video calls",
            "NL": "WhatsApp gebruiken voor gratis berichten, foto's en videobellen",
            "DE": "WhatsApp für kostenlose Nachrichten, Fotos und Videoanrufe",
            "FR": "utiliser WhatsApp pour messages gratuits, photos et appels vidéo",
            "ES": "usar WhatsApp para mensajes gratis, fotos y videollamadas",
        },
        "steps": ["lesson", "quiz", "lesson", "quiz", "module_complete"],
    },
    {
        "id": 4,
        "title": {"EN": "Email", "NL": "E-mail", "DE": "E-Mail", "FR": "Email", "ES": "Correo"},
        "topic": {
            "EN": "understanding and using email on a smartphone",
            "NL": "e-mail begrijpen en gebruiken op een smartphone",
            "DE": "E-Mail auf dem Smartphone verstehen und nutzen",
            "FR": "comprendre et utiliser l'email sur un smartphone",
            "ES": "entender y usar el correo electrónico en el teléfono",
        },
        "steps": ["lesson", "quiz", "lesson", "quiz", "module_complete"],
    },
]


def get_module(module_id: int) -> dict | None:
    for m in MODULES:
        if m["id"] == module_id:
            return m
    return None


def get_step_type(module_id: int, step_nr: int) -> str | None:
    module = get_module(module_id)
    if not module:
        return None
    steps = module["steps"]
    if step_nr < 1 or step_nr > len(steps):
        return None
    return steps[step_nr - 1]


def total_modules() -> int:
    return len(MODULES)


def steps_in_module(module_id: int) -> int:
    module = get_module(module_id)
    return len(module["steps"]) if module else 0


def total_steps() -> int:
    return sum(len(m["steps"]) for m in MODULES)


def completed_steps(module_id: int, step_nr: int) -> int:
    done = 0
    for m in MODULES:
        if m["id"] < module_id:
            done += len(m["steps"])
        elif m["id"] == module_id:
            done += step_nr - 1
    return done


def is_yes(text: str, language: str) -> bool:
    words = YES_WORDS.get(language, YES_WORDS["EN"])
    return text.strip().upper() in words


def lesson_index(module_id: int, step_nr: int) -> int:
    """Which lesson number is this within the module (1-based)."""
    module = get_module(module_id)
    if not module:
        return 1
    count = sum(1 for s in module["steps"][:step_nr - 1] if s == "lesson")
    return count + 1


def quiz_index(module_id: int, step_nr: int) -> int:
    """Which quiz number is this within the module (1-based)."""
    module = get_module(module_id)
    if not module:
        return 1
    count = sum(1 for s in module["steps"][:step_nr - 1] if s == "quiz")
    return count + 1
