from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/01: Report Repair")
problem.preprocessor = ppr.lsi

@problem.solver(part=1)
def part1(ns):
    numbers = set()
    for n in ns:
        if 2020 - n in numbers: return n * (2020 - n)
        numbers.add(n)

@problem.solver(part=2)
def part2(ns):
    ns.sort()

    for i in range(len(ns)):
        l = i + 1
        r = len(ns) - 1

        while (l < r):
            if ns[i] + ns[l] + ns[r] == 2020:
                return ns[i] * ns[l] * ns[r]
            elif ns[i] + ns[l] + ns[r] > 2020:
                r -= 1
            else:
                l += 1
            

if __name__ == "__main__":
    problem.solve()