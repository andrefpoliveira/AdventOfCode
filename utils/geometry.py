class Point:
    def __init__(self, *args):
        coordinates = args[0]
        if len(args) > 1:
            coordinates = tuple(args)

        self.coordinates = coordinates
        self.dimensions = len(coordinates)

    def __str__(self):
        return f"Point({', '.join(str(p) for p in self.coordinates)})"

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    @property
    def z(self):
        return self.coordinates[2]

    def __add__(self, point):
        if not isinstance(point, Point): raise ValueError("Adding something that is not a point")
        if self.dimensions != point.dimensions: raise ValueError(f"Points with different dimensions! {self} + {point}")

        return Point(
            tuple(c1 + c2 for c1, c2 in zip(self.coordinates, point.coordinates))
        )

    def __eq__(self, point):
        if not isinstance(point, Point): raise ValueError("Adding something that is not a point")
        if self.dimensions != point.dimensions: raise ValueError(f"Points with different dimensions! {self} + {point}")

        return all(c1 == c2 for c1, c2 in zip(self.coordinates, point.coordinates))

    def __hash__(self):
        return hash(self.coordinates)

    @staticmethod
    def euclidean(p1, p2):
        """Calculates the euclidean distance between 2 points"""
        if not isinstance(p1, Point) or not isinstance(p2, Point): raise ValueError("Both arguments must be points")
        if p1.dimensions != p2.dimensions: raise ValueError(f"Points with different dimensions! {p1}, {p2}")

        return sum(pow(c1 - c2, 2) for c1, c2 in zip(p1.coordinates, p2.coordinates))

    @staticmethod
    def manhattan(p1, p2):
        """Calculates the manhattan distance between 2 points"""
        if not isinstance(p1, Point) or not isinstance(p2, Point): raise ValueError("Both arguments must be points")
        if p1.dimensions != p2.dimensions: raise ValueError(f"Points with different dimensions! {p1}, {p2}")

        return sum(abs(c1 - c2) for c1, c2 in zip(p1.coordinates, p2.coordinates))

Point.NORTH = Point((1, 0))
Point.SOUTH = Point((-1, 0))
Point.EAST = Point((0, 1))
Point.WEST = Point((0, -1))

Point.UP = Point((1, 0))
Point.DOWN = Point((-1, 0))
Point.RIGHT = Point((0, 1))
Point.LEFT = Point((0, -1))