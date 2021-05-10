import math

class Figure(object):
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        try:
            return self.a * self.b
        except:
            super().get_area()

    def get_perimeter(self):
        try:
            return 2*self.a + 2*self.b
        except:
            super().get_perimeter()


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        try:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        except:
            super().get_area()

    def get_perimeter(self):
        try:
            return self.a + self.b + self.c
        except:
            super().get_perimeter()


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        try:
            return math.pi * self.r * self.r
        except:
            super().get_area()

    def get_perimeter(self):
        try:
            return self.r * math.pi * 2
        except:
            super().get_perimeter()
