class Persona:
    #Clase Padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo para retornar el objeto en String
    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # Importar el contructor de la clase Padre, con los atributos
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado[Sueldo: {self.sueldo}] {super().__str__()} '