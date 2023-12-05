from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/08: Memory Maneuver")
problem.preprocessor = ppr.ssi

@problem.solver(part=1)
def part1(ns):
    total = 0

    child_nodes, meta_entries, *ns = ns
    if child_nodes == 0:
        total += sum(ns[:meta_entries])
        ns = ns[meta_entries:]
        return total, ns
    else:
        for _ in range(child_nodes):
            t, ns = part1(ns)
            total += t
        total += sum(ns[:meta_entries])
        ns = ns[meta_entries:]
        
    return (total, ns) if ns else total


@problem.solver(part=2)
def part2(ns):
    total = 0

    child_nodes, meta_entries, *ns = ns
    if child_nodes == 0:
        total += sum(ns[:meta_entries])
        ns = ns[meta_entries:]
        return total, ns
    else:
        totals = []
        for _ in range(child_nodes):
            t, ns = part2(ns)
            totals.append(t)

        meta = ns[:meta_entries]
        for n in meta:
            if 0 < n <= len(totals):
                total += totals[n-1]

        ns = ns[meta_entries:]
        
    return (total, ns) if ns else total

if __name__ == "__main__":
    problem.solve()