from collections import defaultdict
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/24: Electromagnetic Moat")
problem.preprocessor = ppr.lsv

def parse_ports(ls):
    ports = defaultdict(set)
    for l in ls:
        a, b = [int(x) for x in l.split("/")]
        ports[a].add(b)
        ports[b].add(a)
    return ports

def gen(bridge, components):
    bridge = bridge or [(0, 0)]
    curr = bridge[-1][1]
    for b in components[curr]:
        if not ((curr, b) in bridge or (b, curr) in bridge):
            new = bridge + [(curr, b)]
            yield new
            yield from gen(new, components)

@problem.solver()
def solver(ls):
    ports = parse_ports(ls)

    part1 = 0
    part2 = 0
    size = 0

    for bridge in gen(None, ports):
        s = sum(a+b for a, b in bridge)
        part1 = max(part1, s)
        if len(bridge) > size or (len(bridge) == size and s > part2):
            size = len(bridge)
            part2 = s

    return part1, part2

if __name__ == "__main__":
    problem.solve()