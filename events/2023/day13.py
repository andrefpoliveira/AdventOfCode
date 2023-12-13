from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2023/13: Point of Incidence")
problem.preprocessor = lambda x: [p.split() for p in x.split("\n\n")]

def rotate_pattern(pattern):
    return [
        ''.join([pattern[y][x] for y in range(len(pattern))])
        for x in range(len(pattern[0]))
    ]

def get_mirror(pattern):
    for i in range(1, len(pattern)):
        for x, row in enumerate(pattern):
            if i == x: return i

            compare = i * 2 - 1 - x
            if compare < len(pattern) and row != pattern[compare]:
                break

def get_smudge_mirror(pattern):
    for i in range(1, len(pattern)):
        diffs = 0
        for x, row in enumerate(pattern):
            if i == x and diffs == 1: return i

            compare = i * 2 - 1 - x
            if compare < len(pattern):
                diffs += sum(c1 != c2 for c1, c2 in zip(row, pattern[compare]))
                if diffs > 1:
                    break

@problem.solver(part=1)
def part1(ls):
    part1 = 0
    for l in ls:
        v = get_mirror(l)
        if v is not None:
            part1 += v * 100
            continue

        rotated = rotate_pattern(l)
        part1 += get_mirror(rotated)

    return part1

@problem.solver(part=2)
def part2(ls):
    part2 = 0
    for l in ls:
        v = get_smudge_mirror(l)
        if v is not None:
            part2 += v * 100
            continue

        rotated = rotate_pattern(l)
        part2 += get_smudge_mirror(rotated)

    return part2

if __name__ == "__main__":
    problem.solve()