from itertools import combinations
from functools import reduce
from operator import mul
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/24: It Hangs in the Balance")
problem.preprocessor = ppr.lsi

def quantum_ent(weights, parts):
    goal_weight = sum(weights)//parts

    for i in range(len(weights)):
        qua_ent = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == goal_weight]
        if len(qua_ent) > 0:
            return min(qua_ent)

@problem.solver()
def run(ns):
    return quantum_ent(ns, 3), quantum_ent(ns, 4)

if __name__ == "__main__":
    problem.solve()