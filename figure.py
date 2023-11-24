class Figure():
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.calculate_area() + other.calculate_area()
        else:
            raise ValueError("")