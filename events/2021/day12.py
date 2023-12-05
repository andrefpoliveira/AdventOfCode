from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/12: Passage Pathing")
problem.preprocessor = ppr.lsv

d = {}

def create_graph(ls):
    d = dict()
    for l in ls:
        fr, to = l.split("-")
        if "start" in l:
            arr = d.get("start", [])
            arr.append(to if to != "start" else fr)
            d["start"] = arr
        elif "end" in l:
            n = to if to != "end" else fr
            arr = d.get(n, [])
            arr.append("end")
            d[n] = arr
        else:
            arr = d.get(fr, [])
            arr.append(to)
            d[fr] = arr
            arr = d.get(to, [])
            arr.append(fr)
            d[to] = arr
    return d

def dfsUtil(s, e, visited, path, d):
    count = 0
    visited[s] = True
    path.append(s)

    if s == e:
        count += 1
    else:
        for dest in d[s]:
            if dest.lower() != dest or not visited[dest]:
                count += dfsUtil(dest, e, visited, path, d)

    path.pop()
    visited[s] = False
    return count

def dfsUtil2(s, e, visited, path, d):
    count = 0
    visited[s] += 1
    path.append(s)

    if s == e:
        count += 1
    else:
        for dest in d[s]:
            if dest.lower() != dest or (not any(path.count(x) >= 2 for x in set(path) if x.lower() == x) or visited[dest] < 1):
                count += dfsUtil2(dest, e, visited, path, d)

    path.pop()
    visited[s] -= 1
    return count

@problem.solver(part=1)
def part1(ls):
    global d
    d = create_graph(ls)
    visited = {k: False for k in d.keys()}
    visited["end"] = False
    return dfsUtil("start", "end", visited, [], d)

@problem.solver(part=2)
def part2(ls):
    visited = {k: 0 for k in d.keys()}
    visited["end"] = 0
    return dfsUtil2("start", "end", visited, [], d)

if __name__ == "__main__":
    problem.solve()