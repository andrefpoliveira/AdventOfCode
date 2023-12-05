from utils import problem
from utils import preprocessing as ppr

from functools import cmp_to_key

problem = problem.Problem("2022/13: Distress Signal")
problem.preprocessor = ppr.lsv

def is_ordered(e1, e2):
    if type(e1) == int and type(e2) == int:
        if e1 == e2: return None
        return 1 if e1 > e2 else -1
    elif type(e1) == int and type(e2) == list:
        return is_ordered([e1], e2)
    elif type(e1) == list and type(e2) == int:
        return is_ordered(e1, [e2])
    else:
        for i in range(len(e1)):
            if i >= len(e2): return 1
            res = is_ordered(e1[i], e2[i])
            if res is not None: return res
        if len(e1) < len(e2): return -1
  
@problem.solver(part=1)
def part1(ls):
    count = 0
    for i in range(0, len(ls), 3):
        p1, p2 = eval(ls[i]), eval(ls[i+1])
        if is_ordered(p1, p2) < 0:
            count += (i // 3) + 1

    return count

@problem.solver(part=2)
def part2(ls):
    ls = [eval(l) for l in ls if l != ""] + [[[2]]] + [[[6]]]
    pairs = sorted(ls, key=cmp_to_key(is_ordered))
    return (1+pairs.index([[2]])) * (pairs.index([[6]])+1)

if __name__ == "__main__":
    problem.solve()