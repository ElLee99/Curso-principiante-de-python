#Capitulo 40
#Johan Manuel García Zúñiga 19310416 6E1

class Usuarios:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self. edad = edad
        
    def muestra_datos(self):
        print("El nombre de usuario es: " + self.nombre, self.edad)


usuario1 = Usuarios("Enrique", 28)
print (usuario1.nombre, usuario1.edad)
del usuario1.edad
del usuario1
#print (usuario1.nombre, usuario1.edad)

