from pydantic import BaseModel
from uuid import UUID

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoItem(TodoBase):
    id: int
    public_id: UUID
    owner_id: int

    class Config:
        from_attributes = True
