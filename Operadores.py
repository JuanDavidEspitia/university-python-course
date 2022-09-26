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










