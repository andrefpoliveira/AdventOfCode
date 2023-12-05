import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/08: Two-Factor Authentication")
problem.preprocessor = ppr.lsv
width, height = 50, 6

def part2(grid):
    for row in grid:
        print(''.join([".", "#"][x] for x in row))
    print()

@problem.solver()
def part1(ls):
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for l in ls:
        n1, n2 = [int(n) for n in re.findall(r"\d+", l)]

        if "rect" in l:
            for row in range(n2):
                for col in range(n1):
                    grid[row][col] = 1
        else:
            copy_grid = [[x for x in row] for row in grid]
            if "column" in l:
                for row in copy_grid: row[n1] = 0

                for id, row in enumerate(grid):
                    if row[n1] == 1:
                        new_row = (id + n2) % height
                        copy_grid[new_row][n1] = 1

            else:
                copy_grid[n1] = [0 for _ in range(width)]

                for id, v in enumerate(grid[n1]):
                    if v == 1:
                        new_col = (id + n2) % width
                        copy_grid[n1][new_col] = 1

            grid = copy_grid


    part2(grid)
    return sum([x for row in grid for x in row])


if __name__ == "__main__":
    problem.solve()