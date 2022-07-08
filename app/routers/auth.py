from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas import Login
from app.repository import auth

router = APIRouter(
    prefix='/login',
    tags=['Login']
)

@router.post('/',status_code=status.HTTP_200_OK)
def login(usuario:Login,db:Session = Depends(get_db)):
    auth.authUser(usuario,db)
    return {'respuesta':'login aceptado!'}