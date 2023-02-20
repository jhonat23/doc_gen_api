from database.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

# Creating the user model
class User(Base):
    __tablename__ = 'users'

    ## Attributes
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(45))
    surname: str = Column(String(45))
    nickname: str = Column(String(20), unique=True)
    email: str = Column(String(50), unique=True, index=True)
    phone: int = Column(Integer, unique=True)
    country: str = Column(String(20))

# Creating the docs model
class Docs(Base):
    __tablename__ = 'docs'

# Creating the user's docs model
class UserDocs(Base):
    __tablename__ = 'Userdocs'