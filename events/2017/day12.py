from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2017/12: Digital Plumber")
problem.preprocessor = ppr.lsv

d = dict()

def generate_dict(ls):
    temp = dict()
    for l in ls:
        ns = [int(x) for x in re.findall(r'\d+', l)]
        temp[ns[0]] = list(set(temp.get(ns[0], []) + ns[1:]))
        for i in ns[1:]:
            temp[i] = list(set(temp.get(i, []) + [ns[0]]))

    for k in temp:
        d[k] = {"v": False, "pipes": temp[k]}

def search_connections(start, part2 = False):
    queue = [start]
    seen = [start]
    while queue:
        current = queue.pop(0)

        if part2: d[current]["v"] = True

        for n in d[current]["pipes"]:
            if n not in seen:
                queue.append(n)
                seen.append(n)
    return len(seen)

@problem.solver(part=1)
def part1(ls):
    global d
    generate_dict(ls)
    return search_connections(0)

@problem.solver(part=2)
def part2(ls):
    global d
    groups = 0
    for k in d:
        if not d[k]["v"]:
            groups += 1
            search_connections(k, True)

    return groups

if __name__ == "__main__":
    problem.solve()