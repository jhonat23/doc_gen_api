from app.database.database import Base
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

# Creating the user model
class User(Base):
    __tablename__ = 'users'

    ## Attributes
    id: int = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        autoincrement=True, 
        nullable=False
    )
    name: str = Column(String(45))
    surname: str = Column(String(45))
    nickname: str = Column(
        String(20), 
        unique=True
    )
    email: str = Column(
        String(50), 
        unique=True, 
        index=True
    )
    phone: int = Column(
        Integer, 
        unique=True
    )
    password: str = Column(String(8))

    ## Foregin data
    country_id: int = Column(Integer, ForeignKey('country.id'))
    docs = relationship('UserDocs', backref='users')

# Creating the docs model
class UserDocs(Base):
    __tablename__ = 'userdocs'

    ## Atributtes
    id: int = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        autoincrement=True, 
        nullable=False
    )
    file: bytes = LargeBinary(LargeBinary)

    ## Foregin data
    user_id: int = Column(Integer, ForeignKey('users.id'))
    doctype_id: int = Column(Integer, ForeignKey('doctype.id'))

# # Creating the user's docs model
class DocType(Base):
    __tablename__ = 'doctype'

    ## Atributtes
    id: int = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        autoincrement=True, 
        nullable=False
    )
    name: str = Column(String(50))

# Creating the country model
class Country(Base):
    __tablename__ = 'country'

    ## Atributtes
    id: int = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        autoincrement=True, 
        nullable=False
    )
    name: str = Column(String(50))