import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import settings


def send_verify_email_message(verification_url, recipient_email):
    # SMTP server settings
    smtp_host = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    smtp_user = settings.EMAIL_HOST_USER
    smtp_password = settings.EMAIL_HOST_PASSWORD

    # Creating a letter
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = 'Confirmation email'

    # Text of the letter
    email_content = f'To confirm your email, follow the following link: {verification_url}'
    msg.attach(MIMEText(email_content, 'plain'))

    # Establishing a connection to an SMTP server
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()  # use TLS
    server.login(smtp_user, smtp_password)

    # Sending letter
    server.sendmail(smtp_user, recipient_email, msg.as_string())

    # Closing a connection
    server.quit()