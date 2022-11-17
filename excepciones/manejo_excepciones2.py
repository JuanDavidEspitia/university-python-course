from excepciones.exception_custom import NumerosIdenticosException

resultado = None
a = 10
b = 0

try:
    resultado = a / b
except BaseException as e:
    print(f'Ocurrio un error: {e} de Tipo: {type(e)}')


print(f'Resultado: {resultado}')
print('Continuamos ....')


a = '10'
b = 0
# Primero ponemos las clases hijas de las excepciones y luego la padre
try:
    resultado = a / b
except ZeroDivisionError as ze:
    print(f'Ocurrio un error: {ze} de Tipo: {type(ze)}')
except TypeError as te:
    print(f'Ocurrio un error: {te} de Tipo: {type(te)}')
except Exception as e: # Esta clase padre se debe colocar al final, si no conocemos las posibles excepciones
    print(f'Ocurrio un error: {e} de Tipo: {type(e)}')


print('Continuamos 2 ....')

res = None
# Primero ponemos las clases hijas de las excepciones y luego la padre
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        # Lanza Excepciones personalizadas
        raise NumerosIdenticosException('Numeros Identicos')

    res = a / b
except ZeroDivisionError as ze:
    print(f'Ocurrio un error: {ze} de Tipo: {type(ze)}')
except TypeError as te:
    print(f'Ocurrio un error: {te} de Tipo: {type(te)}')
except ValueError as ve:
    print(f'Ocurrio un error: {ve} de Tipo: {type(ve)}')
except Exception as e: # Esta clase padre se debe colocar al final, si no conocemos las posibles excepciones
    print(f'Ocurrio un error: {e} de Tipo: {type(e)}')
else:
    print('No se arrojo ninguna excepcion (Se ejecuta siempre y cuando no halla ninguna excepcion)')
finally:
    print('Este bloque Finally siempre se ejecuta')

print(f'Resultado de la solicitud por consola: {res}')

