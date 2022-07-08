# Dos formas de ejecutar la app
    1. uvicorn main:app
    2. Agregar las lineas de codigo
        if __name__ == "__main__":
            uvicorn.run("main:app",port=8000)
        y luego se corre python main.py

# hacer migraciones
    alembic revision --autogenerate -m "Crear modelos"
    alembic upgrade heads #Genera las tablas