"""Mail Engine."""
import logging

from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import TEXT

from schemas import MailSchema, NotificationSchema, PersonSchema
from settings import mailjet
from tools import valid_args

db = SQLAlchemy()


class Mail(Resource):
    @valid_args(MailSchema)
    def post(self, **kwargs):
        data, errors = kwargs.get('args')
        if errors:
            return errors, 400
        schema = MailSchema()
        parsed_data = {'Messages':[schema.dump(data).data]}
        result = mailjet.send.create(data=parsed_data)
        logging.info('Mail sent')
        return result.json(), result.status_code

class Notify(Resource):
    def post(self):
        notification = NotificationConfiguration.query.get_or_404(0)
        notification.to_person = {
            'first_name': notification.first_name,
            'last_name': notification.last_name,
            'email': notification.email
        }
        notification.from_person = {
            'first_name': 'No',
            'last_name': 'Reply',
            'email': 'guitartsword@gmail.com'
        }
        if not notification.text:
            notification.text = 'no text'
        mail_schema = MailSchema()
        parsed_data = {'Messages': [mail_schema.dump(notification).data]}
        result = mailjet.send.create(data=parsed_data)
        logging.warn('Mail sent to %s', notification.email)
        logging.warn('Mail sent to %s', parsed_data)
        return result.json(), result.status_code

    @valid_args(NotificationSchema)
    def put(self, **kwargs):
        data, errors = kwargs.get('args')
        if errors:
            return errors, 400
        notification = NotificationConfiguration(**data)
        db.session.add(notification)
        db.session.commit()
        return data

    def get(self,):
        notification = NotificationConfiguration.query.get_or_404(0)
        notification_schema = NotificationSchema()
        data = notification_schema.dump(notification)
        return data
        
    @valid_args(NotificationSchema)
    def patch(self, **kwargs):
        data, errors = kwargs.get('args')
        if errors:
            return errors, 400
        notification = NotificationConfiguration.query.get(data['id'])
        if not notification:
            return {
                'message':'configuration not found',
                'id':data.get('id'),
                'status':404
            }, 404
        notification.update(**data)
        db.session.commit()
        notification_schema = NotificationSchema()
        jsonData = notification_schema.dump(notification)
        return jsonData

class NotificationConfiguration(db.Model):
    id = db.Column('notification_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    subject = db.Column(db.String(100))
    html = db.Column(TEXT)
    text = db.Column(TEXT)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
