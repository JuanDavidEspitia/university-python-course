from Empleado import Empleado
from Gerente import Gerente

# Polimorfismo es multiples formas en tiempo de ejecucion

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    # Metodo isinstance nos permite preguntar si la instacia que queremos
    # validar corresponde a una instancia de cierta clase
    # si el objeto recibo pertenece a cierta instancia
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)