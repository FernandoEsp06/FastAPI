from fastapi import APIRouter, Depends
from app.schemas import User,UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

router = APIRouter(
    prefix='/user',
    tags=['users']
)

usuarios = []

@router.get('/ruta1')
def ruta1():
    return {'mensaje':'Bienvenido a tu primera App'}

@router.get('/')
def obtener_usuarios(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return usuarios

@router.post('/')
def crear_usuario(user:User,db:Session = Depends(get_db)):
    usuario = user.dict()
    nuevo_usuario = models.User(
        username=usuario['username'],
        password=usuario['password'],
        nombre=usuario['nombre'],
        apellido=usuario['apellido'],
        direccion=usuario['direccion'],
        telefono=usuario['telefono'],
        correo=usuario['correo']
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    # usuarios.append(usuario)
    return {'respuesta':'Usuario creado correctamente'}

@router.post('/{user_id}')
def obtener_usuario(user_id:int):
    for user in usuarios:
        if user['id'] == user_id:
            return {'usuario':user}
    return {'respuesta':'Usuario no encontrado!'}

@router.post('/obtener_usuario')
def obtener_usuario2(user_id:UserId):
    for user in usuarios:
        if user['id'] == user_id.id:
            return {'usuario':user}
    return {'respuesta':'Usuario no encontrado!'}

@router.delete('/{user_id}')
def eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios):
        if user['id'] == user_id:
            usuarios.pop(index)
            return {'respuesta':'Usuario eliminado correctamente'}
    return {'respuesta':'Usuario no encontrado!'}

@router.put('/{user_id}')
def actualizar_usuario(user_id:int, updateUser:User):
    for index,user in enumerate(usuarios):
        if user['id']==user_id:
            usuarios[index]['id'] = updateUser.dict()['id']
            usuarios[index]['nombre'] = updateUser.dict()['nombre'] #encuentra el title del usuario en ese indice
            usuarios[index]['apellido'] = updateUser.dict()['apellido']
            usuarios[index]['direccion'] = updateUser.dict()['direccion']
            usuarios[index]['telefono'] = updateUser.dict()['telefono']
            return {'respuesta':'Usuario actualizado correctamente'}
    return {'respuesta':'Usuario no encontrado!'}
