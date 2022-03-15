#Capitulo 44
#Johan Manuel García Zúñiga 19310416 6E1

import math

def area(radio):
    resultado = round(math.pi * radio * radio, 2)
    print (resultado)
    
area(2)

area =lambda radio: round(math.pi * radio * radio, 2)

print(area(2))
