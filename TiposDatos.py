"""
Tipos de Datos
Numeric : {
    Integer:
    Float:
    Complex Numer:
        }

Diccionary

Boolean

Set

Sequence Type: {
    Strings:
    List:
    Tuple:
    }
"""

# Declaramos diferentes tipos de datos
numero = 10
# Imprimimos el tipo de dato con la funcion type()
print(type(numero))

cadena = "Hola Mundo"
print(type(cadena))

# Podemos asiganrle un tipo de dato a nuestra variable
x: str = "Hola Mundo"
print(type(x))
# Las  variables en python siempre son dinamicas

float = 10.45
print(type(float))

boolean = True
print(type(boolean))

# Los tipos de datos tambien son clases

# Variables de tipo Cadena
miGrupoFaborito = "Aerosmith"
miCancionFAvorita = "Angel"
# Concatenacion de cadenas
resultado = "Grupo: " + miGrupoFaborito + "Cancion: " + miCancionFAvorita
print(resultado)

# Mas manejo de Cadenas
comentario = "Thebest rock band"
print("Mi Grupo favorito es: ", miGrupoFaborito, comentario)

numero1 = "1"
numero2 = "2"
print("Concatenacion: ", numero1 + numero2)

# Convertir cadena a integer
int(numero1)
print("Suma: ", int(numero1) + int(numero2))

# Tipos Booleanos

variableTrue = True
variableFalse = False

miVaraiableBool = 2 > 4

print(variableFalse)
print(miVaraiableBool)

if miVaraiableBool:
    print("Resultado Verdadero")
else:
    print("Resultado Falso")



# Entradas del usuario
# La funcion input retorna un string
print("Ingrese dos valores para realizar una suma:")
entrada1: int = input("Ingrese el primer valor: ")
entrada2: int = input("Ingrese el segundo valor: ")

resultado: int = int(entrada1) + int(entrada2)
print(resultado)

# Ejercicio
titulo = input("Proporciona el titulo del libro: ")
autor = input("Proporciona el nombre del autor: ")
print(titulo, "Fue escrito por, ", autor)













