from utils import problem
from utils import preprocessing as ppr

import numpy as np

problem = problem.Problem("2017/21: Fractal Art")
problem.preprocessor = ppr.lsv

pattern = np.array([
        [".", "#", "."],
        [".", ".", "#"],
        ["#", "#", "#"],
    ])

def get_rotations_flips(square: np.array):
    for i in range(0, 4):
        yield np.rot90(square, i)
    flipped = np.flip(square, 0)
    for i in range(0, 4):
        yield np.rot90(flipped, i)

def board_to_str(square):
    return '/'.join(''.join(r) for r in square)

def str_to_board(string):
    return np.array([[x for x in r] for r in string.split("/")])

def get_rules(ls):
    d = {}
    for l in ls:
        k, v = l.strip().split(" => ")
        d[k] = v
    return d

def transform_square(small_square, d):
    for square in get_rotations_flips(small_square):
        s = board_to_str(square)
        try:
            return str_to_board(d[s])
        except: pass
    raise ValueError("No value found")

def enhance(square, size, d):
    new_square = None
    for i in range(0, len(square), size):

        new_line = None
        for j in range(0, len(square), size):

            small_square = square[i:i+size,j:j+size]
            temp_square = transform_square(small_square, d)

            if new_line is None:
                new_line = temp_square
            else:
                new_line = np.concatenate([new_line, temp_square], axis=1)
        
        if new_square is None:
            new_square = new_line
        else:
            new_square = np.concatenate([new_square, new_line], axis=0)
    return new_square

def solver(ls, iterations):
    global pattern
    square = pattern.copy()

    d = get_rules(ls)

    for _ in range(iterations):
        if len(square) % 2 == 0:
            new_square = enhance(square, 2, d)

        elif len(square) % 3 == 0:
            new_square = enhance(square, 3, d)

        square = new_square
    return np.count_nonzero(square == "#")

@problem.solver(part=1)
def part1(ls):
    return solver(ls, 5)

@problem.solver(part=2)
def part2(ls):
    return solver(ls, 18)

if __name__ == "__main__":
    problem.solve()