from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/10: The Stars Align")
problem.preprocessor = ppr.lsv

def calculate_score(points):
    copy = [p for p in points]
    pieces = 0

    while copy:
        pieces += 1
        queue = [copy.pop()]

        while queue:
            p, i = queue.pop(), 0
            while i < len(copy):
                if abs(p[0] - copy[i][0]) + abs(p[1] - copy[i][1]) <= 1:
                    queue.append(copy.pop(i))
                else:
                    i += 1
                    
    return pieces

def get_distance(points):
    y = [p[1] for p in points]

    min_y, max_y = min(y), max(y)
    return max_y - min_y

def print_message(points):
    ps = [(p[0], p[1]) for p in points]
    x = [p[0] for p in ps]
    y = [p[1] for p in ps]

    min_y, max_y, min_x, max_x = min(y), max(y), min(x), max(x)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if (x, y) in ps else " ", end="")
        print()

@problem.solver(part=2)
def part1(ls):
    points = []
    for l in ls:
        x, y, dx, dy = map(int, re.findall(r"-?\d+", l))
        points.append((x, y, dx, dy))

    turns = 0

    while True:
        y_diff = get_distance(points)

        mult = y_diff // 10
        if mult < 1: mult = 1
        turns += mult

        for i, (x, y, dx, dy) in enumerate(points):
            points[i] = (x + dx * mult, y + dy * mult, dx, dy)

        if calculate_score(points) < len(points) // 10:
            break

    print_message(points)
    return turns

if __name__ == "__main__":
    problem.solve()