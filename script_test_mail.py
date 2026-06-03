import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "tonadresse@gmail.com"
APP_PASSWORD = "ton_mot_de_passe_application"

TEST_RECIPIENTS = [
    "test1@gmail.com",
    "Test2@gmail.com"
]

CV_FILE = "VotreCV.pdf"
LM_FILE = "VotreLM.pdf"

MAIL_SUBJECT = "Test candidature alternance 2026 - Technicien support informatique"

MAIL_BODY = """Madame, Monsieur,

Actuellement étudiant en BTS SIO, je recherche une alternance pour la rentrée de septembre 2026 et souhaite candidater au poste de Technicien support informatique au sein de votre entreprise.

Les missions proposées, notamment le support de premier niveau, le traitement des incidents, la gestion du parc informatique et l’installation des postes de travail, correspondent pleinement à mon projet professionnel.

Au cours de ma formation, j’ai développé des compétences en administration système, support informatique et réseau à travers plusieurs projets techniques autour d’Active Directory, GLPI, pfSense, Debian et la virtualisation. Ces expériences m’ont permis de développer ma rigueur, mon sens de l’organisation et ma capacité à diagnostiquer des problèmes techniques.

Motivé, sérieux et impliqué, je souhaite mettre mes compétences au service de vos équipes et évoluer dans un environnement formateur et structuré.

L’ensemble de mes projets et certifications est disponible sur mon portfolio : boumrahsamy.fr.

Je vous prie d’agréer, Madame, Monsieur, l’expression de mes salutations distinguées.

Samy Boumrah
"""


def attach_file(msg, filepath):
    with open(filepath, "rb") as f:
        data = f.read()
        filename = os.path.basename(filepath)
        msg.add_attachment(
            data,
            maintype="application",
            subtype="pdf",
            filename=filename
        )


def build_message(to_email):
    msg = EmailMessage()
    msg["Subject"] = MAIL_SUBJECT
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg.set_content(MAIL_BODY)

    attach_file(msg, CV_FILE)
    attach_file(msg, LM_FILE)
    return msg


def main():
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)

        for recipient in TEST_RECIPIENTS:
            msg = build_message(recipient)
            server.send_message(msg)
            print(f"Mail envoyé à {recipient}")


if __name__ == "__main__":
    main()