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
    public_id: UUID

    class Config:
        from_attributes = True
