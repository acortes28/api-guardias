import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from entity import *
import service

app = FastAPI()

class GuardiaController(BaseModel):

    @app.get('/obtenerGuardia/{rut}')
    async def obtenerGuardiaPorRut(rut: int):
        
        objObtenerGuardiaSrv = service.GuardiaService()
        
        return objObtenerGuardiaSrv.obtenerGuardia(rut)


    @app.post('/agregarGuardia')
    async def agregarGuardia(guardia : Guardia):
        
        agregarGuardiaSrv = service.GuardiaService()
        
        return agregarGuardiaSrv.agregarGuardia(guardia)