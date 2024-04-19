from pydantic import BaseModel, EmailStr, Field, List, UUID4

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(BaseModel):
    name: str = Field(..., max_length=200)
    email: EmailStr
    password: str
    is_evaluator: bool
    is_sponsor: bool
    org_id: str
    bio: str = ""

class UserDisplay(BaseModel):
    id: UUID4
    name: str
    email: EmailStr
    is_evaluator: bool
    is_sponsor: bool
    org_id: str
    bio: str = ""

class UserUpdate(BaseModel):
    name: str = None
    email: EmailStr = None
