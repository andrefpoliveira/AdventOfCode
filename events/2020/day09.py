from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/09: Handheld Halting")
problem.preprocessor = ppr.lsi

CONSIDERED_VALUES = 25

def sum_is_possible(ns, target):
    s = set()
    for n in ns:
        if target - n in s: return True
        s.add(n)
    return False

def _part1(ns):
    vs = ns[:CONSIDERED_VALUES]
    pointer = CONSIDERED_VALUES

    while sum_is_possible(vs, ns[pointer]):
        pointer += 1
        vs = ns[pointer - CONSIDERED_VALUES: pointer]

    return ns[pointer]

@problem.solver()
def solver(ns):
    part1 = _part1(ns)

    min_p, max_p = 0, 1

    while True:
        _ns = ns[min_p: max_p + 1]
        v = sum(_ns)
        if v == part1:
            return part1, max(_ns) + min(_ns)
        
        elif v > part1:
            min_p += 1
        else:
            max_p += 1
 
if __name__ == "__main__":
    problem.solve()