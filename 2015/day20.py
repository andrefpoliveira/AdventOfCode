def part1(number):
    houses = [0 for x in range(number//10)]
    for elf in range(1, number//10):
        for house in range(elf, number//10, elf):
            houses[house-1] += elf * 10

    for i in range(len(houses)):
        if houses[i] >= number:
            return i+1

def part2(number):
    houses = [0 for x in range(number//10)]
    for elf in range(1, number//10):
        for house in range(elf, min(number//10, elf*50 + 1), elf):
            houses[house-1] += elf * 11

    for i in range(len(houses)):
        if houses[i] >= number:
            return i+1

def run():
    with open("./2015/inputs/day20.txt", "r") as f:
        number = int(f.read().strip())

    print(f"Day 20 Part 1: {part1(number)}")
    print(f"Day 20 Part 2: {part2(number)}")

if __name__ == "__main__":
    run()