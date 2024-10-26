import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.mail_formatter import mail_format

load_dotenv()

def send_email_notification(job_type, num_jobs, website, recipient_email, found_jobs):
    sender_email = os.getenv('SENDER_EMAIL')
    formatted = mail_format(found_jobs)
    subject = f"New {job_type} Jobs Notification"
    if formatted:
        body = f"Here are {num_jobs} new {job_type} jobs from {website}." + formatted
    else:
        body = 'There were no new job offers found!'

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, os.getenv('SENDER_PASS'))
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
