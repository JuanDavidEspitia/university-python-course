class PersonaArg:
    # Le enviamos argumentos a nuestro metodo constructor
    # Con el metodo self decimos que son variables de nuestra clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def mostrar_detalle(self):
        print(f'Persona:  Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}')

# Creamos un primer objeto
persona1 = PersonaArg('Juan', 'Aguillon', 25)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# Podemos modificar los valores luego de creado
persona1.nombre = 'Luis'
persona1.apellido = 'Gomez'
persona1.edad = 29
print(f'Objeto Persona 1 Update:  Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}')


# Creamos otro objeto
persona2 =  PersonaArg('Laura', 'Peña', 23)
print(f'Objeto Persona 2:  Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')


# ahora probamos el metodo mostrar_detalle()
print("Ahora con el metodo de mostrar_detalle()")
persona2.mostrar_detalle()