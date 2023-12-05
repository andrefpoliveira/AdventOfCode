from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/11: Hex Ed")
problem.preprocessor = ppr.csv

@problem.solver()
def solver(vs):
    x, y = 0, 0
    part2 = 0

    dir = {"n": (0,2), "s": (0,-2), "ne": (1,1), "nw": (1,-1), "se": (-1,1), "sw": (-1,-1)}
    for v in vs:
        dx, dy = dir[v]
        x += dx
        y += dy

        part2 = max(part2, (abs(x) + abs(y))//2)

    return (abs(x) + abs(y))//2, part2

if __name__ == "__main__":
    problem.solve()