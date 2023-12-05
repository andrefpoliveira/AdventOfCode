from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/03: Rucksack Reorganization")
problem.preprocessor = ppr.lsv

def get_priority(c):
    remove = -ord('A') + 27
    if c == c.lower(): remove = -ord('a') + 1
    return ord(c) + remove

@problem.solver(part=1)
def part1(ls):
    score = 0
    for l in ls:
        s1, s2 = l[:len(l)//2], l[len(l)//2:]
        s = set(s1)
        for c in s2:
            if c in s:
                score += get_priority(c)
                break
    return score

@problem.solver(part=2)
def part2(ls):
    score = 0
    for i in range(0, len(ls), 3):
        map = {}
        for j in range(0, 3):
            for c in set(ls[i + j]):
                map[c] = map.get(c, 0) + 1
        badge = [k for k, v in map.items() if v == 3][0]
        score += get_priority(badge)

    return score

if __name__ == "__main__":
    problem.solve()