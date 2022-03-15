#Capitulo 36
#Johan Manuel García Zúñiga 19310416 6E1


#Parte 1 de video
def colores (color1, color2, color3, color4):
    print ("Este es el color " + color1 + ".")
    
    
    
colores(color1="rojo", color2="azul", color3="verde", color4="amarillo")


#Parte 2 del video
def colores (**kwargs):
    print ("Este es el color " + kwargs["color1"] + ".")
    
    
    
colores(color1="rojo", color2="azul", color3="verde", color4="amarillo")

#Parte 3 del video
def suma (x, y):
    return x + y

total =suma(10, 10)
print (total) 

def resta (x, y):
    return x - y

total =resta(10, 10)
print (total)    

def mul (x, y):
    return x * y

total =mul(10, 10)
print (total) 

def div (x, y):
    return x / y

total =div(10, 10)
print (total) 


#Parte 4 del video
def colores ():
    pass

    
#Parte 5 del video
def colores(color="Rojo"):
    print("Mi color favorito es el " + color)
    
colores("azul")
colores()
colores("verde")
    
