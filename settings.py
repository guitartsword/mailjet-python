"""Centralization of Environ variables"""

import os
import smtplib
from mailjet_rest import Client
from tools import Mail
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')
SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = os.environ.get('SMTP_PORT')

mailjet = Client(auth=(PUBLIC_KEY, SECRET_KEY), version='v3.1')
smtp_mail = Mail(PUBLIC_KEY, SECRET_KEY, SMTP_SERVER, SMTP_PORT)