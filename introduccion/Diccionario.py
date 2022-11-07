# Una coleccion de datos en formato llave: Valor
# LLAVE : "VALOR"
# Simialar a un formato JSON

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programing',
    'DBMS': 'Data Base Managment System'
}
print(diccionario)

#largo
print(len(diccionario))

# acceder a un elemento (key)
print(diccionario['IDE'])

# otra forma de recuperar un elemento, siempre se hace mediante la LLAVE
print(diccionario.get('OOP'))

# modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# recorrer los elementos
for termino, valor in diccionario.items():
    print(termino)
    print(termino, valor)

# Loop que Regresa solamente las LLAVES
for termino in diccionario.keys():
    print(termino)

# Loop que Regresa solamente los valores asociados a cada llave
for valor in diccionario.values():
    print(valor)

# comprobar existencia de algún elemento, es KEY SENSITIVE
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario
#del diccionario
#print(diccionario)


