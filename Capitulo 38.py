#Capitulo 38
#Johan Manuel García Zúñiga 19310416 6E1

class Usuarios():
    
    def __init__(self, nombre, pin):
        self.nombre = nombre
        self.pin = pin
        
    def saludo (self):
        print("Saludos " + self.nombre + " Iniciaste sesión correctamente")
        
    def despedida (self):
        print(self.nombre + ", cerraste la sesión")
        
usuario1 = Usuarios("Tomi", "4321")
usuario2 = Usuarios("Julia", "3692")

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()
