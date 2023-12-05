import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/06: Probably a Fire Hazard")
problem.preprocessor = ppr.lsv

@problem.solver()
def solve(input_text):
    grid1 = [[0 for _ in range(1000)] for _ in range(1000)]
    grid2 = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in input_text:
        r = [int(x) for x in re.findall(r'\d+', line)]

        if "on" in line:
            for i in range(r[0], r[2]+1):
                for j in range(r[1], r[3]+1):
                    grid1[i][j] = 1
                    grid2[i][j] += 1
        elif "off" in line:
            for i in range(r[0], r[2]+1):
                for j in range(r[1], r[3]+1):
                    grid1[i][j] = 0
                    grid2[i][j] -= 1 if grid2[i][j] != 0 else 0
        else:
            for i in range(r[0], r[2]+1):
                for j in range(r[1], r[3]+1):
                    grid1[i][j] = 1 if grid1[i][j] == 0 else 0
                    grid2[i][j] += 2

    return sum([x.count(1) for x in grid1]), sum([sum(x) for x in grid2])

if __name__ == "__main__":
    problem.solve()