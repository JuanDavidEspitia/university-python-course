# Sentencia de control IF
condicion = True

if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")
"""
OJO:
Cualquier valor difente de vacio es VERDADERO
"""
condicion = 10
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")

# Ejemplo 2
condicion = ''
if condicion:
    print("Condicion Verdadera")
else:
    print("Condicion Falsa")

# Aseguramos el valor Booleano
condicion = 'hola'
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion no reconocida")

# Validacion del Modo Debug
# Aseguramos el valor Booleano
condicion = 10
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion no reconocida")


# Ejercio de prueba
numero = int(input("Proporciona un valor entre 1 y 3: "))
numeroTexto = ''
if numero == 1:
    numeroTexto = "Numero Uno"
elif numero == 2:
    numeroTexto = "Numero Dos"
elif numero == 3:
    numeroTexto = "Numero Tres"
else:
    print("Numero fuera de rango")

print(f'Numero proporcionado es: {numeroTexto}')


# Sintaxis simplificada de sentencia de control IF
condicion = True
print('Condicion verdadera') if condicion else print('Condicion verdadera')


# Ejercio para calcular la estacion dependiendo del mes
mes = int(input('Proporciona mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estación es: {estacion}')


# Ejercicio de etapas de la vida
edad = int(input('Proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increíble...'
elif  10 <= edad < 20:
    mensaje = 'Muchos cambios, mucho estudio...'
elif  20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
elif 30 <= edad < 90:
    mensaje = 'Madures y estabilidad...'
else:
    mensaje = 'Etapa de vida NO reconocida'
print(f'Tu edad es: {edad}, {mensaje}')


# Ejercicio de sistema de calificaciones
"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""
calificacion = int(input("Proporciona una calificación entre 0 y 10: "))
# Si esta entre 9 y 10 imprimir: A
if 9 <= calificacion <= 10:
    print("A")
# Si esta entre  8 y menor a 9 imprimir: B
elif 8 <= calificacion < 9:
    print("B")
# Si esta entre 7 y menor a 8 imprimir: C
elif 7 <= calificacion < 8:
    print("C")
# Si esta entre 6 y menor a 7 imprimir: D
elif 6 <= calificacion < 7:
    print("D")
# Si esta entre 0 y menor a 6 imprimir: F
elif 0 <= calificacion < 6:
    print("F")
# Si no esta en el rago, imprimir: Valor desconocido
else:
    print("Valor desconocido")







