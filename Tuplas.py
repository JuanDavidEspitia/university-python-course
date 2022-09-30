# Las tuplas son INMUTABLES
# La tupla guarda los elementos en orden
# Tambien tiene indices

# Declaracion de las tuplas
frutas = ('Naranja', 'Platano', 'Guayaba')
# Despues de declarada la tupla no se puede modificar ni agragar mas elementos
print(frutas)

# Tamaño de la tupla
print(len(frutas))

#acceder a un elemento
print(frutas[0])

# navegación inversa
print(frutas[-1])

# acceder a un rango
print(frutas[0:1])# sin incluir el último índice

# Si se va a declarar una tupla de un solo elemento debe ser asi
verduras = ('Tomate',)
print(verduras)

#recorrer elementos
for fruta in frutas:
    #print(fruta)
    print(fruta, end=' ') # Para que se impriman en una sola linea y cambiamos el salto de liena por espacio

#cambiar valor tupla
# frutas[0] = 'Pera' # No funciona de esta forma, se debe cambiar a Lista
frutasLista = list(frutas)
frutasLista[0] = 'Pera'

# Convertimos la lista nuevamente a tupla
frutas = tuple(frutasLista)
print('\n',frutas)

#eliminar la tupla
#del frutas
#print(frutas)


# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

# Definir la lista
lista = []
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

# Imprimimos la lista
print(lista)






