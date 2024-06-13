from sqlalchemy.orm import Session
from repositories import user as user_repo
from schemas import user as schemas
from core.security import verify_password, create_access_token
from datetime import timedelta
from core.config import settings

def authenticate_user(db: Session, username: str, password: str):
    user = user_repo.get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_user_token(user: schemas.User):
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return access_token
