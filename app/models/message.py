from mongoengine import Document, StringField, DateTimeField, ReferenceField, UUIDField
from .user import User
from .evaluation import Evaluation
import uuid

class EvaluationRequest(Document):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    linked_evaluation = ReferenceField(Evaluation, required=True)
    sender = ReferenceField(User, required=True)
    sent_at = DateTimeField(required=True)
    read_at = DateTimeField()