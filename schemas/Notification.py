"""Notification Schema."""
from marshmallow import Schema, fields
from . import PersonSchema

class NotificationSchema(Schema):
    """Notification Schema."""
    id = fields.Integer(required=True)
    person = fields.Nested(PersonSchema, required=True)
    subject = fields.String()
    html = fields.String()
    text = fields.String()
