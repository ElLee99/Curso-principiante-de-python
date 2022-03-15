#Capitulo 26
#Johan Manuel García Zúñiga 19310416 6E1


#Parte 1
x = 100
y = 200

if x < y: print("x es menor que y")
    

#Parte 2
print("Se ejecuta el if") if x < y else print("Se ejecita el else")


#Parte 3
x = 100
y = 200
z = 300

if x < y and z > y:
    print("Se cumplen las dos condiciones")
else:
    print("No se cumple una o ninguna de las condiciones")
    
if x < y or z > y:
     print("Se cumplen cualquier de las dos condiciones")
else:
     print("No se cumple una o ninguna de las condiciones")
     
#Parte 4
x = 100
y = 200
z = 300

if x < y:
    pass

