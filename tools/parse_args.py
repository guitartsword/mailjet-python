from flask import request
from werkzeug.exceptions import BadRequest
from functools import wraps

def valid_args(Schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            schema = Schema()
            json = request.get_json(force=True, silent=True)
            marshal_result = dict()

            if json:
                marshal_result = schema.load(json)

            req_args = request.args.to_dict()
            if not marshal_result:
                marshal_result = schema.load(req_args)

            if not marshal_result:
                raise BadRequest('Unable to parse args or payload')
            kwargs['args'] = marshal_result
            return func(*args, **kwargs)
        return wrapper
    return decorator
