from utils import problem
from utils import preprocessing as ppr

from functools import cache

problem = problem.Problem("2023/12: Hot Springs")
problem.preprocessor = ppr.lsv

def explore_combinations(line, multiplier = 1):
    spring, ns = line.split()
    spring = '?'.join([spring] * multiplier) + '.'
    ns = [int(n) for n in ns.split(',')] * multiplier

    @cache
    def _f(p, n):
        if p >= len(spring): return n == len(ns)

        r = (spring[p] in '.?') * _f(p+1, n)

        try:
            r += (spring[p] in '#?' and 
                '.' not in spring[p:p+ns[n]] and 
                '#' not in spring[p+ns[n]]) * _f(p+ns[n]+1, n+1)
        except IndexError:
            pass

        return r

    return _f(0, 0)

@problem.solver(part=1)
def part1(ls):
    part1 = 0
    for l in ls:
        part1 += explore_combinations(l)
    return part1

@problem.solver(part=2)
def part2(ls):
    part2 = 0
    for l in ls:
        part2 += explore_combinations(l, 5)
    return part2

if __name__ == "__main__":
    problem.solve()