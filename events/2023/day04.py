from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2023/04: Scratchcards")
problem.preprocessor = ppr.lsv

@problem.solver()
def solver(ls):
    part1 = 0
    part2 = [1 for _ in range(len(ls))]

    for id, l in enumerate(ls):
        scratches = part2[id]

        ns = l.split(":")[1]
        winning_ns, my_ns = [set(x.split()) for x in ns.split("|")]
        common = winning_ns.intersection(my_ns)

        if len(common) > 0:
            part1 += 2 ** (len(common) - 1)

            for i in range(len(common)):
                if i + id + 1 < len(ls):
                    part2[i + id + 1] += scratches

    return part1, sum(part2)

if __name__ == "__main__":
    problem.solve()