from sqlalchemy.orm import Session
from app.db import models
from app.schemas import UpdateUser
from fastapi import HTTPException,status
from app.hashing import Hash

def crear_usuario(usuario,db:Session):
    try: 
        usuario = usuario.dict()
        nuevo_usuario = models.User(
            username=usuario['username'],
            password= Hash.hash_password(usuario['password']),
            nombre=usuario['nombre'],
            apellido=usuario['apellido'],
            direccion=usuario['direccion'],
            telefono=usuario['telefono'],
            correo=usuario['correo']
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail= f'Error creando el usuario {e}' 
        )

def obtener_usuario(user_id,db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f'No existe el usuario con el id {user_id}' 
        )
    return usuario

def eliminar_usuario(user_id,db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f'No existe el usuario con el id {user_id}' 
        )
    usuario.delete(synchronize_session=False)
    db.commit()
    raise HTTPException(
            status_code = status.HTTP_200_OK,
            detail= f'Usuario {user_id} eliminado correctamente' 
        )

def obtener_usuarios(db:Session):
    data = db.query(models.User).all()
    return data

def actualizar_usuario(user_id,updateUser:UpdateUser, db:Session):
    usuario = db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f'No existe el usuario con el id {user_id}'
        )
    usuario.update(updateUser.dict(exclude_unset=True))
    db.commit()
    raise HTTPException(
            status_code = status.HTTP_200_OK,
            detail= f'Usuario {user_id} actualizado correctamente' 
        )