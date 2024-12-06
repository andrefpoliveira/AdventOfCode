from utils import problem
from utils import preprocessing as ppr

import numpy as np

problem = problem.Problem("2024/04: Ceres Search")
problem.preprocessor = ppr.grid

def match_matrix(matrix, pattern, x, y):
    rows, cols = pattern.shape
    if x + rows > matrix.shape[0] or y + cols > matrix.shape[1]:
        return False
    
    region = matrix[x:x+rows, y:y+cols]

    for i in range(rows):
        for j in range(cols):
            if pattern[i, j] != '.' and pattern[i, j] != region[i, j]:
                return False
            
    return True


def solver(grid, patterns):
    count = 0
    matrix = np.matrix(grid)
    for _ in range(4):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                for pattern in patterns:
                    count += match_matrix(matrix, pattern, c, r)

        matrix = np.rot90(matrix)

    return count
    

@problem.solver(part=1)
def part1(grid):
    patterns = [
        np.matrix(
            [['X', 'M', 'A', 'S']]
        ),
        np.matrix(
            [
                ['X', '.', '.', '.'],
                ['.', 'M', '.', '.'],
                ['.', '.', 'A', '.'],
                ['.', '.', '.', 'S'],
            ]
        )
    ]
    
    return solver(grid, patterns)


@problem.solver(part=2)
def part2(grid):
    patterns = [
        np.matrix(
            [
                ['M', '.', 'S'],
                ['.', 'A', '.'],
                ['M', '.', 'S'],
            ]
        ),
    ]
    
    return solver(grid, patterns)


if __name__ == "__main__":
    problem.solve()