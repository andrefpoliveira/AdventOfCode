import math
from functools import reduce
from itertools import permutations
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/18: Snailfish")
problem.preprocessor = lambda x: [eval(r) for r in x.split("\n")]

def add_left(x, value):
    if value == None: return x
    if type(x) == int:
        return x + value
    return [add_left(x[0], value), x[1]]

def add_right(x, value):
    if value == None: return x
    if type(x) == int:
        return x + value
    return [x[0], add_right(x[1], value)]

def explode(x, depth = 0):
    if type(x) == int: return False, None, x, None
    if depth == 4: return True, x[0], 0, x[1]
    a, b = x
    explodes, l, a, r = explode(a, depth + 1)
    if explodes: return True, l, [a, add_left(b, r)], None

    explodes, l, b, r = explode(b, depth + 1)
    if explodes: return True, None, [add_right(a, l), b], r

    return False, None, x, None

def split(x):
    if type(x) == int:
        if x >= 10: return True, [x//2, math.ceil(x/2)]
        return False, x
    a,b = x
    change, a = split(a)
    if change: return True, [a,b]
    change, b = split(b)
    return change, [a, b]

def add(x, y):
    l = [x, y]
    while True:
        change, _, l, _ = explode(l)
        if change: 
            continue
        change, l = split(l)
        if not change: break
    return l

def magnitude(x):
    if type(x) == int:
        return x
    else:
        return 3 * magnitude(x[0]) + 2 * magnitude(x[1])        

@problem.solver(part=1)
def part1(ls):
    return magnitude(reduce(add, ls))

@problem.solver(part=2)
def part2(ls):
    return max(magnitude(add(x, y)) for x, y in permutations(ls, 2))


if __name__ == "__main__":
    problem.solve()