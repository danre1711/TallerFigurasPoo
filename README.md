• Descripción del ejercicio
Este taller consiste en aplicar Programación Orientada a Objetos (POO) en Python utilizando:
Encapsulamiento (@property y setters)
Herencia
Sobrescritura de métodos
Polimorfismo
Validaciones internas
Estructura siguiendo PEP8
Se implementa una clase base FiguraGeometrica y dos clases hijas: Cuadrado y Rectangulo, cada una con cálculos de área, perímetro y un método __str__() sobrescrito.
Además, se desarrolla un archivo principal main.py para demostrar el funcionamiento.


• Explicación breve de cada clase.
-figura_geometrica.py
Contiene la clase base FiguraGeometrica, con atributos privados _alto y _ancho.
Incluye:
Encapsulamiento usando @property y @setter
Validaciones obligatorias (alto y ancho > 0)
Método area()
Método perimetro() (sin implementar)
Método __str__() para mostrar dimensiones

-cuadrado.py
Clase hija Cuadrado que hereda de FiguraGeometrica.
Incluye:
Constructor que recibe un solo valor (lado)
Asignación a alto y ancho usando setters
Sobrescritura de:
area()
perimetro()
__str__()

-rectangulo.py
Clase hija Rectangulo.
Sobrescribe:
area()
perimetro()
__str__()

-main.py
Archivo principal que:
Crea dos cuadrados y dos rectángulos.
Muestra área, perímetro, valores y modificaciones.
Prueba errores con valores inválidos.
Implementa funciones:
sumar_areas()
sumar_perimetros()
Demuestra polimorfismo, llamando métodos sin saber qué tipo de figura es.

• Captura de pantalla de la ejecución 
<img width="1919" height="1069" alt="Captura de pantalla 2025-11-20 215421" src="https://github.com/user-attachments/assets/d33640ed-28a0-4faf-b50e-5cb5d59e19ad" />

<img width="691" height="585" alt="image" src="https://github.com/user-attachments/assets/de175047-f929-4194-bced-448112137b81" />


