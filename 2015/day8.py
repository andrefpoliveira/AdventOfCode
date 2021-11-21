import re, time

def part1(input_text):
    return sum([len(word.strip()) - len(eval(word.strip())) for word in input_text])

def part2(input_text):
    return sum([len('"' + word.strip().replace('\\', '\\\\').replace('"', '\\"') + '"') - len(word.strip()) for word in input_text])

def run():
    with open("./2015/inputs/day8.txt", "r") as f:
        input_text = f.readlines()

    start = time.time()
    print(f"Day 8 Part 1: {part1(input_text)}")
    middle = time.time()
    print(f"Day 8 Part 2: {part2(input_text)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()