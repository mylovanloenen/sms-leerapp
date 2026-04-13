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
        "lessons": [
            {
                "EN": "opening the Messages app and reading a received SMS",
                "NL": "de Berichten-app openen en een ontvangen SMS lezen",
                "DE": "die Nachrichten-App öffnen und eine empfangene SMS lesen",
                "FR": "ouvrir l'application Messages et lire un SMS reçu",
                "ES": "abrir la aplicación Mensajes y leer un SMS recibido",
            },
            {
                "EN": "typing and sending a new SMS to a contact",
                "NL": "een nieuwe SMS typen en versturen naar een contact",
                "DE": "eine neue SMS tippen und an einen Kontakt senden",
                "FR": "taper et envoyer un nouveau SMS à un contact",
                "ES": "escribir y enviar un nuevo SMS a un contacto",
            },
        ],
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
        "lessons": [
            {
                "EN": "making a phone call: opening the dial pad and calling a number",
                "NL": "bellen: het toetsenbord openen en een nummer bellen",
                "DE": "Anruf tätigen: die Wähltastatur öffnen und eine Nummer anrufen",
                "FR": "passer un appel: ouvrir le clavier et appeler un numéro",
                "ES": "hacer una llamada: abrir el teclado y marcar un número",
            },
            {
                "EN": "saving a new contact with a name and phone number",
                "NL": "een nieuw contact opslaan met naam en telefoonnummer",
                "DE": "einen neuen Kontakt mit Name und Telefonnummer speichern",
                "FR": "enregistrer un nouveau contact avec un nom et un numéro",
                "ES": "guardar un nuevo contacto con nombre y número de teléfono",
            },
        ],
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
        "lessons": [
            {
                "EN": "installing WhatsApp and sending a first free text message",
                "NL": "WhatsApp installeren en een eerste gratis bericht sturen",
                "DE": "WhatsApp installieren und eine erste kostenlose Nachricht senden",
                "FR": "installer WhatsApp et envoyer un premier message gratuit",
                "ES": "instalar WhatsApp y enviar un primer mensaje gratuito",
            },
            {
                "EN": "sending a photo and making a video call via WhatsApp",
                "NL": "een foto sturen en videobellen via WhatsApp",
                "DE": "ein Foto senden und per WhatsApp videotelefonieren",
                "FR": "envoyer une photo et passer un appel vidéo via WhatsApp",
                "ES": "enviar una foto y hacer una videollamada por WhatsApp",
            },
        ],
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
        "lessons": [
            {
                "EN": "opening the email app and reading a received email",
                "NL": "de e-mailapp openen en een ontvangen e-mail lezen",
                "DE": "die E-Mail-App öffnen und eine empfangene E-Mail lesen",
                "FR": "ouvrir l'application email et lire un email reçu",
                "ES": "abrir la aplicación de correo y leer un correo recibido",
            },
            {
                "EN": "writing and sending a new email with subject and message",
                "NL": "een nieuwe e-mail schrijven en versturen met onderwerp en bericht",
                "DE": "eine neue E-Mail mit Betreff und Nachricht schreiben und senden",
                "FR": "écrire et envoyer un nouvel email avec objet et message",
                "ES": "escribir y enviar un nuevo correo con asunto y mensaje",
            },
        ],
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


def get_lesson_topic(module_id: int, lesson_nr: int, lang: str) -> str:
    """Geeft het specifieke sub-onderwerp voor les lesson_nr (1-based)."""
    module = get_module(module_id)
    if not module or "lessons" not in module:
        return module["topic"].get(lang, module["topic"]["EN"]) if module else ""
    lessons = module["lessons"]
    idx = lesson_nr - 1
    if idx < 0 or idx >= len(lessons):
        return module["topic"].get(lang, module["topic"]["EN"])
    return lessons[idx].get(lang, lessons[idx]["EN"])


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
