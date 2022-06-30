from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    creacion:datetime = datetime.now()

class UserId(BaseModel):
    id:int

class showUser(BaseModel):
    username:str
    nombre:str
    correo:str
    class Config():
        orm_mode = True