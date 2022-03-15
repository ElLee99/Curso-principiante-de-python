#Capitulo 51
#Johan Manuel García Zúñiga 19310416 6E1
 #Parte 
variable = "Correcto"
try:
    print (variable)
    
except:
    print ("Hay un error")


#Parte 2
reinicio = True

while reinicio:
    try:
        num1 = int (input ("Introduce un numero para multiplicar"))
        num2 = int (input ("Introduce otro numero para multiplicar"))
    except ValueError:
        print ("No has introducido un numero, calale con otro")
    else:
        print ("El resultado es: ", num1 * num2)
    finally:
        pregunta = input ("Quieres seguir multiplicando? S/N")
    if pregunta == "N" or pregunta == "n" :
        reinicio = False
    else:
        print("Oki doki")
            