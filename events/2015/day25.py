import re
from utils import problem

problem = problem.Problem("2015/25: Let It Snow")
problem.preprocessor = lambda x: list(map(int, re.findall(r"\d+", x)))

@problem.solver()
def solve(ns):
    row, col = ns
    value = 31916031
    current_row, current_col = 1, 2
    max_row = 3

    while row != current_row or col != current_col:
        value = (value * 252533) % 33554393

        current_row -= 1
        current_col += 1

        if current_row == 0:
            current_row = max_row
            current_col = 1
            max_row += 1

    return (value * 252533) % 33554393, None

if __name__ == "__main__":
    problem.solve()