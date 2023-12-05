from utils import problem
from utils import preprocessing as ppr

from math import ceil

problem = problem.Problem("2020/05: Binary Boarding")
problem.preprocessor = ppr.lsv

LETTERS = {"F": False, "B": True, "R": True, "L": False}

def calculate_spot(n, chars):
    min_v, max_v = 0, n - 1
    
    for c in chars:
        if LETTERS[c]:
            min_v = min_v + ceil((max_v - min_v) / 2)
        else:
            max_v = max_v - ceil((max_v - min_v) / 2)

    if max_v != min_v:
        raise ValueError("Ups")
    
    return max_v

@problem.solver(part=1)
def part1(ls):
    id = 0
    for l in ls:
        row = calculate_spot(128, l[:7])
        col = calculate_spot(8, l[7:])

        new_id = row * 8 + col
        id = max(new_id, id)

    return id

@problem.solver(part=2)
def part2(ls):
    seats = {}
    for l in ls:
        row = calculate_spot(128, l[:7])
        col = calculate_spot(8, l[7:])

        seats[row] = seats.get(row, []) + [col]

    skipping = True
    for row in sorted(seats.keys()):
        if not skipping and len(seats[row]) != 8:
            return row * 8 + list(set([x for x in range(8)]) - set(seats[row]))[0]

        if len(seats[row]) == 8: skipping = False

            
if __name__ == "__main__":
    problem.solve()