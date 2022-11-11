from uuid import uuid1

from fastapi import FastAPI, Form, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from pydantic import EmailStr

from functions import *


app = FastAPI()


origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
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
    if not(user_id):
        user_id = uuid1()
        register_user(user_id, email)
    
    return user_id


@app.post(
    path="/create_note",
    status_code=status.HTTP_201_CREATED,
    summary="Create a Note in the Database",
    tags=['Create']
)
async def add_note(user_id: str = Form(), name: str = Form()):
    note_id = uuid1()
    print(note_id)
    register_note(note_id, user_id, name)
    return note_id


@app.get(
    path='/get_containers/{user_id}',
    status_code=status.HTTP_202_ACCEPTED,
    summary="Get all the containers of the user",
    tags=['Get']
)
async def get_containers(user_id: str):
    # Returns an Array of arrays -> [ [container_id, name] ]
    containers = []

    # For the notes
    for note in get_notes(user_id):
        containers.append(note)

    return jsonable_encoder(containers)


@app.post(
    path='/modify_note',
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Change the content of the note",
    tags=['Modify']
)
async def change_note(note_id: str = Form(), new_value: str = Form()):
    modify_note(note_id, new_value)
     
    return '200'



 