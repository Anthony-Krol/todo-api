from sqlalchemy.orm import Session
from models import user as models
from schemas import user as schemas
from core.security import get_password_hash
import uuid

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        public_id=uuid.uuid4()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
