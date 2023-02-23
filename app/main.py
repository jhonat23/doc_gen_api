# FastAPI 
from fastapi import FastAPI, Query, Depends

# Models an schemas
from .schemas import UserSchema, UserBase

# Database
from .database.database import Base, engine, LocalSession
from .database.crud import get_user_by_id

# SQLAlchemy
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

# Working with different sessions per SQL request
def get_db_session():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

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
    path="/user/{user_id}",
    response_model=UserSchema
)
def get_user(
    user_id: int = Query(...),
    db: Session = Depends(get_db_session)
):
    result = get_user_by_id(db, user_id)
    print(result)
    return result