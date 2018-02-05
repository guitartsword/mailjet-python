"""Mail Engine."""
import logging
from schemas import MailSchema
from tools import valid_args
from flask_restful import Resource
from settings import mailjet

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
    @valid_args(MailSchema)
    def get(self,**kwargs):
        data, errors = kwargs.get('args')
        if errors:
            return errors, 400
        return data
