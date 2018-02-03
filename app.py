"""Flask Email notification."""
from flask import Flask
from mailjet_rest import Client
from settings import PUBLIC_KEY, SECRET_KEY
from api import api_bp
APP = Flask(__name__)
APP.register_blueprint(api_bp)
mailjet = Client(auth=(PUBLIC_KEY, SECRET_KEY), version='v3.1')
@APP.route('/')
def hello():
    """Simple Hello world."""
    return 'Hello World!'

@APP.route('/send', methods=['POST'])
def send():
    """send."""
    data = {
        'Messages': [{
            'From': {
                'Email': 'guitartsword@gmail.com',
                'Name': 'Mailjet Pilot'
            },
            'To': [{
                'Email': '97ivallei97@gmail.com',
                'Name': 'passenger 1'
            }],
            'Subject': 'Your email flight plan!',
            'TextPart': 'Dear passenger 1, welcome to Mailjet! May the delivery force be with you!',
            'HTMLPart': '<h3>Dear passenger 1, welcome to Mailjet!</h3><br />May the delivery force be with you!'
        }]
    }
    result = mailjet.send.create(data=data)
    return str(result.json()), result.status_code
