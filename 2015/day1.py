def part1(input_text):
    return input_text.count("(") - input_text.count(")")

def part2(input_text):
    floor, l = 0, ["(", ")"]
    for i in range(len(input_text)):
        floor += [1, -1][l.index(input_text[i])]
        if floor == -1: return i+1
    return -1

if __name__ == "__main__":
    with open("./2015/inputs/day1.txt", "r") as f:
        input_text = f.read()

    print(f"Day 1 Part 1: {part1(input_text)}")
    print(f"Day 1 Part 2: {part2(input_text)}")