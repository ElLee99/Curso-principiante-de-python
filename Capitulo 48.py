#Capitulo 48
#Johan Manuel García Zúñiga 19310416 6E1

import re

texto = "tres tristes tigres comen trigo en un trigal"

busqueda = re.findall("es", texto)
print(busqueda)

busqueda = re.findall("Es", texto)
print(busqueda)
