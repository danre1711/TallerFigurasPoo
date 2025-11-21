'''
Esta clase representa a las figuras geometricas
'''
class FiguraGeometrica:
    def __init__(self, alto: float, ancho:float):
       self.alto = alto
       self.ancho = ancho
#propiedades para ancho
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
        #validacion para que el valor sea mayor que 0
           raise ValueError('El ancho debe ser mayor que 0')
        self._ancho = valor


#propiedades para alto
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            # validacion para que el valor sea mayor que 0
           raise ValueError('El alto debe ser mayor que 0')
        self._alto = valor


#metodos
    def area(self):
      return self.ancho * self.alto
    def perimetro(self):
        pass
    def __str__(self):
       return f'alto: {self.alto}, ancho: {self.ancho}'