from utils import problem

import re

problem = problem.Problem("2022/05: Supply Stacks")
problem.preprocessor = lambda x: x

@problem.solver()
def solver(s):
    crates, insts = s.split("\n\n")
    row_crates = crates.split("\n")
    insts = insts.strip().split("\n")

    crates_part1 = [[] for _ in range(len([x for x in row_crates[-1] if x != " "]))]
    crates_part2 = [[] for _ in range(len([x for x in row_crates[-1] if x != " "]))]

    for r in row_crates[:-1]:
        for id, i in enumerate(range(1, len(r), 4)):
            if r[i] != " ":
                crates_part1[id].insert(0, r[i])
                crates_part2[id].insert(0, r[i])

    for inst in insts:
        quant, fr, to = [int(x) for x in re.findall(r'(\d+)', inst)]
        
        crates_part1[to - 1] += crates_part1[fr - 1][-quant:][::-1]
        crates_part2[to - 1] += crates_part2[fr - 1][-quant:]

        crates_part1[fr - 1] = crates_part1[fr - 1][:-quant]
        crates_part2[fr - 1] = crates_part2[fr - 1][:-quant]

    return ''.join(x[-1] for x in crates_part1), ''.join(x[-1] for x in crates_part2)

if __name__ == "__main__":
    problem.solve()