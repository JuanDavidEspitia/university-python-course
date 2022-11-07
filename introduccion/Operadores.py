#Operadores Aritmeticos
"""
Adicion: +
Substraccion: -
Multiplicacion: *
Division: /
Intehger Division:  //
Exponenciacion:  **
Modulo/Reciduo: %
"""
# Suma de dos digitos
operandoA = 7
operandoB = 2

suma = operandoA + operandoB
print('Resultado de la suma: ', suma)

# Es la mejor forma de imprimir los resultados
print(f'Resultado de la suma: {suma}')
resta = operandoA - operandoB
print(f'Resultado de la Resta: {resta}')

# Funcion de residuo
numero1 = 24
numero2 = 5
reciduo = numero1 % numero2
print(f'El residuo es: {reciduo}')

# Ejercicio de area y perimetro de un rectangulo
alto = int(input('Ingrese el alto: '))
ancho = int(input('Ingrese el ancho: '))

print(f'El area es: {alto*ancho}, El permitro es: {(alto*2) + (ancho*2)}')

# Operadores de asigancion
"""
Operador de asigancion:
Asignacion: =
"""
miVariable = 10

"""
Operadores de reasigancion:
mivariable = mivaraiable + 1
"""
miVariable = miVariable * 2
print(miVariable)

miVariable += 3
print(miVariable)

miVariable -= 4
print(miVariable)

miVariable *= 5
print(miVariable)

# Operadores de comparacion:
"""
Nos permite saber sin dos valores son iguales o distintos
"""
a = 4
b = 6

resultado = (a == b)
print(f'Resultado: ', resultado)


# Para validar si son diferentes
resultado = (a != b)
print(f'Resultado: ', resultado)

resultado = (a < b)
print(f'Resultado: ', resultado)

resultado = (a > b)
print(f'Resultado: ', resultado)

# Ejercicio para validar si un numero es par o impar
numero = int(input("Ingrese el numero a validar: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# Ejercicio para determinar si es mayor de edad
edad = int(input("Ingrese la edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

"""
Operadores Logicos:
AND: Devuelve TRUE si ambos operandos son TRUE
OR: Devuelve TRUE si alguno de los operandos es TRUE
NOT: Devuelve TRUE si algino de los operandos son FALSE
"""

a = True
b = True
res = a and b
print(res)

c = True
d = False
res1 = c or d
print(res1)

e = True
res2 = not e
print(res2)

vacaciones = True
diaDescanzo = False

if not (vacaciones or diaDescanzo):
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")


"""
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cual número es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
"""
numero1 = int(input("Proporciona el Número 1:"))
numero2 = int(input("Proporciona el Número 2:"))

if numero1 > numero2:
    print("Número 1 es mayor")
else:
    print("Número 2 es mayor")









