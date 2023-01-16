from pydantic import BaseModel
import datetime
    
class Guardia(BaseModel):
    nombre : str
    apellidoPaterno : str
    apellidoMaterno : str
    rut : int
    DV : str
    domicilio : str
    comuna : str
    fechaInicioContratacion : datetime.datetime
    fechaFinContratacion : datetime.datetime
    fechaInicioOs10 : datetime.datetime
    fechaFinOs10 : datetime.datetime
        
    
class Instalacion(BaseModel):
    nombre : str
    direccion : str
    comuna : str
    contacto : str
    horaApertura : datetime.datetime
    horaCierre : datetime.datetime
