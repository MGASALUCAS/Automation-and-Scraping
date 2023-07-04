import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, sender_email, receiver_email, password):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = "Hello!"

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))
    finally:
        server.quit()

# Set your email and password
sender_email = "mgasa.loucat1@gmail.com"
password = "YANGUMWENYEWEgoogle"

# List of recipient email addresses
receiver_emails = ["computerwizard2022@gmail.com", "maulidiadam1234@gmail.com"]

subject = "Hello"

while True:
    for receiver_email in receiver_emails:
        send_email(subject, sender_email, receiver_email, password)
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
