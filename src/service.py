from connection import ConexionDbGuardias
from pydantic import BaseModel
import repository
from entity import *

class GuardiaService(BaseModel):
    
    def obtenerGuardia(self, rut: int):
        try:
            objGuardiaReptry = repository.GuardiaDbReptry()
            objGuardia = objGuardiaReptry.obtenerGuardia(rut)
            
            return objGuardia
        
        except:
            
            return "Codigo 002: Guardia no encontrado"
        
    def agregarGuardia(self, guardia : Guardia):
        try:
            objGuardiaReptry = repository.GuardiaDbReptry()
            objGuardiaReptry.agregarGuardia(guardia)
            
            print(guardia.__dict__)
            
            return "Guardia Agregado Correctamente."
        
        except:
            
            return "Codigo 002: Error al agregar guardia"