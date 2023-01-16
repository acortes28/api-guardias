import connection
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Test:

    def probarConn():
        
        driver = config['DATABASE']['driver']
        host = config['DATABASE']['host']
        usuario = config['DATABASE']['user']
        password = config['DATABASE']['pass']
        
        print(driver)
        print(host)
        print(usuario)
        print(password)
        
        connexion = connection.ConexionDbGuardias(driver, host, usuario, password)
        connexion.conectarDbGuardias()
        

Test.probarConn()