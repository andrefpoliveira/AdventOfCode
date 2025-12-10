from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2025/09: Movie Theater")
problem.preprocessor = ppr.lsv

from shapely.geometry import Polygon

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    tiles = []

    for v in inp:
        tiles.append(tuple(map(int, v.split(','))))

    main_polygon = Polygon(tiles)

    for i, t1 in enumerate(tiles):
        for t2 in tiles[i+1:]:
            dx = abs(t1[0] - t2[0]) + 1
            dy = abs(t1[1] - t2[1]) + 1
            p1 = max(p1, dx * dy)

            polygon = Polygon([
                t1,
                (t1[0], t2[1]),
                t2,
                (t2[0], t1[1])
            ])

            if main_polygon.contains(polygon):
                p2 = max(p2, dx * dy)

    return p1, p2

if __name__ == "__main__":
    problem.solve()