"""发送邮件模块"""
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(
        receiver: str, title: str, content: str, qr_data: bytes,
        email_user: str, email_password: str, email_host: str, email_port: int,
):
    return
