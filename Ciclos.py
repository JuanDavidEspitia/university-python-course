# Sentencia While
# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')
contador = 0
while contador < 3:
    print(contador)
    contador += 1 #contador = contador + 1
else:
    print('Fin ciclo while')

print("While con contador inverso")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1 #contador = contador + 1
else:
    print('Fin ciclo while')

# Ciclo FOR

cadena = "Hola"
# Iteramos una cadena
for letra in cadena:
    print(letra)

# Palabra BREAK en Python
# la palabra Break se usa para romper el ciclo
for letra in 'Holanda':
    if letra == 'a':
        print("El valor es: ", letra)
        break
    else:
        print("Fin de la condicion")

# Palabra CONTINUE
# la funcion range imprime valores de 0 al valor que le ingresemos
for i in range(6):
    if i % 2 == 0:
        print(f'Valor Par: {i}')

# Usamos la palabra continue, desdes de esta palabra no ejecuta el codigo siguiente y comienza la siguiente iteracion
for i in range(6):
    if i % 2 != 0:
        print(f'Valor Impar: {i}')
        continue








