from mongoengine import Document, StringField, ListField, EmailField, UUIDField, BooleanField, DateTimeField
import uuid
import datetime

class User(Document):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = StringField(required=True, max_length=200)
    email = EmailField(required=True, unique=True)
    is_evaluator = BooleanField(required=True)
    is_sponsor = BooleanField(required=True)
    is_admin = BooleanField(required=True, default=False)
    org_id = StringField(required=True)
    specializations = ListField(StringField(max_length=100))
    created_at = DateTimeField(required=True, default=datetime.datetime.now)
    bio = StringField()
