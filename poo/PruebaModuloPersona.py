# Llamamos o importamos modulos(archivos python) o clases desde otro archivo/modulo
# de esta forma la importamos
from PersonaEncapsulada import Persona

print(' Creacion de Objeto '.center(50, '*'))
persona1 = Persona('Cristian', 'Aguillon', 30)
persona1.mostrar_detalle()

# Main = Principal (Modulo Principal)
print(__name__)

"""
    Metodo Destructor
    
"""

print(' Elimiancion de Objetos '.center(50, '*'))
print("Ingresa al metodo destructor que esta en la clase persona")
del persona1


