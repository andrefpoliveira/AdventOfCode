from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2022/04: Camp Cleanup")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
    count = 0
    for l in ls:
        b1, e1, b2, e2 = [int(x) for x in re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', l)[0]]
        if (b1 - b2) * (e1 - e2) <= 0: count += 1
    return count

@problem.solver(part=2)
def part2(ls):
    count = 0
    for l in ls:
        b1, e1, b2, e2 = [int(x) for x in re.findall(r'(\d+)-(\d+),(\d+)-(\d+)', l)[0]]
        if (e2 - b1) * (b2 - e1) <= 0: count += 1
    return count

if __name__ == "__main__":
    problem.solve()