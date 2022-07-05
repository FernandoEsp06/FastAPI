import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
print(os.getenv('POSTGRES_DB'))

#Configuracion encargada de la conexion con la base de datos
class Settings:
    PROJECT_NAME:str = 'PROYECTO-FAST-API'
    PROJECT_VERSION:str = '1.0'
    POSTGRES_DB:str = os.getenv('POSTGRES_DB')
    POSTGRES_USER:str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSGRES_SERVER:str = os.getenv('POSGRES_SERVER')
    POSTGRES_PORT:str = os.getenv('POSTGRES_PORT')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

settings = Settings()