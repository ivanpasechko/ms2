import math

class Figure:
    def get_area(self) -> float:
        raise NotImplementedError
        
    def get_perimeter(self) -> float:
        raise NotImplementedError

    def compare_area(self, other: 'Figure') -> str:
        if self.get_area() > other.get_area():
            return "Больше"
        elif self.get_area() < other.get_area():
            return "Меньше"
        return "Равны"

    def compare_perimeter(self, other: 'Figure') -> str:
        if self.get_perimeter() > other.get_perimeter():
            return "Больше"
        elif self.get_perimeter() < other.get_perimeter():
            return "Меньше"
        return "Равны"

class Square(Figure):
    def __init__(self, side: float):
        self.side = side
    def get_area(self) -> float: return self.side ** 2
    def get_perimeter(self) -> float: return self.side * 4

class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a, self.b = a, b
    def get_area(self) -> float: return self.a * self.b
    def get_perimeter(self) -> float: return 2 * (self.a + self.b)

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c
    def get_perimeter(self) -> float: return self.a + self.b + self.c
    def get_area(self) -> float:
        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius
    def get_area(self) -> float: return math.pi * (self.radius ** 2)
    def get_perimeter(self) -> float: return 2 * math.pi * self.radius