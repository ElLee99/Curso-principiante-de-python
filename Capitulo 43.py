#Capitulo 43
#Johan Manuel García Zúñiga 19310416 6E1

#Parte1
def funcion1():
    variable1 = "Variable dentro de la función"
    print (variable1)
    
    def funcion2():
        variable1 = "He cambiado el valor de la variable"
        print (variable1)
        
    funcion2()
    
    
funcion1()


#Parte2
variable1 = "Variable fuera de la función"

def funcion1():
    variable1 = "Variable dentro de la funcion"
    print(variable1)
    
funcion1()
print(variable1)


#Parte3
def funcion1():
    global num1
    num1 = 10
    print(num1)
    
funcion1()
print(num1)

#Parte4
num1 = 50

def funcion1():
    global num1
    num1 = 10
    
funcion1()
print(num1)


    
    
    




    
