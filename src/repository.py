from connection import ConexionDbGuardias
from pydantic import BaseModel
from entity import *


class GuardiaDbReptry(BaseModel):
    
    def obtenerGuardia(self, rut: int):
        
        conexion = ConexionDbGuardias()
        cnx = conexion.conectarDbGuardias()
        
        lstResultado = []
        
        cursor = cnx.cursor()
        
        cursor.execute("SELECT * FROM gestionseguridad.guardia WHERE rut = " + str(rut))
        row = cursor.fetchall()

        # Ordenar resultado
        for j in row:
            lstResultado.append(j)
        lstResultado= list(lstResultado[0])           
        
        cnx.close()
        
        #Mapear resultados
        
        objGuardia = Guardia(nombre=lstResultado[1],
                             apellidoPaterno=lstResultado[2],
                             apellidoMaterno=lstResultado[3],
                             rut=lstResultado[4],
                             DV=lstResultado[5],
                             domicilio=lstResultado[6],
                             comuna=lstResultado[7],
                             fechaInicioContratacion=lstResultado[8],
                             fechaFinContratacion=lstResultado[9],
                             fechaInicioOs10=lstResultado[10],
                             fechaFinOs10=lstResultado[11])
        
        objGuardia.rut
        
        return objGuardia
    
    def agregarGuardia(self, guardia : Guardia):
        
        conexion = ConexionDbGuardias()
        cnx = conexion.conectarDbGuardias()
        
        cursor = cnx.cursor()

        cursor.execute("INSERT INTO gestionseguridad.guardia (nombre, apellidoPaterno, apellidoMaterno, rut, DV, domicilio, comuna, fechaInicioContratacion, fechaFinContratacion, fechaInicioOs10, fechaFinOs10) VALUES " 
                    + '(\'' + guardia.nombre + '\','
                    + '\'' + guardia.apellidoPaterno + '\','
                    + '\'' + guardia.apellidoMaterno + '\','
                    + '\'' + str(guardia.rut) + '\','
                    + '\'' + guardia.DV + '\','
                    + '\'' + guardia.domicilio + '\','
                    + '\'' + guardia.comuna + '\','
                    + '\'' + str(guardia.fechaInicioContratacion) + '\','
                    + '\'' + str(guardia.fechaFinContratacion) + '\','
                    + '\'' + str(guardia.fechaInicioOs10) + '\','
                    + '\'' + str(guardia.fechaFinOs10) + '\')'
                    )
        cnx.close()
        
        