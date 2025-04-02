from src.tasks.celery import celery
from pathlib import Path
from pydantic import EmailStr
import smtplib

from src.config import settings
from src.tasks.email_templates import authorizate_user_confirmation_template


@celery.task
def send_usern_confirmation_email(
    username: str,
    email_to: EmailStr,
):
    email_to_mock = settings.SMTP_USER
    msg_content = authorizate_user_confirmation_template(username, email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
