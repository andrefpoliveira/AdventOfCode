from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2025/02: Gift Shop")
problem.preprocessor = lambda x: [map(int, v.split('-')) for v in ppr.csv(x)]

import re

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    for (minv, maxv) in inp:
        for v in range(minv, maxv + 1):
            if re.fullmatch(r'(.+)\1', str(v)):
                p1 += v

            if re.fullmatch(r'(.+)\1+', str(v)):
                p2 += v

    return p1, p2

if __name__ == "__main__":
    problem.solve()