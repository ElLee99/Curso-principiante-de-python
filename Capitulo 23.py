#Capitulo 23
#Johan Manuel García Zúñiga 19310416 6E1

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Ya eres un adulto.')    
elif edad > 100 and edad <= 120:
	print('Ya estás viviendo timpo extra.')      
else:
	print('Edad no válida.')