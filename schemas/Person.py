"""Person Schema."""
from marshmallow import Schema, fields

class PersonSchema(Schema):
    """Person Schema."""
    email = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String()