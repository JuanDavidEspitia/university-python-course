class MiClase:
    # Variables de clase, son aquellas que estan fuera del metodo Init
    variable_clase = 'Valor de variable de clase'


    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia # va


    # Metodos estaticos
    # Se asocia con la clase, no acceden a las variables de instancia
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)



print(MiClase.variable_clase)

miClase = MiClase('Valor varibale de instancia')
print(miClase.variable_instancia)

miClase = MiClase('Otro Valor variable de instancia')
print(miClase.variable_instancia)
print(MiClase.variable_clase)


print(MiClase.metodo_estatico())
print(MiClase.metodo_clase())