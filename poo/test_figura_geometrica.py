from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')


# MRO - Method Resolution Order
# Metodo que nos retorna el orden en que se ejecutan las funciones o los metodos de una clase
print(Cuadrado.mro())
# Output:
# [<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'Color.Color'>, <class 'object'>]

print(cuadrado1)