from fastapi import APIRouter, Depends
from app.models.user_model import User
from icecream import ic
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import model
from datetime import datetime

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/")
def obtener_usuarios(db:Session = Depends(get_db)):
    data = db.query(model.User).all()
    return data

@router.post("/")
def  crear_usuario(user : User, db:Session = Depends(get_db)):
    usuario = user.dict()
    nuevo_usuario = model.User(
        username = usuario["username"],
        password = usuario["password"],
        nombre = usuario["nombre"],
        apellido = usuario["apellido"],
        direccion = usuario["direccion"],
        telefono = usuario["telefono"],
        correo = usuario["correo"],
        creacion = datetime.now()
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"mensaje" : "Usuario registrado satisfactoriamente"}

@router.get("/{id}")
def  obtener_un_usuario(id:int, db:Session = Depends(get_db)):
    usuario = db.query(model.User).filter(model.User.id==id).first()
    if not usuario:
        return {"mensaje":"Usuario no encontrado"}
    return usuario

@router.put("/user/{id}")
def actualizar_usuario(id:int, usuario_actualizado : User, db:Session = Depends(get_db)):
    cambio = usuario_actualizado.dict()
    usuario = db.query(model.User).filter(model.User.id==id).first()
    ic(usuario)
    if usuario:
        usuario.username = cambio["username"]
        usuario.password = cambio["password"]
        usuario.nombre = cambio["nombre"]
        usuario.apellido = cambio["apellido"]
        usuario.direccion = cambio["direccion"]
        usuario.telefono = cambio["telefono"]
        usuario.correo = cambio["correo"]
        db.commit()
        return {"mensaje" : "Usuario actualizado satisfactoriamente"}
    return {"mensaje":"Usuario no encontrado"}
          

@router.delete("/")
def eliminar_usuario(id:int, db:Session = Depends(get_db)): 
    usuario = db.query(model.User).filter(model.User.id==id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return{"mensaje":"El usuario fue eliminado correctamente"}
    return {"mensaje":"El usuario no existe"}    
