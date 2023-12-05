from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/06: Lanternfish")
problem.preprocessor = ppr.csi

def lanterfishes(d, days):
    for _ in range(days):
        new_d = dict()
        for k in d.keys():
            if k == 0:
                new_d[6] = new_d.get(6, 0) + d[0]
                new_d[8] = d[0]
            else:
                new_d[k-1] = new_d.get(k-1, 0) + d[k]
        d = new_d
    return sum(d.values())

@problem.solver()
def solve(ns):
    d = dict()
    for n in ns: d[n] = d.get(n, 0) + 1
    return lanterfishes(d, 80), lanterfishes(d, 256)

if __name__ == "__main__":
    problem.solve()