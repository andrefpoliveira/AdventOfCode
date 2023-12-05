from utils import problem
from utils import preprocessing as ppr

from functools import cache

problem = problem.Problem("2020/10: Adapter Array")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(ns):
    built_in = max(ns) + 3
    ns = [0] + sorted(ns) + [built_in]

    _1 = _3 = 0
    for i in range(1, len(ns)):
        if ns[i] - ns[i-1] == 1: _1 += 1
        elif ns[i] - ns[i-1] == 3: _3 += 1

    return _1 * _3

@cache
def explore_arrangements(ns, pointer = 0):
    if pointer == len(ns) - 1:
        return 1
    
    count = 0
    v = ns[pointer]

    for i in range(pointer + 1, len(ns)):
        if pointer >= len(ns): break
        if ns[i] > v + 3: break
        
        count += explore_arrangements(ns, i)

    return count


@problem.solver(part=2)
def part2(ns):
    built_in = max(ns) + 3
    ns = [0] + sorted(ns) + [built_in]

    return explore_arrangements(tuple(ns))
 
if __name__ == "__main__":
    problem.solve()