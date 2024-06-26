import pickle

from sqlalchemy.orm import Session
from models import todo as models
from schemas import todo as schemas
from fastapi import HTTPException


def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()


def create_todo_item(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_item = models.TodoItem(**todo.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_todo_item(db: Session, public_id: str, user_id: int):
    db_item = db.query(models.TodoItem).filter(models.TodoItem.public_id == public_id,
                                               models.TodoItem.owner_id == user_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return db_item
    raise HTTPException(status_code=404, detail="Todo item not found")


def toggle_todo_item_state(db: Session, public_id: str, user_id: int):
    db_item = db.query(models.TodoItem).filter(models.TodoItem.public_id == public_id,
                                               models.TodoItem.owner_id == user_id).first()
    if db_item:
        db_item.completed = not db_item.completed
        db.commit()
        db.refresh(db_item)
        return db_item
    raise HTTPException(status_code=404, detail="Todo item not found")
