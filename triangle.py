import math

from src.figure_calculating.figure import Figure

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        super().__init__()
        if is_valid_triangle(side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError("Это не треугольник")
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

triangle = Triangle(0, 14, 15)
area = triangle.calculate_area()
print(area)