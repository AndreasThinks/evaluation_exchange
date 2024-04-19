from pydantic import BaseModel, UUID4
from datetime import datetime

class MessageBase(BaseModel):
    content: str
    sender_id: UUID4
    recipient_id: UUID4

class MessageCreate(MessageBase):
    pass

class MessageDisplay(MessageBase):
    id: UUID4
    created_at: datetime

class MessageUpdate(BaseModel):
    content: Optional[str]
