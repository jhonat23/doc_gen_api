# Import models and schemas
from app.models.models import User
from app.schemas import UserSchema

# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import select

# Read 

def get_user_by_id(
        db: Session,
        user_id: int
):
    return db.execute(statement=select(User).where(User.id == user_id))
    #return select(User).where(User.id == user_id)

def get_user_by_email(
        db: Session,
        user_email: str
):
    pass

def get_users(
        db: Session,
):
    pass
