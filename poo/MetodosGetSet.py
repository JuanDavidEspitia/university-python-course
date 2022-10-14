class PersonaArg:

    def __init__(self, nombre, apellido, edad):
        # Las variables con _<> estan encapsuladas
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Metodos Get y Set
    # Get: Para obtner/recuperar
    # Set: Modificar/Colocar

    # Los decoradores modifican el comportamiento de nuestros metodos @property
    # para encapsular el atributo y solo se accede asa variabla atraves del metodo get
    @property
    def nombre(self):
        # Metodo GET
        print("Llamando metodo GET Nombre")
        return self._nombre

    # Metodo SET
    @nombre.setter
    def nombre(self, nombre):
        print("Llamando metodo SET nombre")
        self._nombre = nombre



    def mostrar_detalle(self):
        print(f'Persona:  Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}')

# Cuando se llama un param
persona1 = PersonaArg('Juan', 'Espitia', 34)
print(persona1.nombre)

# para setear  una variable
persona1.nombre = 'Laura'
print(persona1.nombre)

"""
 Cuando definimos un metodo get para una viarible sin el metodo SET, se conocen como variables de solo lectura
 """