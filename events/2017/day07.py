from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2017/07: Recursive Circus")
problem.preprocessor = ppr.lsv

d = dict()
root = None

def generate_d(ls):
    for l in ls:
        new_d = dict()
        parsed = re.findall(r'([a-z0-9]+)', l)
        new_d["weight"] = int(parsed[1])
        new_d["progrs"] = parsed[2:]
        d[parsed[0]] = new_d
    
@problem.solver(part=1)
def part1(ls):
    global root
    generate_d(ls)
    inside = set()
    total = set()
    for k in d:
        total.add(k)
        inside |= set(d.get(k).get("progrs"))
    root = list(total.difference(inside))[0]
    return root

def find_unbalanced(root):
    w = d.get(root).get("weight")
    progrs = d.get(root).get("progrs")
    if len(progrs) == 0: return w, None
    
    ws = []
    for prog in progrs:
        weight, found = find_unbalanced(prog)
        if found != None: return None, found
        ws.append(weight)

    if len(set(ws)) == 1: return w + sum(ws), None
    sorted_l = sorted(ws, key=lambda x: ws.count(x))
    
    p = progrs[ws.index(sorted_l[0])]

    return None, d.get(p).get("weight") - abs(sorted_l[0] - sorted_l[1])

@problem.solver(part=2)
def part2(ls):
    global root
    return find_unbalanced(root)[1]

if __name__ == "__main__":
    problem.solve()