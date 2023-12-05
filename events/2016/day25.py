from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2016/25: Clock Signal")
problem.preprocessor = ppr.lsv

def get_value(value, v):
    return int(value) if value.isdigit() else v[value]

def solve(ls, v):
    idx = 0
    outs = []
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
        
        if inst[0] == "out":
            n = get_value(inst[1], v)
            print(n)
            if n < 0 or n > 1: return False
            if len(outs) % 2 != n: return False
            outs.append(n)

    if len(outs) == 4: return True

@problem.solver(part=1)
def part1(ls):
    n1 = re.findall(r"\d+", ls[1])[0]
    n2 = re.findall(r"\d+", ls[2])[0]
    base = int(n1) * int(n2)
    for a in range(1, 500):
        d = base + a
        if bin(d)[2:14] == "101010101010": return a

if __name__ == "__main__":
    problem.solve()