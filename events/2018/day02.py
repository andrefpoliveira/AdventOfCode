from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/02: Inventory Management System")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
    two_count, three_count = 0, 0
    for l in ls:
        letters = set(l)
        if any(map(lambda x: l.count(x) == 2, letters)): two_count += 1
        if any(map(lambda x: l.count(x) == 3, letters)): three_count += 1

    return two_count * three_count

@problem.solver(part=2)
def part2(ls):
    best_diff, options = float("Inf"), None

    for i in range(len(ls)):
        l1 = ls[i]
        for j in range(i + 1, len(ls)):
            l2 = ls[j]

            diff = sum(l1[i] != l2[i] for i in range(len(l1)))

            if diff < best_diff:
                best_diff = diff
                options = [l1, l2]

    w1, w2 = options
    return ''.join([w1[i] for i in range(len(w1)) if w1[i] == w2[i]])  

if __name__ == "__main__":
    problem.solve()