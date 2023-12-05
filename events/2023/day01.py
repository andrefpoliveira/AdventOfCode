from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2023/01: Trebuchet?!")
problem.preprocessor = ppr.lsv

pattern = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
number = {v: id % 9 + 1 for id, v in enumerate(pattern.split("|"))}

@problem.solver()
def solver(ls):
    part1 = part2 = 0
    for l in ls:
        ns = re.findall(rf"(?=({pattern}))", l)

        digits = [x for x in ns if len(x) == 1]
        part1 += number[digits[0]] * 10 + number[digits[-1]]

        part2 += number[ns[0]] * 10 + number[ns[-1]]

    return part1, part2

if __name__ == "__main__":
    problem.solve()