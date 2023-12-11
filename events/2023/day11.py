from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo

import numpy as np
from itertools import combinations

problem = problem.Problem("2023/11: Cosmic Expansion")
problem.preprocessor = ppr.grid

def get_galaxies(grid, factor = 2):
    empty_rows = [id for id, row in enumerate(grid) if row[0] == "." and len(set(row)) == 1]
    empty_cols = [id for id, row in enumerate(np.transpose(grid)) if row[0] == "." and len(set(row)) == 1]

    galaxies = []

    for y, row in enumerate(grid):
        n_empty_rows = len([i for i in empty_rows if i < y])

        for x, cell in enumerate(row):
            n_empty_cols = len([i for i in empty_cols if i < x])

            if cell == "#":
                galaxies.append((x + (factor - 1) * n_empty_cols, y + (factor - 1) * n_empty_rows))

    return galaxies

@problem.solver(part=1)
def part1(grid):
    galaxies = get_galaxies(grid)
    combs = list(combinations(galaxies, 2))
    return sum([geo.manhattan(c1, c2) for c1, c2 in combs])

@problem.solver(part=2)
def part2(grid):
    galaxies = get_galaxies(grid, 1000000)
    combs = list(combinations(galaxies, 2))
    return sum([geo.manhattan(c1, c2) for c1, c2 in combs])

if __name__ == "__main__":
    problem.solve()