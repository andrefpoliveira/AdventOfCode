from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/01: Sonar Sweep")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(ns):
    return sum([ns[i] > ns[i-1] for i in range(1, len(ns))])

@problem.solver(part=2)
def part2(ns):
    return sum([sum(ns[i-2:i+1]) > sum(ns[i-3:i]) for i in range(3, len(ns))])

if __name__ == "__main__":
    problem.solve()