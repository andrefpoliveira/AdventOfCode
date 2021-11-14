from itertools import combinations

def part1(containers):
    total = 0
    for L in range(1, len(containers)+1):
        for c in combinations(containers, L):
            if sum(c) == 150: total += 1
    return total

def part2(containers):
    for L in range(1, len(containers)+1):
        total = 0
        for c in combinations(containers, L):
            if sum(c) == 150: total += 1
        if total > 0: return total
    return -1

def run():
    with open("./2015/inputs/day17.txt", "r") as f:
        containers = [int(x.strip()) for x in f.readlines()]

    print(f"Day 17 Part 1: {part1(containers)}")
    print(f"Day 17 Part 2: {part2(containers)}")

if __name__ == "__main__":
    run()