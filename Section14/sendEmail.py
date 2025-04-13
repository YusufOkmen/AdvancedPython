import smtplib
from email.mime.text import MIMEText

port = 587 
smtpServer = "smtp-relay.brevo.com"
login = "8a47b6001@smtp-brevo.com"
password = "PIRU8FG04VvWjEDm"

senderEmail = "yusufokkmen@gmail.com"
recieverEmail = "yusufkmen@hotmail.com"

text = """
    Hello, this mail sended by my Python programme.
"""

message = MIMEText(text, "plain")
message["Subject"] = "Hello"
message["From"] = senderEmail
message["To"] = recieverEmail

with smtplib.SMTP(smtpServer, port) as  server:
    server.starttls()
    server.login(login, password)
    server.sendmail(senderEmail, recieverEmail, message.as_string())

print("E-mail sended...")

