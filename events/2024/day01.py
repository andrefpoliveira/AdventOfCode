from utils import problem
from utils import preprocessing as ppr

from collections import Counter

problem = problem.Problem("2024/01: Historian Hysteria")
problem.preprocessor = ppr.lsv


def get_lists(ls):
    l1, l2 = [], []

    for l in ls:
        ns = [int(x) for x in l.split()]
        l1.append(ns[0])
        l2.append(ns[1])

    l1.sort()
    l2.sort()

    return l1, l2


@problem.solver(part=1)
def part1(ls):
    l1, l2 = get_lists(ls)
    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))


@problem.solver(part=2)
def part2(ls):
    l1, l2 = get_lists(ls)

    c1, c2 = Counter(l1), Counter(l2)

    return sum(k * c1[k] * c2.get(k, 0) for k, v in c1.items())


if __name__ == "__main__":
    problem.solve()