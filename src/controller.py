from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from entity import *
import service

app = FastAPI(title='api-guardia',
              description='api para poder gestionar servicios relacionados con los guardias',
              version='0.0.1')



@app.get('/')
def prueba():
    return 'Funciona Correctamente'

class GuardiaController(BaseModel):

    @app.get('/obtenerGuardia/{rut}')
    async def obtenerGuardiaPorRut(rut: int):
        
        objObtenerGuardiaSrv = service.GuardiaService()
        
        return objObtenerGuardiaSrv.obtenerGuardia(rut)


    @app.post('/agregarGuardia')
    async def agregarGuardia(guardia : Guardia):
        
        agregarGuardiaSrv = service.GuardiaService()
        
        return agregarGuardiaSrv.agregarGuardia(guardia)