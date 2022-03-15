#Capitulo 49
#Johan Manuel García Zúñiga 19310416 6E1

import re

texto = "Aquellos que no conocen la historia están condenados a repetirla - Edmund Burke"

resultado = re.split(" ", texto)
print (resultado)
resultado = re.split("que", texto)
print (resultado)
resultado = re.split("que", texto, 4)
print (resultado)


resultado = re.sub(" ", "-", texto)
print (resultado)
resultado = re.sub(" ", "-----", texto)
print (resultado)
resultado = re.sub(" ", "-----", texto, 4)
print (resultado)