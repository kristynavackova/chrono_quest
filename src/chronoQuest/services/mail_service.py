import os
import smtplib
from email.message import EmailMessage

class MailError(Exception):
    pass

def _gmail_send(msg: EmailMessage) -> None:
    user = os.getenv("GMAIL_USER")
    app_pw = os.getenv("GMAIL_APP_PASSWORD")
    if not user or not app_pw:
        raise MailError("GMAIL_USER / GMAIL_APP_PASSWORD nejsou k dispozici")

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as s:
        s.starttls()
        s.login(user, app_pw)
        s.send_message(msg)

def send_email(to: str, subject: str, html: str, reply_to: str | None = None) -> None:
   
   # Mail service pomocí Gmail SMTP
   # User a app password uložené mimo kód v env proměnných na serveru
    sender = os.getenv("GMAIL_USER")
    if not sender:
        raise MailError("Chybí GMAIL_USER")

    msg = EmailMessage()
    msg["From"] = sender              # u Gmailu musí být stejná adresa
    msg["To"] = to
    msg["Subject"] = subject
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content("Váš e-mailový klient nepodporuje HTML.")
    msg.add_alternative(html, subtype="html")

    # případný budoucí přepínač backendu (např. MAIL_BACKEND=sendgrid)
    backend = (os.getenv("MAIL_BACKEND") or "gmail").lower()
    if backend == "gmail":
        _gmail_send(msg)
    else:
        raise MailError(f"Neznámý MAIL_BACKEND: {backend}")