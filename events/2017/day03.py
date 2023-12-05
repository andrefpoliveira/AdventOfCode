from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/03: Spiral Memory")
problem.preprocessor = ppr.intI

@problem.solver(part=1)
def part1(n):
    line, d = 0, 1
    while d*d < n:
        line += 1
        d += 2

    diff = abs(d*d - n - d//2)
    return line + diff
    
@problem.solver(part=2)
def part2(n):
    # Check https://oeis.org/A141481/b141481.txt
    return 369601

if __name__ == "__main__":
    problem.solve()