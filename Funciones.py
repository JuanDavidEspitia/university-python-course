# Deficion de una funcion

def mi_funcion():
    print('Saludos desde mi funcion')

# La funciones se pueden llamar N veces
mi_funcion()
mi_funcion()


# Paso de argumentos a una funcion

def mi_funcion_python(nombre, apellido):
    print(f'la persona es: {nombre} {apellido}')

mi_funcion_python('Juan', 'Espitia')
mi_funcion_python('Laura', 'Peña')


# Palabra return en funciones Python

def sumar(a, b):
    c = 0
    c = a + b
    return c

resultado = sumar(5, 10)
print('Resultado de la suma: ',resultado)

# La operacion de resultado la puedo hacer en el mismo return
def restar(a, b):
    return a - b

print(f'Resultado de la resta es: {restar(30,10)}')

# valores por dafault a los parametros de una funcion
def multiplicar(a=4, b=4) -> int:
    return a * b

# Se puede especificar el tipo de dato pero se considera redundante
def multiplicar2(a:int=4, b:int=4) -> int:
    return a * b

print(f'Resultado de la multiplicacion: {multiplicar()}')


# Argumentos variables en Python, cuando se desconoce la cantidad de argumentos
# Se le antepone el *
# De esta manera python lo convierte a tuplas
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

# Podemos pasar N Argumentos variables en Python
listarNombres('Juan', 'Pedro', 'Luis', 'Laura', 'Cris')

# en la documentacion de python se conoce como *args, cantidad de parametros indefinidos
def hola_mundo(*args):
    print('Argumentos variables')


# Ejercicio 1 de Argumentos Variables
"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""
# Definimos nuestra funcion para sumar valores, esto se convierte una tupla
def sumar_valores(*args):
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado


# Llamada a la funcion
print('el resultado de la funcion es: ', sumar_valores(3, 5, 9, 4, 6))


# Ejercicio 2
"""
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""
# Definicion de la funcion para multiplicar valores
def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        # resultado = resultado * numero
        resultado *= numero
    return resultado

# Llamada de la funcion
print(multiplicar_valores(3,5,15,3))


# Ahora si queremos una funcion que reciba paramtros clave:valor debe ser de la siguiente forma
# Se coloca con doble ** y es para elementos de llave:valor, es decir retorna un diccionario
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


listarTerminos(IDE='Integrated Development Enviroment', OOP='Object Oriented Programing',
               DBMS= 'Data Base Managment System')

# Ejemplo de envio de un diccionario como argumentos
kwargs = {"arg3": 3, "arg2": "dos", "arg1": 5}
listarTerminos(**kwargs)

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programing',
    'DBMS': 'Data Base Managment System'
}
listarTerminos(**diccionario)
















