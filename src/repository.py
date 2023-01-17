from connection import ConexionDbGuardias
from pydantic import BaseModel
from entity import *
from datetime import datetime


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

        query = 'INSERT INTO gestionseguridad.guardia (nombre, apellidoPaterno, apellidoMaterno, rut, DV, domicilio, comuna, fechaInicioContratacion, fechaFinContratacion, fechaInicioOs10, fechaFinOs10) VALUES (?,?,?,?,?,?,?,?,?,?,?)'
        
        #print(guardia.__dict__)
        print(str(guardia.fechaInicioContratacion))
        print("Registro insertado exitosamente")
        try:
            cursor.execute(query,(str(guardia.nombre),
                                str(guardia.apellidoPaterno),
                                str(guardia.apellidoMaterno),
                                str(guardia.rut),
                                str(guardia.DV),
                                str(guardia.domicilio),
                                str(guardia.comuna),
                                str(guardia.fechaInicioContratacion),
                                str(guardia.fechaFinContratacion),
                                str(guardia.fechaInicioOs10),
                                str(guardia.fechaFinOs10)
                                )
            )
            cnx.commit()
            
            cnx.close()
        except:
            print("Error al intentar insertar a la BD")
            cnx.close()
        

# gsdb = GuardiaDbReptry()

# ggss = Guardia(nombre='Rodrigo',
#                apellidoPaterno='Munoz',
#                apellidoMaterno='California',
#                rut=28827384,
#                DV='K',
#                domicilio='estela 1219',
#                comuna='San Miguel',
#                fechaInicioContratacion='2022-01-30 15:00:00',
#                fechaFinContratacion='2022-05-29 16:00:00',
#                fechaInicioOs10='2022-01-01 17:00:00',
#                fechaFinOs10='2022-01-01 18:00:00'
#                ) 

# #print(ggss.__dict__)

# gsdb.agregarGuardia(ggss)