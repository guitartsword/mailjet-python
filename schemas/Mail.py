"""Mail Schema."""
from marshmallow import Schema, fields
from . import PersonSchema

class MailSchema(Schema):
    """Mail Schema."""    
    from_person = fields.Nested(PersonSchema, required=True)
    to_person = fields.Nested(PersonSchema, required=True)
    subject = fields.String(required=True)
    text = fields.String(required=True)
    html = fields.String(required=True)