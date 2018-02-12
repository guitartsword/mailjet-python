"""Centralization of Environ variables"""

import os
from mailjet_rest import Client
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')

mailjet = Client(auth=(PUBLIC_KEY, SECRET_KEY), version='v3.1')
