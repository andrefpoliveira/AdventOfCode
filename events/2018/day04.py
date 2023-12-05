from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/04: Repose Record")
problem.preprocessor = ppr.lsv

guards = {}

@problem.solver(part=1)
def part1(ls):
    global guards

    ls = sorted(ls)
    
    ind = 0
    while ind < len(ls):
        m = re.match(r'\[\d+-\d+-\d+ \d+:\d+\] Guard #(\d+) begins shift', ls[ind])
        id = int(m.groups()[0])

        data = guards.get(id, {})
        
        while ind + 1 < len(ls) and "shift" not in ls[ind+1]:
            asleep = re.match(r'\[\d+-\d+-\d+ \d+:(\d+)\] falls asleep', ls[ind+1])
            min = int(asleep.groups()[0])

            awake = re.match(r'\[\d+-\d+-\d+ \d+:(\d+)\] wakes up', ls[ind+2])
            p_minute = int(awake.groups()[0])

            for i in range(min, p_minute):
                data[(i)] = data.get(i, 0) + 1

            ind += 2

        guards[id] = data

        ind += 1

    max_id = -1
    max_v = -1
    for k in guards:
        max_c = sum(guards[k].values())
        if max_c > max_v:
            max_id, max_v = k, max_c

    return max(guards[max_id], key=guards[max_id].get) * max_id

@problem.solver(part=2)
def part2(ls):
    global guards

    guard = -1
    best_minute = -1
    max_minutes_count = -1
    for k in guards:
        if not guards[k]: continue
        minute = max(guards[k], key=guards[k].get)
        minutes_asleep = guards[k][minute]
        if minutes_asleep > max_minutes_count:
            guard, best_minute, max_minutes_count = k, minute, minutes_asleep

    return guard * best_minute


if __name__ == "__main__":
    problem.solve()