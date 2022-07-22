import smtplib
from email.mime.text import MIMEText

msg = MIMEText("It's working..")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # identifies ourselves to smtp gmail client
    smtp.starttls() # secure our mail with tls encryption.
    smtp.ehlo() # re-identify ourselves as an encrypted connection.
    smtp.login("python9948@gmail.com", "Lakshmi@123")
    smtp.sendmail("python9948@gmail.com", "mudhireddynandu@gmail.com", msg.as_string())
    print("message sent successfully.")