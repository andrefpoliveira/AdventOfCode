from utils import problem
from utils import preprocessing as ppr

from functools import reduce

problem = problem.Problem("2020/03: Toboggan Trajectory")
problem.preprocessor = ppr.grid

def get_hits(grid, dir):
    pos = (0, 0)

    hits = 0
    while pos[1] < len(grid):
        if grid[pos[1]][pos[0] % len(grid[0])] == "#":
            hits += 1

        pos = (pos[0] + dir[0], pos[1] + dir[1])
    
    return hits

@problem.solver(part=1)
def part1(grid):
    return get_hits(grid, (3, 1))

@problem.solver(part=2)
def part2(grid):
    dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(lambda x, y: x * y, [get_hits(grid, dir) for dir in dirs])
            
if __name__ == "__main__":
    problem.solve()