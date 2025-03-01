class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Segment:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
        self.distance = self.get_distance()

    def __repr__(self):
        return f'({self.point_1.x}, {self.point_1.y}), ({self.point_2.x}, {self.point_2.y})'

    def get_distance(self) -> float:
        return ((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point) -> None:
        self.p_1 = point_1
        self.p_2 = point_2
        self.p_3 = point_3

        self.s_1 = Segment(self.p_1, self.p_2)
        self.s_2 = Segment(self.p_2, self.p_3)
        self.s_3 = Segment(self.p_3, self.p_1)

        self.area = self.get_area()

    def __repr__(self):
        return f"a={self.s_2.distance}, b={self.s_3.distance}, c={self.s_1.distance}"

    def get_area(self) -> float:
        p = (self.s_1.distance + self.s_2.distance + self.s_3.distance) / 2
        area = (p * (p - self.s_1.distance) * (p - self.s_2.distance) * (p - self.s_3.distance)) ** 0.5
        return area


###############################

A = Point(0, 4)
B = Point(3, 0)
C = Point(0, 0)

ABC = Triangle(A, B, C)

print(ABC.area)
