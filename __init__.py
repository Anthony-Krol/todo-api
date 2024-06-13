from .database import Base, engine
from .models import user, todo

Base.metadata.create_all(bind=engine)
