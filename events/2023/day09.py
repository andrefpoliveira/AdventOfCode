from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2023/09: Mirage Maintenance")
problem.preprocessor = ppr.lsv

def get_history(ns):
    part1 = part2 = 0
    history = []
    while ns[0] != 0 or len(set(ns)) != 1:
        history.append(ns)
        ns = [ns[i] - ns[i-1] for i in range(1, len(ns))]
    
    for ns in reversed(history):
        part1 = ns[-1] + part1
        part2 = ns[0] - part2

    return part1, part2

@problem.solver()
def solver(ls):
    part1 = part2 = 0
    for l in ls:
        ns = [int(n) for n in l.split()]
        p1, p2 = get_history(ns)
        part1, part2 = part1 + p1, part2 + p2
    return part1, part2

if __name__ == "__main__":
    problem.solve()