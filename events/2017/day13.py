from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/13: Packet Scanners")
problem.preprocessor = lambda ls: {int(l.split(": ")[0]): int(l.split(": ")[1]) for l in ls.strip().split("\n")}

def pass_firewall(d, delay = 0):
    sev, escaped = 0, True
    for i in range(max(d.keys())+1):
        if i not in d: continue
        size = d[i]
        if (i + delay) % (size + size - 2) == 0:
            sev += i * size
            if delay != 0:
                return -1, False
    return sev, escaped

@problem.solver(part=1)
def part1(d):
    return pass_firewall(d)[0]

@problem.solver(part=2)
def part2(d):
    escaped = False
    delay = 0
    while not escaped:
        delay += 1
        escaped = pass_firewall(d, delay)[1]
    return delay

if __name__ == "__main__":
    problem.solve()