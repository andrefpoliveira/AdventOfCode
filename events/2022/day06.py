from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/06: Tuning Trouble")
problem.preprocessor = ppr.I

def solver(s, size):
    for i in range(len(s)):
        if len(set(s[i:i+size])) == size:
            return i + size

@problem.solver(part=1)
def part1(s):
    return solver(s, 4)

@problem.solver(part=2)
def part2(s):
    return solver(s, 14)

if __name__ == "__main__":
    problem.solve()