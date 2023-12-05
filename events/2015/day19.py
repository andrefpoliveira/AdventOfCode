import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/19: Medicine for Rudolph")
problem.preprocessor = ppr.lsv

def part1(reactions, mol):
    s = set()
    for fr, t in reactions:
        matches = [(m.start(0), m.end(0)) for m in re.finditer(fr, mol)]

        for match in matches:

            new_s = mol[:match[0]] + t + mol[match[1]:]
            s.add(new_s)

    return len(s)

def part2(reactions, mol):
    count = 0
    while mol != "e":
        for fr, t in reactions:
            if t in mol:
                mol = mol.replace(t, fr, 1) 
                count += 1
    return count

@problem.solver()
def solve(ls):
    reactions = []
    for line in ls[:-2]:
        spl = line.strip().split(" => ")
        fr, t = spl[0], spl[1]
        reactions.append((fr, t))

    mol = ls[-1].strip() 

    return part1(reactions, mol), part2(reactions, mol)

if __name__ == "__main__":
    problem.solve()