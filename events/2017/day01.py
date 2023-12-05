from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/01: Inverse Captcha")
problem.preprocessor = ppr.digits

@problem.solver(part=1)
def part1(ns):
    total = 0
    for i in range(1,len(ns)):
        if ns[i] == ns[i-1]: total += ns[i]
    if ns[0] == ns[-1]: total += ns[0]

    return total

@problem.solver(part=2)
def part2(ns):
    total = 0
    half = len(ns)//2
    for i in range(len(ns)):
        if i < half:
            if ns[i] == ns[i+half]: total += ns[i]
        else:
            if ns[i] == ns[i-half]: total += ns[i]
    return total

if __name__ == "__main__":
    problem.solve()