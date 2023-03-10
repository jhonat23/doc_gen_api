from pydantic import BaseModel, Field, EmailStr

# User models

## UserBase and UserLogin is for Login
class UserBase(BaseModel):
    nickname: str = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=3,
        description="User's hashed password"
    )

## User for database
class UserSchema(UserLogin):
    id: int = Field(...)
    name: str = Field(
        ...,
        min_length=2,
        max_length=45,
        description="User's real name"
    )
    surname: str = Field(
        ...,
        min_length=3,
        max_length=45,
        description="User's real surname"
    )
    email: EmailStr = Field(
        ...,
        description="User's email"
    )
    phone: str = Field(
        ...,
        max_length=20,
        description="User's phone"
    )
    country: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="User's country"
    )

    class Config:
        orm_mode = True

class Country(BaseModel):
    id: int = Field(...),
    name: str = Field(
        ...,
        max_length=20,
        description="Country's original name"
    )