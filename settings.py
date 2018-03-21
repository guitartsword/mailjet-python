"""Centralization of Environ variables"""

import os
import smtplib
from mailjet_rest import Client
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')

mailjet = Client(auth=(PUBLIC_KEY, SECRET_KEY), version='v3.1')


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