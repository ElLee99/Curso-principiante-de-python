#Capitulo 42
#Johan Manuel García Zúñiga 19310416 6E1

class Usuarios:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print("El nombre de usuario es: " + self.nombre + " y tiene ", self.edad,  "años")


usuario1 = Usuarios("Enrique", 28)
usuario1.muestra_datos()


class Usuarios_premium(Usuarios):
    def __init__(self, nombre, edad, instagram):
        Usuarios.__init__(self, nombre, edad)
        self.instagram =instagram
        
       
    def muestra_datos_premium(self):
        print("El nombre de usuario es: " + self.nombre + " y tiene ", self.edad, "años. Su Instagram es: " + self.instagram)

usuario2 = Usuarios_premium("Elvira", 23, "elvi23")
usuario2.muestra_datos_premium()