# FastAPI 
from fastapi import FastAPI

# Models an schemas
from .schemas import UserSchema

# Database
from .database.database import Base, engine
from .database.crud import get_user_by_id

# SQLAlchemy
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

# Create app instance
app = FastAPI()

# Routes (most of variables and strings will be in spanish due to region use (Colombia))

## Root
@app.get(
    path='/'
)
def root():
    return {'Mensaje': '¡Hola!'}

@app.get(
    path="/user/{user_id}"
)
def get_user(user_id: int):
    result = get_user_by_id(Session, user_id)
    print(result)
    return '1'