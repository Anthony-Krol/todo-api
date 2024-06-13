from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas import todo as schemas
from schemas.user import User as UserSchema
from services import todo as todo_service
from repositories import user as user_repo
from database import get_db
from core.security import decode_access_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = user_repo.get_user_by_username(db, username=payload["sub"])
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user

@router.get("/todos", response_model=List[schemas.TodoItem])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return todo_service.get_todos(db, skip, limit)

@router.post("/todos", response_model=schemas.TodoItem)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return todo_service.create_todo_item(db, todo, current_user.id)
