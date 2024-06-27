from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, todo
from database import engine, Base
from models import user, todo as todo_model

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(todo.router)
