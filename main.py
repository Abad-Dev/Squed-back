from uuid import uuid1

from fastapi import FastAPI, Form, status
from pydantic import EmailStr

from functions import register_user, registered

app = FastAPI()

@app.get('/inicio')
async def ruta_de_prueba():
    return 'Hola desde FastAPI.'

@app.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=['Users']
)
async def signup(email: EmailStr = Form() ):
    if not(registered(email)):
        register_user(uuid1(), email)
        return '201'
    return '200'
