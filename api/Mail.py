from flask_restful import Resource, request
from schemas import MailSchema
from api import api
from tools import valid_args

class Mail(Resource):
    @valid_args(MailSchema)
    def post(self, **kwargs):
        data, errors = kwargs.get('args')
        if errors:
            return errors, 400
        return data
    @valid_args(MailSchema)
    def get(self,**kwargs):
        data, errors = kwargs.get('args')
        if errors:
            return errors, 400
        return data

api.add_resource(Mail, '/mail')
