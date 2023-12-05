from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/16: Permutation Promenade")
problem.preprocessor = ppr.csv

def apply_rules(progs, vs):
    for v in vs:
        if v[0] == 'p':
            idx_a = progs.index(v[1])
            idx_b = progs.index(v[3])
            progs[idx_a], progs[idx_b] = progs[idx_b], progs[idx_a]
        elif v[0] == 'x':
            a, b = map(int, v[1:].split("/"))
            progs[a], progs[b] = progs[b], progs[a]
        else:
            n = int(v[1:])
            progs = progs[-n:] + progs[:-n]
    return progs

@problem.solver(part=1)
def part1(vs):
    progs = [x for x in 'abcdefghijklmnop']

    return ''.join(apply_rules(progs, vs))

@problem.solver(part=2)
def part2(vs):
    progs = [x for x in 'abcdefghijklmnop']
    copy = [x for x in 'abcdefghijklmnop']

    repeats = 0
    for i in range(1000000000):
        if i != 0 and copy == progs:
            repeats = i
            break
        progs = apply_rules(progs, vs)
    
    for i in range(1000000000 % repeats):
        progs = apply_rules(progs, vs)

    return ''.join(progs)

if __name__ == "__main__":
    problem.solve()