from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    public_id: UUID

    class Config:
        from_attributes = True
