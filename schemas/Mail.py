"""Mail Schema."""
from marshmallow import Schema, fields
from . import PersonSchema

class MailSchema(Schema):
    """Mail Schema."""    
    from_person = fields.Nested(
        PersonSchema, required=True, dump_to='From')
    to_person = fields.List(
        fields.Nested(PersonSchema, required=True),
        dump_to='To')
    subject = fields.String(required=True, dump_to='Subject')
    text = fields.String(required=True, dump_to='TextPart', default='no text')
    html = fields.String(required=True, dump_to='HTMLPart', default='no html')