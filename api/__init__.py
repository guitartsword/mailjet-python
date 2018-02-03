from flask import Blueprint
from flask_restful import Api
from modulefinder import importlib

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

importlib.import_module(f'{__name__}.Mail')