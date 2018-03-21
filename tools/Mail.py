import smtplib
from schemas import MailSchema
class Mail():
    def __init__(self, email, password, server, port):
        self.email = email
        self.password = password
        self.server = server
        self.port = port

    def __enter__(self):
        self.open()

    def __exit__(self):
        self.close()

    def open(self):
        self.session = smtplib.SMTP(self.server, self.port)
        self.session.ehlo()
        self.session.starttls()
        self.session.login(self.email, self.password)
    def close(self):
        self.session.quit()
    def sendmail(self, mail_schema):
        msg = '\r\n'.join([
          'From: %s' % mail_schema.from_person.email,
          'To: %s' % mail_schema.to_person.email,
          'Subject: %s' % mail_schema.subject,
          '',
          mail_schema.html or mail_schema.text
        ])
        self.session.sendmail(mail_schema.from_person.email, mail_schema.to_person.email, msg)


msg = "\r\n".join([
  "From: guitartsword@gmail.com",
  "To: 97ivallei97@gmail.com",
  "Subject: Just a message",
  "",
  "Hello guitart, this is a test message, please check if you received it"
  ])
mailing = smtplib.SMTP('smtp.gmail.com:587')
mailing.ehlo()
mailing.starttls()
mailing.login('guitartsword@gmail.com', 'diez10nueve9')
mailing.sendmail('guitartsword@gmail.com', '97ivallei97@gmail.com', msg)
mailing.quit()
print('mail sent')