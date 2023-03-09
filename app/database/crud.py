# Import models and schemas
from app.models.models import User, Country
from app.schemas import UserSchema

# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import select

# passwords
import bcrypt

# Read 

def get_user_by_id(
        db: Session,
        user_id: int
):
    #return db.execute(statement=select(User).where(User.id == user_id))
    #return select(User).where(User.id == user_id)
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(
        db: Session,
        user_email: str
):
    pass

def get_users(db: Session):
    pass

def find_country_by_name(
        db: Session, 
        name: str
):
    return db.query(Country).filter(Country.name == name).first()

# Create

def create_user(
        db: Session,
        user: UserSchema
):

    country = find_country_by_name(
        db=db,
        name=user.country
    ).__dict__

    new_user = User(
        nickname=user.nickname,
        password=bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()),
        name=user.name,
        surname=user.surname,
        email=user.email,
        phone=user.phone,
        country_id = country['id']
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user