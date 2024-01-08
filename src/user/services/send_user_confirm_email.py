from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from src.core.config import SMTP_CONFIG

from .create_or_update_confirm_email_token import create_or_update_confirm_email_token


async def send_user_confirm_email(user):
    token = await create_or_update_confirm_email_token(user.id)
    message = MessageSchema(
        subject="Verification E-mail",
        recipients=[f"{user.email}"],
        template_body=[token],
        subtype=MessageType.html,
    )
    fm = FastMail(SMTP_CONFIG)
    await fm.send_message(message, template_name="confirm_email.html")
