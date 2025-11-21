from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho: float, alto: float):
        super().__init__(ancho, alto)
    def area(self):
        return self.alto * self.alto
    def perimetro(self):
        return 2 * (self.alto + self.ancho)
    def __str__(self):
        return f'rectangulo (ancho={self.ancho}, alto={self.alto})'