#Capitulo 46
#Johan Manuel García Zúñiga 19310416 6E1

import datetime, locale

locale.setlocale(locale.LC_ALL, "es-ES")

fecha = datetime.datetime.now()
print(fecha.strftime("%A"))

fecha = datetime.datetime(1998, 9, 30)
print(fecha.strftime("%A"))