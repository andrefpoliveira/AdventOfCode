from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/20: Firewall Rules")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
    min_v = 0
    ls.sort(key = lambda x: int(x.split("-")[0]))

    for l in ls:
        ns = [int(x) for x in l.split("-")]
        if ns[0] <= min_v: min_v = max(min_v, ns[1]) + 1

    return min_v

@problem.solver(part=2)
def part2(ls):
    min_v, ips = 0, 0
    ls.sort(key = lambda x: int(x.split("-")[0]))

    for l in ls:
        ns = [int(x) for x in l.split("-")]

        if ns[0] > min_v:
            ips += ns[0] - min_v

        min_v = max(min_v, ns[1] + 1)
        
    ips += max(0, 4294967295 - min_v)

    return ips

if __name__ == "__main__":
    problem.solve()