from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/05: A Maze of Twisty Trampolines, All Alike")
problem.preprocessor = ppr.lsi

def solve(ns, part2 = False):
    idx = 0
    steps = 0
    while idx < len(ns):
        v = ns[idx]
        if ns[idx] >= 3 and part2:
            ns[idx] -= 1
        else:
            ns[idx] += 1
        idx += v
        steps += 1
    return steps

@problem.solver(part=1)
def part1(ns):
    return solve(ns)
    
@problem.solver(part=2)
def part2(ns):
    return solve(ns, True)

if __name__ == "__main__":
    problem.solve()