#Capitulo 47
#Johan Manuel García Zúñiga 19310416 6E1

import re

texto = "Bienvenido a Progrmación con L33"

busqueda = re.search("i", texto)
print(busqueda)
busqueda = re.search("b", texto)
print(busqueda)
busqueda = re.search("L33", texto)
print(busqueda)
busqueda = re.search("Bienvenido a Progrmación con L33", texto)
print(busqueda)
busqueda = re.search("Bienvenido a Progrmacion con L33", texto)
print(busqueda)