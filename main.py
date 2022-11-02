from uuid import uuid1

from fastapi import FastAPI, Form, status
from pydantic import EmailStr

from functions import register_user, get_id

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
    user_id = get_id(email)
    print(user_id)
    if not(user_id):
        user_id = uuid1()
        register_user(user_id, email)
    
    return user_id


 