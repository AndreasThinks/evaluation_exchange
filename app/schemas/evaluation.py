from pydantic import BaseModel, UUID4, Field
from datetime import datetime
from typing import Optional

class EvaluationBase(BaseModel):
    title: str = Field(..., max_length=200)
    description: str
    is_public: bool
    status: str

class EvaluationCreate(EvaluationBase):
    sponsor_id: UUID4  # Assuming this comes from input as a UUID

class EvaluationDisplay(EvaluationBase):
    id: UUID4
    sponsor_id: UUID4
    deadline: Optional[datetime]

class EvaluationUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str]
    is_public: Optional[bool]
    status: Optional[str]
    deadline: Optional[datetime]
