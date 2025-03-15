# Інкапсуляція
# Наслідування

class Point:
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


class Segment:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self._point_1 = point_1
        self._point_2 = point_2
        self._distance = self.get_distance()

    def __repr__(self):
        return f'({self._point_1.x}, {self._point_1.y}), ({self._point_2.x}, {self._point_2.y})'

    @property
    def distance(self) -> float:
        return self._distance

    def get_distance(self) -> float:
        return ((self._point_1.x - self._point_2.x) ** 2 + (self._point_1.y - self._point_2.y) ** 2) ** 0.5


class Vector(Segment):
    def __init__(self, point_1: Point, point_2: Point) -> None:
        super().__init__(point_1, point_2)
        self._coordinates = self.get_coordinates()

    def __repr__(self):
        return f'{self.coordinates}, |a|={self.distance}'

    @property
    def coordinates(self) -> Point:
        return self._coordinates

    def get_coordinates(self) -> Point:
        a = self._point_2.x - self._point_1.x
        b = self._point_2.y - self._point_1.y
        return Point(a, b)


class Triangle:
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


###############################
A = Point(0, 4)
B = Point(3, 0)
# C = Point(0, 0)
#
# print(A)
#
# ABC = Triangle(A, B, C)
# # ABC.area = 12  ## AttributeError: property 'area' of 'Triangle' object has no setter
#
# print(ABC.area, ABC.get_area())

vector = Vector(A, B)

print(vector)
