import math
from src.figure_calculating.figure import Figure

class Square(Figure):
    def __init__(self, side):
        super().__init__()
        if is_valid_square(side):
            self.side = side
        else:
            raise ValueError("Это не квадрат")

    def calculate_area(self):
        return (self.side ** 2)

def is_valid_square(side):
    return side > 0

sqare=Square(side=5)
area=sqare.calculate_area()
print(area)