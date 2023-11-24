import math
from src.figure_calculating.figure import Figure

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        if is_valid_rectangle(length, width):
            self.length = length
            self.width = width
        else:
            raise ValueError("Это не прямоугольник")

    def calculate_area(self):
        return self.length * self.width

def is_valid_rectangle(a, b):
    return a != b

rectangle=Rectangle(length=1, width=2)
area=rectangle.calculate_area()
print(area)