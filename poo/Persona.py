# Sitanxis Basica para crear una clase
class Persona:
    """
    Metodo Inicializador
    """
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Espitia'
        self.edad = 26


# Para crear un objeto, se llama de manera indirecta el metodo __init__
persona1 = Persona()

# Accedemos al atributo del objeto
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
