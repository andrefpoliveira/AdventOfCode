from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/12: Leonardo's Monorail")
problem.preprocessor = ppr.lsv

def get_value(value, v):
    return int(value) if value.isdigit() else v[value]

def solve(ls, v):
    idx = 0
    while idx < len(ls):
        inst = ls[idx].split(" ")
        if inst[0] == "cpy":
            v[inst[2]] = get_value(inst[1], v)
            idx += 1

        if inst[0] == "inc":
            v[inst[1]] += 1
            idx += 1

        if inst[0] == "dec":
            v[inst[1]] -= 1
            idx += 1

        if inst[0] == "jnz":
            if get_value(inst[1], v) != 0:
                idx += int(inst[2])
            else:
                idx += 1
    return v['a']

@problem.solver(part=1)
def part1(ls):
    return solve(ls, {'a': 0, 'b': 0, 'c': 0, 'd': 0})

@problem.solver(part=2)
def part2(ls):
    return solve(ls, {'a': 0, 'b': 0, 'c': 1, 'd': 0})

if __name__ == "__main__":
    problem.solve()