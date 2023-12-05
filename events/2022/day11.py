from utils import problem
from utils import preprocessing as ppr
from utils import ntheory as nt

import re

problem = problem.Problem("2022/11: Monkey in the Middle")
problem.preprocessor = ppr.I

def parse_input(s):
    monkeys = []
    for monkey in s.split("\n\n"):
        lines = monkey.splitlines()
        m = {
            "count": 0,
            "items": [int(x) for x in re.findall(r"(\d+)", lines[1])],
            "op": re.findall(r"= (.+)", lines[2])[0],
            "test": [int(x) for x in re.findall(r"(\d+)", lines[3] + lines[4] + lines[5])],
        }
        monkeys.append(m)
    return monkeys

def throwing(monkeys, rounds, div):
    lcm = nt.lcm([m["test"][0] for m in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            monkey["count"] += len(monkey["items"])
            for old in monkey["items"]:
                new = (eval(monkey["op"]) // div) % lcm
                if new % monkey["test"][0] == 0:
                    monkeys[monkey["test"][1]]["items"].append(new)
                else:
                    monkeys[monkey["test"][2]]["items"].append(new)
            monkey["items"] = []

    keys = sorted([monkeys[i]["count"] for i in range(len(monkeys))], reverse=True)
    return keys[0] * keys[1]


@problem.solver(part=1)
def part1(s):
    monkeys = parse_input(s)
    return throwing(monkeys, 20, 3)

@problem.solver(part=2)
def part2(s):
    monkeys = parse_input(s)
    return throwing(monkeys, 10000, 1)

if __name__ == "__main__":
    problem.solve()