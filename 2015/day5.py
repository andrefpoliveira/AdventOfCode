import re

def part1(input_text):
    total = 0
    for word in input_text:
        if word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u') < 3: continue
        if not re.match(r'.*(\w)\1+.*', word): continue
        if "ab" in word or "cd" in word or "pq" in word or "xy" in word: continue

        total += 1
    return total

def part2(input_text):
    total = 0
    for word in input_text:
        if not re.match(r'.*(\w\w).*(\1).*', word): continue
        if not re.match(r'.*(\w)[a-z](\1).*', word): continue

        total += 1
    return total

if __name__ == "__main__":
    with open("./2015/inputs/day5.txt", "r") as f:
        input_text = f.readlines()

    print(f"Day 5 Part 1: {part1(input_text)}")
    print(f"Day 5 Part 2: {part2(input_text)}")