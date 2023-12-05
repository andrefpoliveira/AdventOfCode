from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/14: Chocolate Charts")
problem.preprocessor = ppr.I

@problem.solver()
def part1(s):
    v = int(s)
    scores = "37"
    elf1, elf2 = 0, 1

    while s not in scores[-7:]:
        sc1, sc2 = int(scores[elf1]), int(scores[elf2])

        total = int(scores[elf1]) + int(scores[elf2])
        scores += str(total)

        elf1 = (elf1 + sc1 + 1) % len(scores)
        elf2 = (elf2 + sc2 + 1) % len(scores)

    return scores[v : v + 10], scores.find(s)

if __name__ == "__main__":
    problem.solve()