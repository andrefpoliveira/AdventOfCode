import re
import json

def part1 (input_text):
    return sum([int(x) for x in re.findall(r"-?\d+", input_text)])

def evaluate(data):
    total = 0
    if type(data) == list:
        for d in data:
            if type(d) in [list, dict]:
                total += evaluate(d)
            if type(d) == int:
                total += d

    else:
        if "red" not in data.keys() and "red" not in data.values():
            for d in data.values():
                if type(d) in [list, dict]:
                    total += evaluate(d)
                if type(d) == int:
                    total += d

    return total

def part2 (input_text):
    return evaluate(eval(input_text))

if __name__ == "__main__":
    with open("./2015/inputs/day12.txt", "r") as f:
        input_text = f.read().strip()

    print(f"Day 12 Part 1: {part1(input_text)}")
    print(f"Day 12 Part 2: {part2(input_text)}")