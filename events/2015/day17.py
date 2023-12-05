from itertools import combinations
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/17: No Such Thing as Too Much")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(containers):
    total = 0
    for L in range(1, len(containers)+1):
        for c in combinations(containers, L):
            if sum(c) == 150: total += 1
    return total

@problem.solver(part=2)
def part2(containers):
    for L in range(1, len(containers)+1):
        total = 0
        for c in combinations(containers, L):
            if sum(c) == 150: total += 1
        if total > 0: return total
    return -1

if __name__ == "__main__":
    problem.solve()