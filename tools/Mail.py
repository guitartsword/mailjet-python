import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from schemas import MailSchema
class Mail():
    def __init__(self, email, password, server, port):
        self.email = email
        self.password = password
        self.server = server
        self.port = port

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, tb):
        self.close()

    def open(self):
        self.session = smtplib.SMTP(self.server, self.port)
        self.session.ehlo()
        self.session.starttls()
        self.session.login(self.email, self.password)
    def close(self):
        self.session.quit()
    def send(self, mail_schema):
        logging.error("SCHEMA:%s",mail_schema)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = mail_schema.get('Subject')
        msg['From'] = mail_schema.get('From').get('Email')
        msg['To'] = mail_schema.get('To')[0].get('Email')
        text = MIMEText(mail_schema.get('TextPart'), 'plain')
        html = MIMEText(mail_schema.get('HTMLPart'), 'html')
        msg.attach(text)
        msg.attach(html)
        self.session.sendmail(msg['From'], msg['To'], msg.as_string())
        return {
            'status_code': 200
        }


# msg = "\r\n".join([
#   "From: guitartsword@gmail.com",
#   "To: 97ivallei97@gmail.com",
#   "Subject: Just a message",
#   "",
#   "Hello guitart, this is a test message, please check if you received it"
#   ])
# mailing = smtplib.SMTP('smtp.gmail.com:587')
# mailing.ehlo()
# mailing.starttls()
# mailing.login('guitartsword@gmail.com', 'diez10nueve9')
# mailing.sendmail('guitartsword@gmail.com', '97ivallei97@gmail.com', msg)
# mailing.quit()
# print('mail sent')