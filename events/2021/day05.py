import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/05: Hydrothermal Venture")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(ls):
    part1 = dict()
    part2 = dict()
    for l in ls:
        x1, y1, x2, y2 = [int(x) for x in re.findall(r"\d+", l)]

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    part1[(x, y)] = part1.get((x, y), 0) + 1
                    part2[(x, y)] = part2.get((x, y), 0) + 1
        else:
            dx = abs(x2 - x1)//(x2 - x1)
            dy = abs(y2 - y1)//(y2 - y1)

            while x1 != x2 + dx:
                part2[(x1, y1)] = part2.get((x1, y1), 0) + 1
                x1 += dx
                y1 += dy

    return sum(part1.get(x) > 1 for x in part1.keys()), sum(part2.get(x) > 1 for x in part2.keys())

if __name__ == "__main__":
    problem.solve()