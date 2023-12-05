from utils import problem
from utils import preprocessing as ppr

import math, re

problem = problem.Problem("2016/23: Safe Cracking")
problem.preprocessor = ppr.lsv

def get_value(value, v):
    try:
        return int(value)
    except:
        return v[value]

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
                idx += get_value(inst[2], v)
            else:
                idx += 1

        if inst[0] == "tgl":
            target_idx = get_value(inst[1], v) + idx
            if target_idx >= len(ls):
                idx += 1
                continue
            target_inst = ls[target_idx]
            if target_inst.count(" ") == 1:
                if "inc" in target_inst: ls[target_idx] = "dec" + target_inst[3:]
                else: ls[target_idx] = "inc" + target_inst[3:]
            else:
                if "jnz" in target_inst: ls[target_idx] = "cpy" + target_inst[3:]
                else: ls[target_idx] = "jnz" + target_inst[3:]
            idx += 1

    return v['a']

@problem.solver(part=1)
def part1(ls):
    return solve(ls, {'a': 7})

@problem.solver(part=2)
def part2(ls):
    n1 = re.findall(r'\d+', ls[19])[0]
    n2 = re.findall(r'\d+', ls[20])[0]
    return math.factorial(12) + int(n1) * int(n2)


if __name__ == "__main__":
    problem.solve()