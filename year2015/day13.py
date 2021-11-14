from itertools import permutations
import time

def solve(d, list_people):
    max_hap = 0
    for p in permutations(list_people, len(list_people)):
        current_hap = d[f"{p[-1]}-{p[0]}"]
        current_hap += d[f"{p[0]}-{p[-1]}"]

        for i in range(1, len(list_people)):
            current_hap += d[f"{p[i-1]}-{p[i]}"]
            current_hap += d[f"{p[i]}-{p[i-1]}"]

        if current_hap > max_hap:
            max_hap = current_hap
    return max_hap

def run():
    with open("./year2015/inputs/day13.txt", "r") as f:
        d = {}
        list_people = set()
        for line in f.readlines():
            splitted = line.strip().split(" ")
            if "lose" in line:
                p1, hap, p2 = splitted[0], -int(splitted[3]), splitted[10][:-1]
            else:
                p1, hap, p2 = splitted[0], int(splitted[3]), splitted[10][:-1]

            d[f"me-{p1}"] = 0
            d[f"{p1}-me"] = 0
            d[f"{p1}-{p2}"] = hap

            list_people.add(p1)

    start = time.time()
    print(f"Day 13 Part 1: {solve(d, list_people)}")
    middle = time.time()
    list_people.add("me")
    print(f"Day 13 Part 2: {solve(d, list_people)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()