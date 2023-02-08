# FastAPI 
from fastapi import FastAPI

# Create app instance
app = FastAPI()

# Routes (most of variables and strings will be in spanish due to region use (Colombia))

## Root
@app.get(
    path='/'
)
def root():
    return {'Mensaje': '¡Hola!'}