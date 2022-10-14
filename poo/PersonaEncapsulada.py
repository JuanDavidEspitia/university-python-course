class Persona:
    def __init__(self, nombre, apellido, edad):
        # Atributos encapsulados
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    # Este es el metodo destructor
    def __del__(self):
        print("Estamos eliminando el objeto con el metodo destructor")
        print(f'Objeto a eliminar: Persona: {self._nombre} {self._apellido} {self._edad}')



if __name__ == '__main__':
    persona1 = Persona('Juan', 'Espitia', 28)
    persona1.mostrar_detalle()
    persona1.nombre = 'Laura'
    persona1.apellido = 'Peña'
    persona1.edad = 15
    persona1.mostrar_detalle()

    print(__name__)
