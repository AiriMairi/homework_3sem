from abc import ABC, abstractmethod, abstractclassmethod
import math

class Figure(ABC):
    """"Абстрактный класс геометрических фигур"""

    def __init__(self, side, injection):
        self.side = side
        self.injection = injection


class Sqart(Figure):

    def __init__(self, side):
        self.side = side

    @abstractmethod
    def area(self, side_sqart):
        self.side_sqart == side_sqart
        s_sqart = side_sqart ** 2
        print('Площадь квадрата равна', s_sqart)

    def perimetr(self, side_sqart):
        self.side_sqart == side_sqart
        p_sqart = side_sqart * 4
        print('Периметр квадрата равен', p_sqart)

    def diametr(self, side_sqart):
        self.side_sqart == side_sqart
        d_sqart = (side_sqart**2 + side_sqart**2)**(1/2)
        print('Диаметр квадрата равен', d_sqart)


class Triangle(Figure):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        p_triangle = (side1 + side2 + side3)/2
        s_triangle = ((1/2) ** (p_triangle * (p_triangle - side1) * (p_triangle - side2) * (p_triangle - side3)))
        print('Площадь треугольника равна', s_triangle)

    def perimetr(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        p_triangle = side1 + side2 + side3
        print('Периметр треугольника равен', p_triangle)

    def injection(self, injection1, injection2):
        self.injection1 = injection1
        self.injection2 = injection2
        injection_triangle = 180 - injection1 - injection2
        print('Неизвестный угол равен', injection_triangle)


class Rectangle(Figure):

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        s_rectangle = side1 * side2
        print('Площадь прямоугольника равна', s_rectangle)

    def perimetr(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        p_rectangle = 2*(side1 + side2)
        print('Периметр прямоугольника равен', p_rectangle)

    def diametr(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        d_rectangle = (side1**2 + side2**2)**(1/2)
        print('Диаметр квадрата равен', d_rectangle)

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        self.radius = radius
        s_circle = math.pi * (radius)**2
        print('Площадь круга равна', s_circle)

    def perimetr(self, radius):
        self.radius = radius
        p_circle = math.pi * (radius) * 2
        print('Периметр круга равен', p_circle)

    def diametr(self, radius):
        self.radius = radius
        d_circle = radius * 2
        print('Диаметр круга равен', d_circle)




сircle = Circle(5)
сircle.area(5)
сircle.perimetr(5)
сircle.diametr(5)

print()

sqart = Sqart(5)
sqart.area(5)
sqart.perimetr(5)
sqart.diametr(5)

print()

triangle = Triangle(3, 4, 5)
triangle.area(3, 4, 5)
triangle.perimetr(3, 4, 5)
triangle.injection(60, 25)

print()

rectangle = Rectangle(2, 3)
rectangle.area(2, 3)
rectangle.perimetr(2, 3)
rectangle.diametr(2, 3)


