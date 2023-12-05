from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/02: Corruption Checksum")
problem.preprocessor = ppr.int_grid

@problem.solver(part=1)
def part1(grid):
    return sum(max(row) - min(row) for row in grid)

@problem.solver(part=2)
def part2(grid):
    return sum([i//j for row in grid for i in row for j in row if i != j and not i % j])

if __name__ == "__main__":
    problem.solve()