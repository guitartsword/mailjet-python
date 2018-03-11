"""Notification Schema."""
from marshmallow import Schema, fields
from . import PersonSchema

class NotificationSchema(PersonSchema):
    """Notification Schema."""
    id = fields.Integer(required=True)
    first_name =fields.String()
    last_name =fields.String()
    email =fields.Email()
    subject = fields.String()
    html = fields.String()
    text = fields.String()
