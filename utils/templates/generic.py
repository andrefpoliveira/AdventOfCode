from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2015/01: ???")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    for v in inp:
        print(v)

    return (0, 0)

if __name__ == "__main__":
    problem.solve()