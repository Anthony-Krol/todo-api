from fastapi import FastAPI
from routers import auth, todo
from database import engine, Base
from models import user, todo as todo_model

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todo.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
