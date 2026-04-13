LANGUAGES = {
    "EN": "English",
    "NL": "Nederlands",
    "DE": "Deutsch",
    "FR": "Français",
    "ES": "Español",
}

WELCOME_MESSAGE = (
    "Welcome! 👋 What language do you prefer?\n"
    "Welke taal spreek je?\n"
    "Welche Sprache möchten Sie?\n"
    "Quelle langue préférez-vous?\n"
    "¿Qué idioma prefiere?\n\n"
    "Reply / Antwoord: EN / NL / DE / FR / ES"
)

# YES synonyms per language (for module_complete steps)
YES_WORDS = {
    "EN": ["YES", "Y", "OK", "OKAY", "SURE"],
    "NL": ["JA", "J", "OK", "OKEY", "ZEKER"],
    "DE": ["JA", "J", "OK", "OKAY", "SICHER"],
    "FR": ["OUI", "O", "OK", "BIEN SÛR"],
    "ES": ["SÍ", "SI", "S", "OK", "CLARO"],
}

CURRICULUM = [
    # ─────────────────────────────────────────
    # MODULE 1 — SMS BASICS
    # ─────────────────────────────────────────
    {
        "module": 1,
        "title": {
            "EN": "Module 1: SMS Basics",
            "NL": "Module 1: SMS Basis",
            "DE": "Modul 1: SMS Grundlagen",
            "FR": "Module 1 : Les bases des SMS",
            "ES": "Módulo 1: Conceptos básicos de SMS",
        },
        "steps": [
            {
                "step": 1,
                "type": "lesson",
                "content": {
                    "EN": (
                        "📱 Welcome to your phone training!\n\n"
                        "Module 1: SMS Basics\n\n"
                        "SMS are text messages you send and receive on your phone. "
                        "You are using SMS right now! 😊\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "📱 Welkom bij je telefoontraining!\n\n"
                        "Module 1: SMS Basis\n\n"
                        "SMS zijn tekstberichten die je verstuurt en ontvangt op je telefoon. "
                        "Je gebruikt SMS op dit moment! 😊\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "📱 Willkommen zu Ihrem Telefontraining!\n\n"
                        "Modul 1: SMS-Grundlagen\n\n"
                        "SMS sind Textnachrichten, die Sie auf Ihrem Telefon senden und empfangen. "
                        "Sie benutzen gerade SMS! 😊\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "📱 Bienvenue dans votre formation téléphonique!\n\n"
                        "Module 1 : Les bases des SMS\n\n"
                        "Les SMS sont des messages texte que vous envoyez et recevez sur votre téléphone. "
                        "Vous utilisez les SMS en ce moment! 😊\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "📱 ¡Bienvenido a su entrenamiento telefónico!\n\n"
                        "Módulo 1: Conceptos básicos de SMS\n\n"
                        "Los SMS son mensajes de texto que envía y recibe en su teléfono. "
                        "¡Está usando SMS ahora mismo! 😊\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 2,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Quick quiz!\n\nWhat does SMS stand for?\n\nA) Simple Mobile Service\nB) Short Message Service\nC) Send More Stuff\n\nReply A, B or C:",
                    "NL": "🎯 Snelle quiz!\n\nWaar staat SMS voor?\n\nA) Simple Mobile Service\nB) Short Message Service\nC) Send More Stuff\n\nAntwoord A, B of C:",
                    "DE": "🎯 Kurzes Quiz!\n\nWofür steht SMS?\n\nA) Simple Mobile Service\nB) Short Message Service\nC) Send More Stuff\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Quiz rapide!\n\nQue signifie SMS?\n\nA) Simple Mobile Service\nB) Short Message Service\nC) Send More Stuff\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Quiz rápido!\n\n¿Qué significa SMS?\n\nA) Simple Mobile Service\nB) Short Message Service\nC) Send More Stuff\n\nResponda A, B o C:",
                },
                "correct": "B",
                "feedback_correct": {
                    "EN": "✅ Correct! SMS = Short Message Service. Well done!",
                    "NL": "✅ Correct! SMS = Short Message Service. Goed gedaan!",
                    "DE": "✅ Richtig! SMS = Short Message Service. Gut gemacht!",
                    "FR": "✅ Correct! SMS = Short Message Service. Bien joué!",
                    "ES": "✅ ¡Correcto! SMS = Short Message Service. ¡Bien hecho!",
                },
                "feedback_wrong": {
                    "EN": "❌ Not quite! The correct answer is B: Short Message Service. Keep going!",
                    "NL": "❌ Helaas! Het juiste antwoord is B: Short Message Service. Ga door!",
                    "DE": "❌ Leider falsch! Die richtige Antwort ist B: Short Message Service. Weiter!",
                    "FR": "❌ Pas tout à fait! La bonne réponse est B: Short Message Service. Continuez!",
                    "ES": "❌ ¡No exactamente! La respuesta correcta es B. ¡Siga adelante!",
                },
            },
            {
                "step": 3,
                "type": "lesson",
                "content": {
                    "EN": (
                        "📨 Reading an SMS\n\n"
                        "When you receive a message, your phone notifies you.\n\n"
                        "• iPhone → open the green 'Messages' app 💬\n"
                        "• Android → open the 'Messages' or 'SMS' app 📩\n\n"
                        "New messages appear at the top!\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "📨 Een SMS lezen\n\n"
                        "Als je een bericht ontvangt, krijg je een melding.\n\n"
                        "• iPhone → open de groene 'Berichten' app 💬\n"
                        "• Android → open de 'Berichten' of 'SMS' app 📩\n\n"
                        "Nieuwe berichten staan bovenaan!\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "📨 Eine SMS lesen\n\n"
                        "Wenn Sie eine Nachricht erhalten, werden Sie benachrichtigt.\n\n"
                        "• iPhone → öffnen Sie die grüne 'Nachrichten' App 💬\n"
                        "• Android → öffnen Sie die 'Nachrichten' App 📩\n\n"
                        "Neue Nachrichten erscheinen oben!\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "📨 Lire un SMS\n\n"
                        "Quand vous recevez un message, votre téléphone vous avertit.\n\n"
                        "• iPhone → ouvrez l'app verte 'Messages' 💬\n"
                        "• Android → ouvrez l'app 'Messages' 📩\n\n"
                        "Les nouveaux messages apparaissent en haut!\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "📨 Leer un SMS\n\n"
                        "Cuando recibe un mensaje, su teléfono le notifica.\n\n"
                        "• iPhone → abra la app verde 'Mensajes' 💬\n"
                        "• Android → abra la app 'Mensajes' 📩\n\n"
                        "¡Los mensajes nuevos aparecen arriba!\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 4,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Quiz!\n\nWhere do you find text messages on an iPhone?\n\nA) Blue 'Phone' app\nB) Green 'Messages' app\nC) Camera app\n\nReply A, B or C:",
                    "NL": "🎯 Quiz!\n\nWaar vind je berichten op een iPhone?\n\nA) Blauwe 'Telefoon' app\nB) Groene 'Berichten' app\nC) Camera app\n\nAntwoord A, B of C:",
                    "DE": "🎯 Quiz!\n\nWo finden Sie Textnachrichten auf einem iPhone?\n\nA) Blaue 'Telefon' App\nB) Grüne 'Nachrichten' App\nC) Kamera App\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Quiz!\n\nOù trouvez-vous les messages sur un iPhone?\n\nA) App bleue 'Téléphone'\nB) App verte 'Messages'\nC) App appareil photo\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Quiz!\n\n¿Dónde encuentra mensajes en un iPhone?\n\nA) App azul 'Teléfono'\nB) App verde 'Mensajes'\nC) App de cámara\n\nResponda A, B o C:",
                },
                "correct": "B",
                "feedback_correct": {
                    "EN": "✅ Correct! The green Messages app is where you find your texts.",
                    "NL": "✅ Correct! De groene Berichten app is voor je tekstberichten.",
                    "DE": "✅ Richtig! Die grüne Nachrichten App ist für Ihre Textnachrichten.",
                    "FR": "✅ Correct! L'app verte Messages est pour vos messages texte.",
                    "ES": "✅ ¡Correcto! La app verde Mensajes es para sus mensajes.",
                },
                "feedback_wrong": {
                    "EN": "❌ Almost! Correct answer: B — the green Messages app.",
                    "NL": "❌ Bijna! Juist antwoord: B — de groene Berichten app.",
                    "DE": "❌ Fast! Richtige Antwort: B — die grüne Nachrichten App.",
                    "FR": "❌ Presque! Bonne réponse: B — l'app verte Messages.",
                    "ES": "❌ ¡Casi! Respuesta correcta: B — la app verde Mensajes.",
                },
            },
            {
                "step": 5,
                "type": "lesson",
                "content": {
                    "EN": (
                        "✉️ Sending an SMS\n\n"
                        "1. Open the Messages app\n"
                        "2. Tap the pencil icon ✏️\n"
                        "3. Enter a phone number or name\n"
                        "4. Type your message\n"
                        "5. Press the send button ➡️\n\n"
                        "That's it! 😊\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "✉️ Een SMS sturen\n\n"
                        "1. Open de Berichten app\n"
                        "2. Tik op het potlood ✏️\n"
                        "3. Vul een nummer of naam in\n"
                        "4. Typ je bericht\n"
                        "5. Druk op de verzendknop ➡️\n\n"
                        "Dat is het! 😊\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "✉️ Eine SMS senden\n\n"
                        "1. Öffnen Sie die Nachrichten App\n"
                        "2. Tippen Sie auf das Stift-Symbol ✏️\n"
                        "3. Geben Sie Nummer oder Namen ein\n"
                        "4. Schreiben Sie Ihre Nachricht\n"
                        "5. Drücken Sie den Senden-Button ➡️\n\n"
                        "Das war's! 😊\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "✉️ Envoyer un SMS\n\n"
                        "1. Ouvrez l'app Messages\n"
                        "2. Appuyez sur le crayon ✏️\n"
                        "3. Entrez un numéro ou un nom\n"
                        "4. Tapez votre message\n"
                        "5. Appuyez sur envoyer ➡️\n\n"
                        "C'est tout! 😊\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "✉️ Enviar un SMS\n\n"
                        "1. Abra la app Mensajes\n"
                        "2. Toque el lápiz ✏️\n"
                        "3. Ingrese un número o nombre\n"
                        "4. Escriba su mensaje\n"
                        "5. Presione enviar ➡️\n\n"
                        "¡Eso es todo! 😊\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 6,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Final quiz for Module 1!\n\nWhat is the LAST step when sending an SMS?\n\nA) Type your name\nB) Press the send button ➡️\nC) Turn off your phone\n\nReply A, B or C:",
                    "NL": "🎯 Laatste quiz van Module 1!\n\nWat is de LAATSTE stap bij het sturen van een SMS?\n\nA) Typ je naam\nB) Druk op de verzendknop ➡️\nC) Zet je telefoon uit\n\nAntwoord A, B of C:",
                    "DE": "🎯 Letztes Quiz für Modul 1!\n\nWas ist der LETZTE Schritt beim SMS-Senden?\n\nA) Namen eingeben\nB) Senden-Button drücken ➡️\nC) Telefon ausschalten\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Dernier quiz du Module 1!\n\nQuelle est la DERNIÈRE étape pour envoyer un SMS?\n\nA) Taper votre nom\nB) Appuyer sur envoyer ➡️\nC) Éteindre votre téléphone\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Último quiz del Módulo 1!\n\n¿Cuál es el ÚLTIMO paso al enviar un SMS?\n\nA) Escribir su nombre\nB) Presionar enviar ➡️\nC) Apagar el teléfono\n\nResponda A, B o C:",
                },
                "correct": "B",
                "feedback_correct": {
                    "EN": "✅ Correct! Press the send button and your message is on its way!",
                    "NL": "✅ Correct! Druk op verzenden en je bericht is onderweg!",
                    "DE": "✅ Richtig! Senden-Button drücken und Ihre Nachricht ist unterwegs!",
                    "FR": "✅ Correct! Appuyez sur envoyer et votre message est en route!",
                    "ES": "✅ ¡Correcto! ¡Presione enviar y su mensaje está en camino!",
                },
                "feedback_wrong": {
                    "EN": "❌ The answer is B: press the send button!",
                    "NL": "❌ Het antwoord is B: druk op de verzendknop!",
                    "DE": "❌ Die Antwort ist B: Senden-Button drücken!",
                    "FR": "❌ La réponse est B: appuyer sur envoyer!",
                    "ES": "❌ ¡La respuesta es B: presionar enviar!",
                },
            },
            {
                "step": 7,
                "type": "module_complete",
                "content": {
                    "EN": (
                        "🏆 Module 1 Complete!\n\n"
                        "You now know SMS basics:\n"
                        "✅ What SMS is\n"
                        "✅ How to read messages\n"
                        "✅ How to send messages\n\n"
                        "Ready for Module 2: Calling & Contacts?\n"
                        "Reply YES to continue!"
                    ),
                    "NL": (
                        "🏆 Module 1 Voltooid!\n\n"
                        "Je kent nu de SMS-basis:\n"
                        "✅ Wat SMS is\n"
                        "✅ Hoe je berichten leest\n"
                        "✅ Hoe je berichten stuurt\n\n"
                        "Klaar voor Module 2: Bellen & Contacten?\n"
                        "Antwoord JA om door te gaan!"
                    ),
                    "DE": (
                        "🏆 Modul 1 Abgeschlossen!\n\n"
                        "Sie kennen jetzt die SMS-Grundlagen:\n"
                        "✅ Was SMS ist\n"
                        "✅ Wie man Nachrichten liest\n"
                        "✅ Wie man Nachrichten sendet\n\n"
                        "Bereit für Modul 2: Anrufen & Kontakte?\n"
                        "Antworten Sie JA um fortzufahren!"
                    ),
                    "FR": (
                        "🏆 Module 1 Terminé!\n\n"
                        "Vous connaissez les bases des SMS:\n"
                        "✅ Ce qu'est un SMS\n"
                        "✅ Comment lire les messages\n"
                        "✅ Comment envoyer des messages\n\n"
                        "Prêt pour le Module 2: Appels & Contacts?\n"
                        "Répondez OUI pour continuer!"
                    ),
                    "ES": (
                        "🏆 ¡Módulo 1 Completado!\n\n"
                        "Ahora conoce los básicos de SMS:\n"
                        "✅ Qué es SMS\n"
                        "✅ Cómo leer mensajes\n"
                        "✅ Cómo enviar mensajes\n\n"
                        "¿Listo para el Módulo 2: Llamadas y Contactos?\n"
                        "¡Responda SÍ para continuar!"
                    ),
                },
            },
        ],
    },

    # ─────────────────────────────────────────
    # MODULE 2 — CALLING & CONTACTS
    # ─────────────────────────────────────────
    {
        "module": 2,
        "title": {
            "EN": "Module 2: Calling & Contacts",
            "NL": "Module 2: Bellen & Contacten",
            "DE": "Modul 2: Anrufen & Kontakte",
            "FR": "Module 2 : Appels & Contacts",
            "ES": "Módulo 2: Llamadas y Contactos",
        },
        "steps": [
            {
                "step": 1,
                "type": "lesson",
                "content": {
                    "EN": (
                        "📞 Module 2: Calling & Contacts\n\n"
                        "Your phone can make and receive phone calls!\n\n"
                        "To make a call:\n"
                        "1. Open the 'Phone' app 📞\n"
                        "2. Tap the keypad icon\n"
                        "3. Type the number\n"
                        "4. Press the green call button 📞\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "📞 Module 2: Bellen & Contacten\n\n"
                        "Je telefoon kan ook bellen en gebeld worden!\n\n"
                        "Om te bellen:\n"
                        "1. Open de 'Telefoon' app 📞\n"
                        "2. Tik op het toetsenbord\n"
                        "3. Typ het nummer\n"
                        "4. Druk op de groene belknop 📞\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "📞 Modul 2: Anrufen & Kontakte\n\n"
                        "Ihr Telefon kann Anrufe tätigen und empfangen!\n\n"
                        "Um anzurufen:\n"
                        "1. Öffnen Sie die 'Telefon' App 📞\n"
                        "2. Tippen Sie auf die Tastatur\n"
                        "3. Geben Sie die Nummer ein\n"
                        "4. Drücken Sie den grünen Anruf-Button 📞\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "📞 Module 2 : Appels & Contacts\n\n"
                        "Votre téléphone peut faire et recevoir des appels!\n\n"
                        "Pour appeler:\n"
                        "1. Ouvrez l'app 'Téléphone' 📞\n"
                        "2. Appuyez sur le clavier\n"
                        "3. Tapez le numéro\n"
                        "4. Appuyez sur le bouton vert 📞\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "📞 Módulo 2: Llamadas y Contactos\n\n"
                        "¡Su teléfono puede hacer y recibir llamadas!\n\n"
                        "Para llamar:\n"
                        "1. Abra la app 'Teléfono' 📞\n"
                        "2. Toque el teclado\n"
                        "3. Escriba el número\n"
                        "4. Presione el botón verde 📞\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 2,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Quiz!\n\nWhat color is the call button?\n\nA) Red\nB) Blue\nC) Green\n\nReply A, B or C:",
                    "NL": "🎯 Quiz!\n\nWelke kleur heeft de belknop?\n\nA) Rood\nB) Blauw\nC) Groen\n\nAntwoord A, B of C:",
                    "DE": "🎯 Quiz!\n\nWelche Farbe hat der Anruf-Button?\n\nA) Rot\nB) Blau\nC) Grün\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Quiz!\n\nDe quelle couleur est le bouton d'appel?\n\nA) Rouge\nB) Bleu\nC) Vert\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Quiz!\n\n¿De qué color es el botón de llamada?\n\nA) Rojo\nB) Azul\nC) Verde\n\nResponda A, B o C:",
                },
                "correct": "C",
                "feedback_correct": {
                    "EN": "✅ Correct! The call button is green. Easy to remember!",
                    "NL": "✅ Correct! De belknop is groen. Makkelijk te onthouden!",
                    "DE": "✅ Richtig! Der Anruf-Button ist grün. Leicht zu merken!",
                    "FR": "✅ Correct! Le bouton d'appel est vert. Facile à retenir!",
                    "ES": "✅ ¡Correcto! El botón de llamada es verde. ¡Fácil de recordar!",
                },
                "feedback_wrong": {
                    "EN": "❌ The answer is C: Green! Green = go = call.",
                    "NL": "❌ Het antwoord is C: Groen! Groen = bellen.",
                    "DE": "❌ Die Antwort ist C: Grün! Grün = los = anrufen.",
                    "FR": "❌ La réponse est C: Vert! Vert = appeler.",
                    "ES": "❌ ¡La respuesta es C: Verde! Verde = llamar.",
                },
            },
            {
                "step": 3,
                "type": "lesson",
                "content": {
                    "EN": (
                        "👥 Saving Contacts\n\n"
                        "Save numbers as contacts so you don't have to remember them!\n\n"
                        "1. Open the 'Contacts' app\n"
                        "2. Tap the + button\n"
                        "3. Enter the person's name\n"
                        "4. Enter their phone number\n"
                        "5. Tap 'Save'\n\n"
                        "Now you can call them by name! 😊\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "👥 Contacten Opslaan\n\n"
                        "Sla nummers op als contacten, zodat je ze niet hoeft te onthouden!\n\n"
                        "1. Open de 'Contacten' app\n"
                        "2. Tik op de + knop\n"
                        "3. Vul de naam in\n"
                        "4. Vul het telefoonnummer in\n"
                        "5. Tik op 'Bewaar'\n\n"
                        "Nu kun je ze bij naam bellen! 😊\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "👥 Kontakte Speichern\n\n"
                        "Speichern Sie Nummern als Kontakte!\n\n"
                        "1. Öffnen Sie die 'Kontakte' App\n"
                        "2. Tippen Sie auf das + Symbol\n"
                        "3. Geben Sie den Namen ein\n"
                        "4. Geben Sie die Telefonnummer ein\n"
                        "5. Tippen Sie auf 'Sichern'\n\n"
                        "Jetzt können Sie beim Namen anrufen! 😊\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "👥 Enregistrer des Contacts\n\n"
                        "Enregistrez des numéros comme contacts!\n\n"
                        "1. Ouvrez l'app 'Contacts'\n"
                        "2. Appuyez sur le bouton +\n"
                        "3. Entrez le nom\n"
                        "4. Entrez le numéro de téléphone\n"
                        "5. Appuyez sur 'Enregistrer'\n\n"
                        "Vous pouvez maintenant appeler par nom! 😊\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "👥 Guardar Contactos\n\n"
                        "¡Guarde números como contactos!\n\n"
                        "1. Abra la app 'Contactos'\n"
                        "2. Toque el botón +\n"
                        "3. Ingrese el nombre\n"
                        "4. Ingrese el número\n"
                        "5. Toque 'Guardar'\n\n"
                        "¡Ahora puede llamarlos por nombre! 😊\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 4,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Quiz!\n\nWhich button do you press to add a new contact?\n\nA) The - button\nB) The + button\nC) The home button\n\nReply A, B or C:",
                    "NL": "🎯 Quiz!\n\nWelke knop druk je om een nieuw contact toe te voegen?\n\nA) De - knop\nB) De + knop\nC) De home knop\n\nAntwoord A, B of C:",
                    "DE": "🎯 Quiz!\n\nWelchen Button drücken Sie, um einen neuen Kontakt hinzuzufügen?\n\nA) Den - Button\nB) Den + Button\nC) Den Home Button\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Quiz!\n\nQuel bouton appuyez-vous pour ajouter un contact?\n\nA) Le bouton -\nB) Le bouton +\nC) Le bouton accueil\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Quiz!\n\n¿Qué botón presiona para agregar un contacto?\n\nA) El botón -\nB) El botón +\nC) El botón de inicio\n\nResponda A, B o C:",
                },
                "correct": "B",
                "feedback_correct": {
                    "EN": "✅ Correct! The + button adds new things — contacts, messages, and more!",
                    "NL": "✅ Correct! De + knop voegt nieuwe dingen toe — contacten, berichten en meer!",
                    "DE": "✅ Richtig! Der + Button fügt neue Dinge hinzu!",
                    "FR": "✅ Correct! Le bouton + ajoute de nouvelles choses!",
                    "ES": "✅ ¡Correcto! ¡El botón + agrega cosas nuevas!",
                },
                "feedback_wrong": {
                    "EN": "❌ The answer is B: the + button! Plus = add.",
                    "NL": "❌ Het antwoord is B: de + knop! Plus = toevoegen.",
                    "DE": "❌ Die Antwort ist B: der + Button! Plus = hinzufügen.",
                    "FR": "❌ La réponse est B: le bouton +! Plus = ajouter.",
                    "ES": "❌ ¡La respuesta es B: el botón +! Más = agregar.",
                },
            },
            {
                "step": 5,
                "type": "module_complete",
                "content": {
                    "EN": (
                        "🏆 Module 2 Complete!\n\n"
                        "You can now:\n"
                        "✅ Make phone calls\n"
                        "✅ Save contacts\n"
                        "✅ Call people by name\n\n"
                        "Ready for Module 3: WhatsApp?\n"
                        "Reply YES to continue!"
                    ),
                    "NL": (
                        "🏆 Module 2 Voltooid!\n\n"
                        "Je kunt nu:\n"
                        "✅ Telefoongesprekken maken\n"
                        "✅ Contacten opslaan\n"
                        "✅ Mensen bij naam bellen\n\n"
                        "Klaar voor Module 3: WhatsApp?\n"
                        "Antwoord JA om door te gaan!"
                    ),
                    "DE": (
                        "🏆 Modul 2 Abgeschlossen!\n\n"
                        "Sie können jetzt:\n"
                        "✅ Telefonanrufe tätigen\n"
                        "✅ Kontakte speichern\n"
                        "✅ Menschen beim Namen anrufen\n\n"
                        "Bereit für Modul 3: WhatsApp?\n"
                        "Antworten Sie JA um fortzufahren!"
                    ),
                    "FR": (
                        "🏆 Module 2 Terminé!\n\n"
                        "Vous pouvez maintenant:\n"
                        "✅ Passer des appels\n"
                        "✅ Enregistrer des contacts\n"
                        "✅ Appeler par nom\n\n"
                        "Prêt pour le Module 3: WhatsApp?\n"
                        "Répondez OUI pour continuer!"
                    ),
                    "ES": (
                        "🏆 ¡Módulo 2 Completado!\n\n"
                        "Ahora puede:\n"
                        "✅ Hacer llamadas\n"
                        "✅ Guardar contactos\n"
                        "✅ Llamar por nombre\n\n"
                        "¿Listo para el Módulo 3: WhatsApp?\n"
                        "¡Responda SÍ para continuar!"
                    ),
                },
            },
        ],
    },

    # ─────────────────────────────────────────
    # MODULE 3 — WHATSAPP
    # ─────────────────────────────────────────
    {
        "module": 3,
        "title": {
            "EN": "Module 3: WhatsApp",
            "NL": "Module 3: WhatsApp",
            "DE": "Modul 3: WhatsApp",
            "FR": "Module 3 : WhatsApp",
            "ES": "Módulo 3: WhatsApp",
        },
        "steps": [
            {
                "step": 1,
                "type": "lesson",
                "content": {
                    "EN": (
                        "💬 Module 3: WhatsApp\n\n"
                        "WhatsApp is a free app for messages, calls and photos!\n\n"
                        "Advantages:\n"
                        "• Free messages & calls (uses Wi-Fi)\n"
                        "• Send photos and videos\n"
                        "• Make video calls\n"
                        "• Group chats with family\n\n"
                        "Download it from the App Store (iPhone) or Play Store (Android).\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "💬 Module 3: WhatsApp\n\n"
                        "WhatsApp is een gratis app voor berichten, bellen en foto's!\n\n"
                        "Voordelen:\n"
                        "• Gratis berichten & bellen (via Wi-Fi)\n"
                        "• Foto's en video's sturen\n"
                        "• Videogesprekken voeren\n"
                        "• Groepsgesprekken met familie\n\n"
                        "Download het uit de App Store (iPhone) of Play Store (Android).\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "💬 Modul 3: WhatsApp\n\n"
                        "WhatsApp ist eine kostenlose App für Nachrichten, Anrufe und Fotos!\n\n"
                        "Vorteile:\n"
                        "• Kostenlose Nachrichten & Anrufe (über WLAN)\n"
                        "• Fotos und Videos senden\n"
                        "• Videoanrufe\n"
                        "• Gruppenunterhaltungen mit Familie\n\n"
                        "Laden Sie es aus dem App Store (iPhone) oder Play Store (Android) herunter.\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "💬 Module 3 : WhatsApp\n\n"
                        "WhatsApp est une app gratuite pour messages, appels et photos!\n\n"
                        "Avantages:\n"
                        "• Messages & appels gratuits (via Wi-Fi)\n"
                        "• Envoyer photos et vidéos\n"
                        "• Appels vidéo\n"
                        "• Groupes de discussion en famille\n\n"
                        "Téléchargez-le depuis l'App Store (iPhone) ou Play Store (Android).\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "💬 Módulo 3: WhatsApp\n\n"
                        "¡WhatsApp es una app gratuita para mensajes, llamadas y fotos!\n\n"
                        "Ventajas:\n"
                        "• Mensajes y llamadas gratis (con Wi-Fi)\n"
                        "• Enviar fotos y videos\n"
                        "• Videollamadas\n"
                        "• Chats de grupo con familia\n\n"
                        "Descárguela de la App Store (iPhone) o Play Store (Android).\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 2,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Quiz!\n\nWhere do you safely download WhatsApp on iPhone?\n\nA) From any website\nB) From the App Store\nC) From a friend's phone\n\nReply A, B or C:",
                    "NL": "🎯 Quiz!\n\nWaar download je WhatsApp veilig op een iPhone?\n\nA) Van een willekeurige website\nB) Uit de App Store\nC) Van de telefoon van een vriend\n\nAntwoord A, B of C:",
                    "DE": "🎯 Quiz!\n\nWo laden Sie WhatsApp sicher auf einem iPhone herunter?\n\nA) Von einer beliebigen Website\nB) Aus dem App Store\nC) Vom Telefon eines Freundes\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Quiz!\n\nOù télécharger WhatsApp en sécurité sur iPhone?\n\nA) Depuis n'importe quel site web\nB) Depuis l'App Store\nC) Depuis le téléphone d'un ami\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Quiz!\n\n¿Dónde descarga WhatsApp de forma segura en iPhone?\n\nA) De cualquier sitio web\nB) De la App Store\nC) Del teléfono de un amigo\n\nResponda A, B o C:",
                },
                "correct": "B",
                "feedback_correct": {
                    "EN": "✅ Correct! Always use the official App Store or Play Store. Never download apps from random websites!",
                    "NL": "✅ Correct! Gebruik altijd de officiële App Store of Play Store. Download nooit apps van willekeurige websites!",
                    "DE": "✅ Richtig! Verwenden Sie immer den offiziellen App Store oder Play Store. Laden Sie nie Apps von beliebigen Websites herunter!",
                    "FR": "✅ Correct! Utilisez toujours l'App Store ou Play Store officiel. Ne téléchargez jamais depuis des sites inconnus!",
                    "ES": "✅ ¡Correcto! Use siempre la App Store o Play Store oficial. ¡Nunca descargue apps de sitios desconocidos!",
                },
                "feedback_wrong": {
                    "EN": "❌ The answer is B: App Store! Official stores keep your phone safe.",
                    "NL": "❌ Het antwoord is B: App Store! Officiële winkels houden je telefoon veilig.",
                    "DE": "❌ Die Antwort ist B: App Store! Offizielle Stores halten Ihr Telefon sicher.",
                    "FR": "❌ La réponse est B: App Store! Les stores officiels protègent votre téléphone.",
                    "ES": "❌ ¡La respuesta es B: App Store! Las tiendas oficiales mantienen su teléfono seguro.",
                },
            },
            {
                "step": 3,
                "type": "lesson",
                "content": {
                    "EN": (
                        "📸 Sending Photos on WhatsApp\n\n"
                        "1. Open a conversation in WhatsApp\n"
                        "2. Tap the 📎 clip or 📷 camera icon\n"
                        "3. Choose a photo from your gallery\n"
                        "   (or take a new photo)\n"
                        "4. Press send ➡️\n\n"
                        "The photo arrives instantly! 🖼️\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "📸 Foto's sturen op WhatsApp\n\n"
                        "1. Open een gesprek in WhatsApp\n"
                        "2. Tik op het 📎 paperclip of 📷 camera icoon\n"
                        "3. Kies een foto uit je galerij\n"
                        "   (of maak een nieuwe foto)\n"
                        "4. Druk op verzenden ➡️\n\n"
                        "De foto komt meteen aan! 🖼️\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "📸 Fotos auf WhatsApp senden\n\n"
                        "1. Öffnen Sie eine Unterhaltung\n"
                        "2. Tippen Sie auf 📎 oder 📷\n"
                        "3. Wählen Sie ein Foto aus der Galerie\n"
                        "   (oder machen Sie ein neues)\n"
                        "4. Drücken Sie Senden ➡️\n\n"
                        "Das Foto kommt sofort an! 🖼️\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "📸 Envoyer des photos sur WhatsApp\n\n"
                        "1. Ouvrez une conversation\n"
                        "2. Appuyez sur 📎 ou 📷\n"
                        "3. Choisissez une photo de votre galerie\n"
                        "   (ou prenez-en une nouvelle)\n"
                        "4. Appuyez sur envoyer ➡️\n\n"
                        "La photo arrive instantanément! 🖼️\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "📸 Enviar fotos en WhatsApp\n\n"
                        "1. Abra una conversación\n"
                        "2. Toque 📎 o 📷\n"
                        "3. Elija una foto de su galería\n"
                        "   (o tome una nueva)\n"
                        "4. Presione enviar ➡️\n\n"
                        "¡La foto llega al instante! 🖼️\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 4,
                "type": "module_complete",
                "content": {
                    "EN": (
                        "🏆 Module 3 Complete!\n\n"
                        "You know WhatsApp basics:\n"
                        "✅ What WhatsApp is\n"
                        "✅ How to download apps safely\n"
                        "✅ How to send photos\n\n"
                        "Ready for Module 4: Email?\n"
                        "Reply YES to continue!"
                    ),
                    "NL": (
                        "🏆 Module 3 Voltooid!\n\n"
                        "Je kent de basis van WhatsApp:\n"
                        "✅ Wat WhatsApp is\n"
                        "✅ Hoe je apps veilig downloadt\n"
                        "✅ Hoe je foto's stuurt\n\n"
                        "Klaar voor Module 4: E-mail?\n"
                        "Antwoord JA om door te gaan!"
                    ),
                    "DE": (
                        "🏆 Modul 3 Abgeschlossen!\n\n"
                        "Sie kennen WhatsApp-Grundlagen:\n"
                        "✅ Was WhatsApp ist\n"
                        "✅ Apps sicher herunterladen\n"
                        "✅ Fotos senden\n\n"
                        "Bereit für Modul 4: E-Mail?\n"
                        "Antworten Sie JA um fortzufahren!"
                    ),
                    "FR": (
                        "🏆 Module 3 Terminé!\n\n"
                        "Vous connaissez les bases de WhatsApp:\n"
                        "✅ Ce qu'est WhatsApp\n"
                        "✅ Télécharger des apps en sécurité\n"
                        "✅ Envoyer des photos\n\n"
                        "Prêt pour le Module 4: Email?\n"
                        "Répondez OUI pour continuer!"
                    ),
                    "ES": (
                        "🏆 ¡Módulo 3 Completado!\n\n"
                        "Conoce los básicos de WhatsApp:\n"
                        "✅ Qué es WhatsApp\n"
                        "✅ Descargar apps de forma segura\n"
                        "✅ Enviar fotos\n\n"
                        "¿Listo para el Módulo 4: Correo?\n"
                        "¡Responda SÍ para continuar!"
                    ),
                },
            },
        ],
    },

    # ─────────────────────────────────────────
    # MODULE 4 — EMAIL
    # ─────────────────────────────────────────
    {
        "module": 4,
        "title": {
            "EN": "Module 4: Email",
            "NL": "Module 4: E-mail",
            "DE": "Modul 4: E-Mail",
            "FR": "Module 4 : Email",
            "ES": "Módulo 4: Correo Electrónico",
        },
        "steps": [
            {
                "step": 1,
                "type": "lesson",
                "content": {
                    "EN": (
                        "📧 Module 4: Email\n\n"
                        "Email is like a digital letter!\n\n"
                        "An email address looks like:\n"
                        "  name@provider.com\n"
                        "  Example: jan@gmail.com\n\n"
                        "Every email has:\n"
                        "• To: who receives it\n"
                        "• Subject: the topic\n"
                        "• Message: your text\n"
                        "• Attachment: files/photos (optional)\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "📧 Module 4: E-mail\n\n"
                        "E-mail is als een digitale brief!\n\n"
                        "Een e-mailadres ziet er zo uit:\n"
                        "  naam@provider.com\n"
                        "  Voorbeeld: jan@gmail.com\n\n"
                        "Elk e-mail heeft:\n"
                        "• Aan: wie het ontvangt\n"
                        "• Onderwerp: het onderwerp\n"
                        "• Bericht: jouw tekst\n"
                        "• Bijlage: bestanden/foto's (optioneel)\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "📧 Modul 4: E-Mail\n\n"
                        "E-Mail ist wie ein digitaler Brief!\n\n"
                        "Eine E-Mail-Adresse sieht so aus:\n"
                        "  name@anbieter.com\n"
                        "  Beispiel: hans@gmail.com\n\n"
                        "Jede E-Mail hat:\n"
                        "• An: wer sie empfängt\n"
                        "• Betreff: das Thema\n"
                        "• Nachricht: Ihr Text\n"
                        "• Anhang: Dateien/Fotos (optional)\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "📧 Module 4 : Email\n\n"
                        "L'email c'est comme une lettre numérique!\n\n"
                        "Une adresse email ressemble à:\n"
                        "  nom@fournisseur.com\n"
                        "  Exemple: jean@gmail.com\n\n"
                        "Chaque email a:\n"
                        "• À: qui le reçoit\n"
                        "• Objet: le sujet\n"
                        "• Message: votre texte\n"
                        "• Pièce jointe: fichiers/photos (optionnel)\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "📧 Módulo 4: Correo Electrónico\n\n"
                        "¡El correo es como una carta digital!\n\n"
                        "Una dirección de correo se ve así:\n"
                        "  nombre@proveedor.com\n"
                        "  Ejemplo: juan@gmail.com\n\n"
                        "Cada correo tiene:\n"
                        "• Para: quién lo recibe\n"
                        "• Asunto: el tema\n"
                        "• Mensaje: su texto\n"
                        "• Adjunto: archivos/fotos (opcional)\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 2,
                "type": "quiz",
                "question": {
                    "EN": "🎯 Quiz!\n\nWhat symbol is ALWAYS in an email address?\n\nA) The # symbol\nB) The @ symbol\nC) The * symbol\n\nReply A, B or C:",
                    "NL": "🎯 Quiz!\n\nWelk symbool zit er ALTIJD in een e-mailadres?\n\nA) Het # symbool\nB) Het @ symbool\nC) Het * symbool\n\nAntwoord A, B of C:",
                    "DE": "🎯 Quiz!\n\nWelches Symbol ist IMMER in einer E-Mail-Adresse?\n\nA) Das # Symbol\nB) Das @ Symbol\nC) Das * Symbol\n\nAntworten Sie A, B oder C:",
                    "FR": "🎯 Quiz!\n\nQuel symbole est TOUJOURS dans une adresse email?\n\nA) Le symbole #\nB) Le symbole @\nC) Le symbole *\n\nRépondez A, B ou C:",
                    "ES": "🎯 ¡Quiz!\n\n¿Qué símbolo hay SIEMPRE en una dirección de correo?\n\nA) El símbolo #\nB) El símbolo @\nC) El símbolo *\n\nResponda A, B o C:",
                },
                "correct": "B",
                "feedback_correct": {
                    "EN": "✅ Correct! The @ symbol is in every email address. It means 'at'.",
                    "NL": "✅ Correct! Het @ symbool (apenstaartje) zit in elk e-mailadres.",
                    "DE": "✅ Richtig! Das @ Symbol (At-Zeichen) ist in jeder E-Mail-Adresse.",
                    "FR": "✅ Correct! Le symbole @ (arobase) est dans chaque adresse email.",
                    "ES": "✅ ¡Correcto! El símbolo @ (arroba) está en cada dirección de correo.",
                },
                "feedback_wrong": {
                    "EN": "❌ The answer is B: @! Like: name@gmail.com",
                    "NL": "❌ Het antwoord is B: @! Zoals: naam@gmail.com",
                    "DE": "❌ Die Antwort ist B: @! Wie: name@gmail.com",
                    "FR": "❌ La réponse est B: @! Comme: nom@gmail.com",
                    "ES": "❌ ¡La respuesta es B: @! Como: nombre@gmail.com",
                },
            },
            {
                "step": 3,
                "type": "lesson",
                "content": {
                    "EN": (
                        "📤 Sending an Email\n\n"
                        "1. Open your email app (Gmail, Mail, etc.)\n"
                        "2. Tap the compose / pencil button ✏️\n"
                        "3. Fill in 'To:' with the email address\n"
                        "4. Fill in 'Subject:' with a short title\n"
                        "5. Write your message\n"
                        "6. Tap the send button ➡️\n\n"
                        "Just like writing a letter, but instant! 📬\n\n"
                        "Reply OK to continue."
                    ),
                    "NL": (
                        "📤 Een E-mail Sturen\n\n"
                        "1. Open je e-mail app (Gmail, Mail, etc.)\n"
                        "2. Tik op het schrijf / potlood knopje ✏️\n"
                        "3. Vul 'Aan:' in met het e-mailadres\n"
                        "4. Vul 'Onderwerp:' in met een korte titel\n"
                        "5. Schrijf je bericht\n"
                        "6. Tik op de verzendknop ➡️\n\n"
                        "Net als een brief schrijven, maar dan direct! 📬\n\n"
                        "Antwoord OK om door te gaan."
                    ),
                    "DE": (
                        "📤 Eine E-Mail Senden\n\n"
                        "1. Öffnen Sie Ihre E-Mail App (Gmail, Mail, etc.)\n"
                        "2. Tippen Sie auf Verfassen / Stift ✏️\n"
                        "3. Geben Sie bei 'An:' die E-Mail-Adresse ein\n"
                        "4. Geben Sie bei 'Betreff:' einen kurzen Titel ein\n"
                        "5. Schreiben Sie Ihre Nachricht\n"
                        "6. Tippen Sie auf Senden ➡️\n\n"
                        "Wie einen Brief schreiben, aber sofort! 📬\n\n"
                        "Antworten Sie OK zum Fortfahren."
                    ),
                    "FR": (
                        "📤 Envoyer un Email\n\n"
                        "1. Ouvrez votre app email (Gmail, Mail, etc.)\n"
                        "2. Appuyez sur rédiger / crayon ✏️\n"
                        "3. Remplissez 'À:' avec l'adresse email\n"
                        "4. Remplissez 'Objet:' avec un titre court\n"
                        "5. Écrivez votre message\n"
                        "6. Appuyez sur envoyer ➡️\n\n"
                        "Comme écrire une lettre, mais instantané! 📬\n\n"
                        "Répondez OK pour continuer."
                    ),
                    "ES": (
                        "📤 Enviar un Correo\n\n"
                        "1. Abra su app de correo (Gmail, Mail, etc.)\n"
                        "2. Toque redactar / lápiz ✏️\n"
                        "3. Complete 'Para:' con la dirección\n"
                        "4. Complete 'Asunto:' con un título corto\n"
                        "5. Escriba su mensaje\n"
                        "6. Toque enviar ➡️\n\n"
                        "¡Como escribir una carta, pero instantáneo! 📬\n\n"
                        "Responda OK para continuar."
                    ),
                },
            },
            {
                "step": 4,
                "type": "module_complete",
                "content": {
                    "EN": (
                        "🎉 CONGRATULATIONS!\n\n"
                        "You have completed ALL 4 modules!\n\n"
                        "You can now:\n"
                        "📱 Send & receive SMS\n"
                        "📞 Make calls & save contacts\n"
                        "💬 Use WhatsApp\n"
                        "📧 Send emails\n\n"
                        "You are a phone pro! 🌟\n\n"
                        "Want to restart the training? Reply RESTART."
                    ),
                    "NL": (
                        "🎉 GEFELICITEERD!\n\n"
                        "Je hebt ALLE 4 modules voltooid!\n\n"
                        "Je kunt nu:\n"
                        "📱 SMS sturen en ontvangen\n"
                        "📞 Bellen en contacten opslaan\n"
                        "💬 WhatsApp gebruiken\n"
                        "📧 E-mails sturen\n\n"
                        "Je bent een telefoonpro! 🌟\n\n"
                        "Wil je opnieuw beginnen? Antwoord OPNIEUW."
                    ),
                    "DE": (
                        "🎉 HERZLICHEN GLÜCKWUNSCH!\n\n"
                        "Sie haben ALLE 4 Module abgeschlossen!\n\n"
                        "Sie können jetzt:\n"
                        "📱 SMS senden und empfangen\n"
                        "📞 Anrufen und Kontakte speichern\n"
                        "💬 WhatsApp nutzen\n"
                        "📧 E-Mails senden\n\n"
                        "Sie sind ein Telefon-Profi! 🌟\n\n"
                        "Neu starten? Antworten Sie NEU."
                    ),
                    "FR": (
                        "🎉 FÉLICITATIONS!\n\n"
                        "Vous avez terminé TOUS les 4 modules!\n\n"
                        "Vous pouvez maintenant:\n"
                        "📱 Envoyer et recevoir des SMS\n"
                        "📞 Appeler et enregistrer des contacts\n"
                        "💬 Utiliser WhatsApp\n"
                        "📧 Envoyer des emails\n\n"
                        "Vous êtes un pro du téléphone! 🌟\n\n"
                        "Recommencer? Répondez RECOMMENCER."
                    ),
                    "ES": (
                        "🎉 ¡FELICITACIONES!\n\n"
                        "¡Ha completado TODOS los 4 módulos!\n\n"
                        "Ahora puede:\n"
                        "📱 Enviar y recibir SMS\n"
                        "📞 Llamar y guardar contactos\n"
                        "💬 Usar WhatsApp\n"
                        "📧 Enviar correos\n\n"
                        "¡Es un profesional del teléfono! 🌟\n\n"
                        "¿Reiniciar? Responda REINICIAR."
                    ),
                },
            },
        ],
    },
]


def get_module(module_nr: int) -> dict | None:
    for m in CURRICULUM:
        if m["module"] == module_nr:
            return m
    return None


def get_step(module_nr: int, step_nr: int) -> dict | None:
    module = get_module(module_nr)
    if not module:
        return None
    for s in module["steps"]:
        if s["step"] == step_nr:
            return s
    return None


def total_modules() -> int:
    return len(CURRICULUM)


def is_yes(text: str, language: str) -> bool:
    words = YES_WORDS.get(language, YES_WORDS["EN"])
    return text.strip().upper() in words
