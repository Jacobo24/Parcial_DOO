from abc import ABC, abstractmethod

# Interfaz Shape con responsabilidad única de calcular el área de una forma
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Clase Circle que implementa Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# Clase Square que implementa Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Clase AreaCalculator que calcula el área total de una lista de formas
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

# Uso del código refactorizado
shapes = [Circle(1.0), Square(1.0)]
calculator = AreaCalculator(shapes)
print(calculator.total_area())  # Salida esperada: 4.14159