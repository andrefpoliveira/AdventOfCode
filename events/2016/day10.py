import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/10: Balance chips")
problem.preprocessor = ppr.lsv

chips = dict()

def add_value(chips, bot, v):
    l = chips.get(bot, [])
    l.append(v)
    chips[bot] = l

@problem.solver(part=1)
def part1(ls):
    global chips
    instrs = dict()

    for l in ls:
        if "value" in l:
            v, bot = [int(x) for x in re.findall(r"\d+", l)]
            add_value(chips, f"bot {bot}", v)
        else:
            bot, bot_low, bot_high = [x for x in re.findall(r"output \d+|bot \d+", l)]
            instrs[bot] = [bot_low, bot_high]

    while any(len(v) == 2 for _,v in chips.items()):
        for k, v in list(chips.items()):
            if len(v) == 2:
                max_v, min_v = max(v), min(v)
                if min_v == 17 and max_v == 61: res = k.split(" ")[-1]

                bot_low, bot_high = instrs[k]
                chips[k] = []
                add_value(chips, bot_high, max_v)
                add_value(chips, bot_low, min_v)
                break

    return res
        
@problem.solver(part=2)
def part2(ls):
    res = 1
    for k in ["output 0", "output 1", "output 2"]:
        for chip in chips.get(k, []):
            res *= chip
    return res

if __name__ == "__main__":
    problem.solve()