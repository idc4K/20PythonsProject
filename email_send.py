#Function for sending email with gmail


from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'xxxxxxxxxxxxxxxxxxxx'
email_password = 'xxxxxxxxxxxxxxxx'

email_recepteur = 'xxxxxxxxxxxxxxxx'

subject = "Test of send mail function"

body = """
Content of mail there!!!
"""

sender = EmailMessage()
sender["From"] = email_sender
sender["To"] = email_recepteur
sender["Subject"] = subject
sender.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smpt.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_recepteur,sender.as_string())