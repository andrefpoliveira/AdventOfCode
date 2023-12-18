from utils import problem
from utils import preprocessing as ppr

import re
from shapely.geometry import Polygon
from shapely.geometry import JOIN_STYLE

problem = problem.Problem("2023/18: Lavaduct Lagoon")
problem.preprocessor = ppr.lsv

DIRS = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
HEX_TO_DIR = {"0": "R", "1": "D", "2": "L", "3": "U"}

@problem.solver(part=1)
def part1(ls):
    x, y = 0, 0
    points = []

    for l in ls:
        dir, dist, color = re.findall(r"([RLUD]) (\d+) \((.+)\)", l)[0]
        x += int(dist) * DIRS[dir][0]
        y += int(dist) * DIRS[dir][1]
        points.append((x, y))

    return Polygon(points).buffer(0.5, join_style=JOIN_STYLE.mitre).area

@problem.solver(part=2)
def part2(ls):
    x, y = 0, 0
    points = [(0, 0)]

    for l in ls:
        color = re.findall(r"\((.+)\)", l)[0][1:]

        dist = int(color[:-1], 16)
        x += dist * DIRS[HEX_TO_DIR[color[-1]]][0]
        y += dist * DIRS[HEX_TO_DIR[color[-1]]][1]
        
        points.append((x, y))

    return Polygon(points).buffer(0.5, join_style=JOIN_STYLE.mitre).area

if __name__ == "__main__":
    problem.solve()