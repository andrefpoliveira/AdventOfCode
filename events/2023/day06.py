from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2023/06: Wait For It")
problem.preprocessor = ppr.lsv

def is_record(t, time, distance):
    return t * (time - t) > distance

@problem.solver(part=1)
def part1(ls):
    part1 = 1
    times = tuple(map(int, re.findall(r"\d+", ls[0])))
    distances = tuple(map(int, re.findall(r"\d+", ls[1])))

    for i in range(len(times)):
        c = 0
        time, distance = times[i], distances[i]
        for t in range(time):
            if t * (time - t) > distance:
                c += 1
        part1 *= c
    return part1

@problem.solver(part=2)
def part2(ls):
    RANGE_STEP = 20000

    time = int(''.join(re.findall(r"\d+", ls[0])))
    distance = int(''.join(re.findall(r"\d+", ls[1])))
    part2 = 0

    for t in range(0, time, RANGE_STEP):
        if is_record(t, time, distance):
            if part2 == 0:
                for _t in range(t-1, t - RANGE_STEP - 1, -1):
                    if is_record(_t, time, distance):
                        part2 += 1
                    else:
                        break
            else:
                part2 += RANGE_STEP

        elif part2 > 0:
            for _t in range(t-1, t - RANGE_STEP - 1, -1):
                if is_record(_t, time, distance):
                    part2 += 1

            return part2

if __name__ == "__main__":
    problem.solve()