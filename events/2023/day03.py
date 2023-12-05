from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo

import re
from functools import reduce

problem = problem.Problem("2023/03: Gear Ratios")
problem.preprocessor = ppr.I

def get_row_col(c, l):
    c -= c // l
    return c // l, c % l

@problem.solver()
def solver(s):
    part1 = part2 = 0

    l = len(s.split()[0])
    gears = {}

    ns = re.finditer(r"(\d+)", s)
    symbols = re.finditer(r"([^\d\.\n])", s)

    for s in symbols:
        row, col = get_row_col(s.start(), l)
        gears[(row, col)] = {"valid": s.groups()[0] == "*", "parts": set()}

    for n in ns:
        number = int(n.groups()[0])
        begin, end = n.start(), n.end()

        found = False
        for i in range(begin, end):
            row, col = get_row_col(i, l)
            for dx, dy in geo.NEIGHBOURS8:
                cx, cy = col + dx, row + dy
                if (cy, cx) in gears.keys():
                    gears[(cy, cx)]["parts"].add(number)
                    found = True
        
        if found:
            part1 += number

    for v in gears.values():
        if v["valid"] and len(v["parts"]) == 2:
            part2 += reduce(lambda x, y: x * y, list(v["parts"]))

    return part1, part2

if __name__ == "__main__":
    problem.solve()