from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2025/01: Secret Entrance")
problem.preprocessor = ppr.lsv

from collections import deque

DIRS = {'L': -1, 'R': 1}

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    dial = deque(range(100))
    dial.rotate(50)
    
    for v in inp:
        direction, amount = DIRS[v[0]], int(v[1:])
        for _ in range(amount):
            dial.rotate(direction)
            if dial[0] == 0:
                p2 += 1
        if dial[0] == 0:
            p1 += 1

    return p1, p2

if __name__ == "__main__":
    problem.solve()