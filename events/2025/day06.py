from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2025/06: Trash Compactor")
problem.preprocessor = lambda x: x.split('\n')

import re
from functools import reduce

def resolve_column(column, part=1):
    if part == 1:
        return [int(x.strip()) for x in column]
    else:
        col_values = []
        for col in range(len(column[0])):
            v = ""
            for row in range(len(column)):
                if column[row][col].isdigit():
                    v += column[row][col]
            col_values.append(int(v))

        return col_values

@problem.solver()
def solver(inp):
    p1 = p2 = 0
    actions = { '+': lambda x, y: x + y, '*': lambda x, y: x * y }

    ap = [x.start() for x in re.finditer(r'[\+\*]', inp[-1])]
    ranges = [(ap[i-1], ap[i]-1) for i in range(1, len(ap))] + [(ap[-1], len(inp[-1]))]

    values = [[line[_range[0]:_range[1]] for line in inp[:-1]] for _range in ranges]

    for col, _range in enumerate(ranges):
        action = inp[-1][_range[0]:_range[1]].strip()
        column = values[col]

        resolved = resolve_column(column)
        p1 += reduce(actions[action], resolved)

        resolved = resolve_column(column, part=2)
        p2 += reduce(actions[action], resolved)

    return p1, p2

if __name__ == "__main__":
    problem.solve()