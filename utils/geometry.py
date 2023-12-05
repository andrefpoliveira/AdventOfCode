def get_neighbours(point, min_v, max_r, max_c, dirs):
    points = []
    for dir in dirs:
        dx, dy = point[0] + dir[0], point[1] + dir[1]
        if not(dx < min_v or dx >= max_r or dy < min_v or dy >= max_c):
            points.append((dx, dy))

    return points

def euclidean(p1, p2):
    """Calculates the euclidean distance between 2 points"""
    return sum(pow(c1 - c2, 2) for c1, c2 in zip(p1, p2))

def manhattan(p1, p2):
    """Calculates the manhattan distance between 2 points"""
    return sum(abs(c1 - c2) for c1, c2 in zip(p1, p2))

NORTH = (1, 0)
SOUTH = (-1, 0)
EAST = (0, 1)
WEST = (0, -1)
NE = (1,1)
NW = (1,-1)
SE = (-1,1)
SW = (-1,-1)

UP = (1, 0)
DOWN = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

NEIGHBOURS4 = (NORTH, SOUTH, EAST, WEST)
NEIGHBOURS8 = NEIGHBOURS4 + (NE, NW, SE, SW)