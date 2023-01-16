import pyodbc
import configparser



class ConexionDbGuardias:
    
    driver : str
    host  : str
    user : str
    password : str
    
    def __init__(self):
        self.__configuracion__()
        print('Conexion construida')
    
    
    def __configuracion__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.driver = config['DATABASE']['driver']
        self.host = config['DATABASE']['host']
        self.user = config['DATABASE']['user']
        self.password = config['DATABASE']['pass']
                
    
    def conectarDbGuardias(self):
        
        global conn
        
        try:
            conn = pyodbc.connect('Driver={0};'
                                  'Server={1};'
                                  'User={2};'
                                  'Password={3};'.format(self.driver,
                                                         self.host,
                                                         self.user,
                                                         self.password))
            
            print("Se realizo correctamente la conexión a la base de datos")
            
            return conn

        except:
            
            print("Error al intentar conectar a la base de datos")
            