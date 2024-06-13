from sqlalchemy.orm import Session
from repositories import todo as todo_repo
from schemas import todo as schemas

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return todo_repo.get_todos(db, skip, limit)

def create_todo_item(db: Session, todo: schemas.TodoCreate, user_id: int):
    return todo_repo.create_todo_item(db, todo, user_id)
