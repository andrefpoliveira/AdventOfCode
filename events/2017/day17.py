from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/17: Spinlock")
problem.preprocessor = ppr.intI

@problem.solver(part=1)
def part1(n):
    ns = [0]
    idx = 0
    for i in range(1,2018):
        idx = (idx + n) % len(ns) + 1
        ns.insert(idx, i)
    return ns[ns.index(2017)+1]

@problem.solver(part=2)
def part2(n):
    v, idx = 0, 0
    for i in range(1,50000001):
        idx = (idx + n) % i + 1
        if idx == 1: v = i
    return v

if __name__ == "__main__":
    problem.solve()