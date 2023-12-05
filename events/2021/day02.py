from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/02: Dive!")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(ls):
    h, d1, d2, aim = 0, 0, 0, 0
    for l in ls:
        value = int(l.split(" ")[1])
        if "forward" in l:
            h += value
            d2 += value*aim
        elif "down" in l:
            d1 += value
            aim += value
        else:
            d1 -= value
            aim -= value
    return h*d1, h*d2

if __name__ == "__main__":
    problem.solve()