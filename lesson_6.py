# Поліморфізм
import math

from lesson_4 import Point, Segment


class BaseFigure:

    def get_area(self):
        """
        This method should return the area of the figure.
        """
        raise NotImplementedError


class Triangle(BaseFigure):
    def __init__(self, point_1: Point, point_2: Point, point_3: Point) -> None:
        self._p_1 = point_1
        self._p_2 = point_2
        self._p_3 = point_3

        self._s_1 = Segment(self._p_1, self._p_2)
        self._s_2 = Segment(self._p_2, self._p_3)
        self._s_3 = Segment(self._p_3, self._p_1)

        self._area = self.get_area()

    def __repr__(self):
        return f"a={self._s_2.distance}, b={self._s_3.distance}, c={self._s_1.distance}"

    @property
    def area(self) -> float:
        return self._area

    def get_area(self) -> float:
        p = (self._s_1.distance + self._s_2.distance + self._s_3.distance) / 2
        area = (p * (p - self._s_1.distance) * (p - self._s_2.distance) * (p - self._s_3.distance)) ** 0.5
        return area


class Circle(BaseFigure):
    def __init__(self, point: Point, radius: float) -> None:
        self._center = point
        self._radius = radius

    def __repr__(self):
        return f"center={self._center}, radius={self._radius}"

    def get_area(self) -> float:
        return math.pi * self._radius ** 2


triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
circle = Circle(Point(0, 0), 1)

print(triangle.get_area())
print(circle.get_area())


####################################################
# value_1 = 2 + 3
# value_2 = "qwe" + "asd"
# value_3 = [1, 2, 3]  + [4, 5, 6]
# value_4 = (1, 2, 3) + (4, 5, 6)
#
# print(value_1, value_2, value_3, value_4)
####################################################
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


####################################################
a = Vector(3, 4)
b = Vector(3, 4)

c = a + b

print(a, id(a))
print(b, id(b))
print(c, id(c))
print(a == b)
