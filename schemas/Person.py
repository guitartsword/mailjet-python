"""Person Schema."""
from marshmallow import Schema, fields

class PersonSchema(Schema):
    """Person Schema."""
    email = fields.Email(required=True, dump_to='Email')
    first_name = fields.String(required=True, load_only=True)
    last_name = fields.String(default='', load_only=True)
    Name = fields.Method('format_name', dump_only=True)

    def format_name(self, person):
        last = person.get('last_name', '')
        return '{} {}'.format(person.get('first_name'), last).strip()
