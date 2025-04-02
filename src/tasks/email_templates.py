from email.message import EmailMessage
from pydantic import EmailStr

from src.config import settings


def authorizate_user_confirmation_template(
    username: str,
    email_to: EmailStr
):
    email = EmailMessage()

    email["Subject"] = "Подтверждение бронирования"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Зарегистрировался новый пользователь</h1>
            Новый пользователь: {username}
        """,
        subtype="html"
    )

    return email
