#Pip installed numpy
import numpy as np


class Polygon:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        print("Area is:", self.side1 * self.side2, "\n")

    def perimeter(self):
        print("Perimeter is:", (self.side1 * 2) + (self.side2 * 2))


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2)
        self.side3 = side3
        global n
        n = 3

    def area(self):
        a = self.side1 / (2 * np.tan(np.deg2rad(180/n)))
        p = self.side1 * n
        print("Area of this polygon is:", (p * a) / 2, "\n")

    def perimeter(self):
        print("Perimeter of triangle is:", (self.side1 + self.side2 + self.side3))


class Quadrilateral(Polygon):
    def __init__(self, side1, side2, side3, side4):
        super().__init__(side1, side2)
        self.side3 = side3
        self.side4 = side4

    def perimeter(self):
        print("Perimeter of quadrilateral is:", (self.side1 + self.side2 + self.side3 + self.side4))


class Pentagon(Triangle):
    def __init__(self, side1, side2, side3, side4, side5):
        super().__init__(side1, side2, side3)
        self.side4 = side4
        self.side5 = side5
        global n
        n = 5

    def perimeter(self):
        print("Perimeter pentagon is:", (self.side1 + self.side2 + self.side3 + self.side4 + self.side5))


class Hexagon(Triangle):
    def __init__(self, side1, side2, side3, side4, side5, side6):
        super().__init__(side1, side2, side3)
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6
        global n
        n = 6

    def perimeter(self):
        print("Perimeter of hexagon is:", (self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6))


class Octagon(Triangle):
    def __init__(self, side1, side2, side3, side4, side5, side6, side7, side8):
        super().__init__(side1, side2, side3)
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6
        self.side7 = side7
        self.side8 = side8
        global n
        n = 8

    def perimeter(self):
        print("Perimeter of octagon is:", (self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6 + self.side7 + self.side8))


class IsocelesTriangle(Triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def perimeter(self):
        print("Perimeter of triangle is:", (self.side1 + self.side2 + self.side3))


class EquilateralTriangle(Triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(self.side1,side2,side3)\


    def perimeter(self):
        print("Perimeter of triangle is:", (self.side1 * 3))


class Rectangle(Quadrilateral):
    def __init__(self, side1, side2, side3, side4):
        super().__init__(side1, side2, side3, side4)

    def perimeter(self):
        print("Perimeter of rectangle is:", (self.side1 + self.side2 + self.side3 + self.side4))

    def area(self):
        print("Area of rectangle is:", (self.side1 * self.side3), "\n")


class Square(Quadrilateral):
    def __init__(self, side1, side2, side3, side4):
        super().__init__(side1, side2, side3, side4)

    def perimeter(self):
        print("Perimeter of square is:", (self.side1 * 4))

    def area(self):
        print("Area of square is:", (self.side1 * self.side2), "\n")


tri = Triangle(3, 3, 3)
tri.perimeter()
tri.area()

quad = Quadrilateral(4, 4, 4, 4)
quad.perimeter()
quad.area()

rec = Rectangle(3, 3, 5, 5)
rec.perimeter()
rec.area()

squ = Square(6, 6, 6, 6)
squ.perimeter()
squ.area()

pent = Pentagon(7, 7, 7, 7, 7)
pent.perimeter()
pent.area()

hexa = Hexagon(8, 8, 8, 8, 8, 8)
hexa.perimeter()
hexa.area()

octa = Octagon(9, 9, 9, 9, 9, 9, 9, 9)
octa.perimeter()
octa.area()