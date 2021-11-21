import time
from itertools import combinations
from functools import reduce
from operator import mul

def solve(weights, parts):
    goal_weight = sum(weights)//parts

    for i in range(len(weights)):
        qua_ent = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == goal_weight]
        if len(qua_ent) > 0:
            return min(qua_ent)


def run():
    with open("./2015/inputs/day24.txt", "r") as f:
        weights = [int(x.strip()) for x in f.readlines()]

    start = time.time()
    print(f"Day 24 Part 1: {solve(weights, 3)}")
    middle = time.time()
    print(f"Day 24 Part 2: {solve(weights, 4)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()