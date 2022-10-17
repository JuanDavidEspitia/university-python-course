class Color:
    def __init__(self, color):
        self._color = color

    # Metodo Get
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return  f'Color [Color: {self._color}]'