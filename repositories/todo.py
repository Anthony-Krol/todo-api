from sqlalchemy.orm import Session
from models import todo as models
from schemas import todo as schemas

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()

def create_todo_item(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_item = models.TodoItem(**todo.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
