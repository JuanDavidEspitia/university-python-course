# Una LISTA es un conjunto de elementos
# De diferentes tipos de datos
# las listas se componen de indices

# Declaramos una lista
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria', 0,  100, True]

# Imprimimos la lista de nombres
print(nombres)


# Accedemos a los elementos de la lista
# Para ver el indici 1 (es decir la posicion 2)
print("Imprimimos la posicion 2 del arreglo")
print(nombres[1])

# Acceder a los elementos de manera inversa
print(f'El ultimo elemento es: {nombres[-1]}')

# Acceder a un rango de nuestra lista
# Accedemos desde el indice 0 hasta el 2
print(nombres[0:2]) # Sin incluir el indice 2
# Desde el indice 1 hasta el 3
print(nombres[ :3])

#Recorremos la lista desde el indice indicado hasta el final
print(nombres[1:])

# Para cambiar un valor de un elemento de la lista
nombres[2] =  'Laura'
print(nombres)

# Para iterar una lista es con la siguiente funcion
for nombre in nombres:
    print(f'Elemento de la lista:', nombre)
else:
    print('No existen mas nombres en la lista')


# preguntar el largo o cantidad de elementos de una lista
print(len(nombres))

# agregar un elemento
nombres.append('Lorenzo')
print(nombres)

# insertar un elemento en un índice en específico
nombres.insert(3, 'Octavio')
print(nombres)

# remover un elemento
nombres.remove('Octavio')
print(nombres)

# remover el último valor agregado
nombres.pop()
print(nombres)

# eliminar un indice
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# borrar la lista por completo
#del nombres
#print(nombres)


# Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)
# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos
print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2,7)
for i in rango:
    print(i)

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
rango = range(3,11,2)
for i in rango:
    print(i)













