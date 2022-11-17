try:
    10/0# Esto genera una excepcion
except Exception as e:
    print(f'Ocurrio un error: {e} de Tipo: {type(e)}')


try:
    10/0
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}')
