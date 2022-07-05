from fastapi import APIRouter, Depends
from app.schemas import User, showUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.get('/',response_model=List[showUser])
def obtener_usuarios(db:Session = Depends(get_db)):
    data = user.obtener_usuarios(db)
    return data

@router.post('/')
def crear_usuario(usuario:User,db:Session = Depends(get_db)):
    user.crear_usuario(usuario,db)
    # usuarios.append(usuario)
    return {'respuesta':'Usuario creado correctamente'}

@router.get('/{user_id}',response_model=showUser)
def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
    usuario = user.obtener_usuario(user_id,db)
    return usuario

@router.delete('/{user_id}')
def eliminar_usuario(user_id:int,db:Session = Depends(get_db)):
    res = user.eliminar_usuario(user_id,db)

    return res

@router.patch('/{user_id}')
def actualizar_usuario(user_id:int, updateUser:UpdateUser, db:Session = Depends(get_db)):
    res = user.actualizar_usuario(user_id,updateUser,db)
    return res