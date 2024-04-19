from mongoengine import Document, StringField, ListField, DateTimeField, ReferenceField, UUIDField, BooleanField
import uuid

from .user import User

class Evaluation(Document):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    title = StringField(required=True, max_length=200)
    description = StringField(required=True)
    is_public = BooleanField(required=True)
    status = StringField(required=True, choices=['Draft', 'Open', 'In Progress', 'Completed'])
    sponsor = ReferenceField(User, required=True)  # Changed from sponsor_id to sponsor
    deadline = DateTimeField()