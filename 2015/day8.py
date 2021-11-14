import re

def part1(input_text):
    return sum([len(word.strip()) - len(eval(word.strip())) for word in input_text])

def part2(input_text):
    return sum([len('"' + word.strip().replace('\\', '\\\\').replace('"', '\\"') + '"') - len(word.strip()) for word in input_text])

if __name__ == "__main__":
    with open("./2015/inputs/day8.txt", "r") as f:
        input_text = f.readlines()

    print(f"Day 8 Part 1: {part1(input_text)}")
    print(f"Day 8 Part 2: {part2(input_text)}")