from utils import problem
from utils import preprocessing as ppr
from utils import ntheory as nt

problem = problem.Problem("2021/07: The Treachery of Whales")
problem.preprocessor = ppr.csi

@problem.solver()
def solve(ns):
    min_p, max_p = min(ns), max(ns)

    min_cost, min_cost2 = float("inf"), float("inf")
    for pos in range(min_p, max_p+1):
        cost, cost2 = 0, 0
        for n in ns:
            cost += abs(pos - n)
            cost2 += nt.triangular_number(max(n, pos) - min(n, pos))

        if cost > min_cost and cost2 > min_cost2: break

        min_cost = min(min_cost, cost)
        min_cost2 = min(min_cost2, cost2)

    return min_cost, min_cost2
        

if __name__ == "__main__":
    problem.solve()