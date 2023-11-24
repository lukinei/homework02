import math
from src.figure_calculating.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if is_valid_circle(radius):
            self.radius = radius
        else:
            raise ValueError("Это не круг")

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

def is_valid_circle(radius):
    return radius > 0

circle = Circle(radius=2)
area = circle.calculate_area()
print(area)