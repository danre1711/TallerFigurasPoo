from cuadrado import Cuadrado
from rectangulo import Rectangulo

#funciones que suman las areas y los perimetros
def sumar_areas(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total

#funcion que muestra el codigo
def main():
    print("---Calculos para las figuras geometricas ---")

#valores asignados a cada figura
    c1 = Cuadrado(5)
    c2 = Cuadrado(3)

    r1 = Rectangulo(4, 6)
    r2 = Rectangulo(2, 10)

    figuras = [c1, c2, r1, r2]

    #demostracion de los valores
    for f in figuras:
        print(f)
        print(f"Área: {f.area()}")
        print(f"Perímetro: {f.perimetro()}\n")

    #demostracion de los errores
    print("---Erorres---")
    try:
        c3 = Cuadrado(-5)
    except ValueError as i:
        print("Error!!!", i)

    try:
        r3 = Rectangulo(0, 8)
    except ValueError as i:
        print("Error!!!", i)

    #Muestra las sumas de las areas y los perimetro
    print("")
    print("---Suma de areas y perimetros---")
    print("Suma de areas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))


if __name__ == "__main__":
    main()
