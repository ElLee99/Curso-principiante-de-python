#Capitulo 35
#Johan Manuel García Zúñiga 19310416 6E1

#Parte 1
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') # 4 argumentos
colores('lila', 'negro', 'rojo')             # 3 argumentos
colores('rosa')                              # 1 argumento
colores('marrón', 'naranja')                 # 2 argumentos

#Parte 2
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('Verde fosforiloco', 'Rosa fosforecente')

#Parte 3

def suma(*args):
    for x in args:
        sumar = args[0] + args[1] + args[2] + args[3] + args[4]
    print (sumar)
    
    
suma(20, 10, 56, 34, 89)