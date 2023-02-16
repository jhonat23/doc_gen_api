# FastAPI 
from fastapi import FastAPI

# Models
from .schemas import User

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
    path="/user"
)
def get_user(user: User):
    return 