from pydantic import BaseModel
from  typing import List, Optional
from datetime import datetime


class User(BaseModel):
    username : str
    password : str
    nombre : str
    apellido :str
    direccion : Optional[str]
    telefono : str
    correo : str
    creacion : datetime=datetime.now()
