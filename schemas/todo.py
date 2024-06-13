from pydantic import BaseModel

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
    owner_id: int

    class Config:
        orm_mode = True
