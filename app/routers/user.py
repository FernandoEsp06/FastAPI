from fastapi import APIRouter, Depends
from app.schemas import User,UserId, showUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List
router = APIRouter(
    prefix='/user',
    tags=['users']
)

usuarios = []

@router.get('/',response_model=List[showUser])
def obtener_usuarios(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return data

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

@router.get('/{user_id}',response_model=showUser)
def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        return {'respuesta':'Usuario no encontrado!'}
    return usuario

@router.post('/obtener_usuario')
def obtener_usuario2(user_id:UserId):
    for user in usuarios:
        if user['id'] == user_id.id:
            return {'usuario':user}
    return {'respuesta':'Usuario no encontrado!'}

@router.delete('/{user_id}')
def eliminar_usuario(user_id:int,db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        return {'respuesta':'Usuario no encontrado!'}
    usuario.delete(synchronize_session=False)
    db.commit()
    return {'respuesta':'Usuario eliminado correctamente'}
    # for index,user in enumerate(usuarios):
    #     if user['id'] == user_id:
    #         usuarios.pop(index)
    #         return {'respuesta':'Usuario eliminado correctamente'}
    # return {'respuesta':'Usuario no encontrado!'}

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
