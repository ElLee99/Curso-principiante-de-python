#Capitulo 50
#Johan Manuel García Zúñiga 19310416 6E1

import re 
texto = "siete séptimos son siete más de los que tienes"
resultado = re.findall("\Asiete", texto)
print (resultado)

resultado = re.findall("\Asie", texto)
print (resultado)

resultado = re.findall("\Ason", texto)
print (resultado)

resultado = re.findall("\D", texto)
print (resultado)

resultado = re.findall("sép..mos", texto)
print (resultado)
 
texto = "siete séptimos son siete séptimas más de los que tienes"
resultado = re.findall("séptimos | séptimas", texto)
print (resultado)

resultado = re.findall("séptimos | séptimas | aloo", texto)
print (resultado)

resultado = re.findall("[eé]", texto)
print (resultado)

resultado = re.findall("[a-p]", texto)
print (resultado)