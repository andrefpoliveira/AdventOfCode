from utils import problem
from utils import preprocessing as ppr
from itertools import accumulate, cycle

problem = problem.Problem("2018/01: Chronal Calibration")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(vs):
    return sum(vs)

@problem.solver(part=2)
def part2(vs):
    seen = {0}
    for v in accumulate(cycle(vs)):
        if v in seen: return v
        seen.add(v)


if __name__ == "__main__":
    problem.solve()