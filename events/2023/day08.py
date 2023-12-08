from utils import problem
from utils import preprocessing as ppr
from utils import ntheory as nt

import re

problem = problem.Problem("2023/08: Haunted Wasteland")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
    instructions = ls[0]
    pos = "AAA"
    m = {}

    for l in ls[2:]:
        nodes = re.findall(r"(\w+) = \((\w+), (\w+)\)", l)[0]
        m[nodes[0]] = (nodes[1], nodes[2])

    steps = 0
    while pos != "ZZZ":
        inst = 0 if instructions[steps % len(instructions)] == "L" else 1
        pos = m[pos][inst]
        steps += 1

    return steps

@problem.solver(part=2)
def part2(ls):
    instructions = ls[0]
    pos = []
    m = {}

    for l in ls[2:]:
        nodes = re.findall(r"(\w+) = \((\w+), (\w+)\)", l)[0]
        m[nodes[0]] = (nodes[1], nodes[2])
        if nodes[0][-1] == "A":
            pos.append(nodes[0])

    cycles = []
    for p in pos:
        steps = 0
        d = {}
        while p[-1] != "Z" or p not in d:
            d[p] = steps
            inst = 0 if instructions[steps % len(instructions)] == "L" else 1
            p = m[p][inst]
            steps += 1
        
        cycles.append(steps - d[p])
    
    return nt.lcm(cycles)

if __name__ == "__main__":
    problem.solve()