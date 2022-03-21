#Capitulo 28
#Johan Manuel García Zúñiga 19310416 6E1

x = 0
while x <= 30:
    x += 1

    if (x== 4 or x== 6 or x== 10):
        print("Se saltó el valor " +  str(x) + " de x")
        continue

    if (x==15):
        print ("Se rompió la ejecución del bucle cuando x valía: " + str(x))
        break

    print ("El valor del bucle es " + str(x))
