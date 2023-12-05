from utils import problem

problem = problem.Problem("2017/06: Memory Reallocation")
problem.preprocessor = lambda x: [int(i) for i in x.split()]

def allocate(ns, blocks, bank):
    size = len(ns)
    new_ns = [x for x in ns]
    new_ns[bank] = 0
    while blocks > 0:
        bank = (bank + 1) % size
        new_ns[bank] += 1
        blocks -= 1
    return new_ns

@problem.solver()
def solver(ns):
    seen, part1, state = [], 0, None
    while ns not in seen:
        seen.append(ns)
        blocks = max(ns)
        ns = allocate(ns, blocks, ns.index(blocks))
        part1 += 1

    state = ns
    blocks = max(ns)
    ns = allocate(ns, blocks, ns.index(blocks))
    part2 = 1

    while ns != state:
        blocks = max(ns)
        ns = allocate(ns, blocks, ns.index(blocks))
        part2 += 1
    
    return part1, part2

if __name__ == "__main__":
    problem.solve()