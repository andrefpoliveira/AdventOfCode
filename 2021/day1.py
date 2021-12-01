import time

def part1(ns):
    return sum([ns[i] > ns[i-1] for i in range(1, len(ns))])

def part2(ns):
    return sum([sum(ns[i-2:i+1]) > sum(ns[i-3:i]) for i in range(3, len(ns))])

def run():
    with open("./2021/inputs/day1.txt", "r") as f:
        input_text = [int(x) for x in f.read().split("\n")]

    start = time.time()
    print(f"Day 1 Part 1: {part1(input_text)}")
    middle = time.time()
    print(f"Day 1 Part 2: {part2(input_text)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()