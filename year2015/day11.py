import time

def increase(pwd_numbers):
    min_n = ord('a')
    max_n = ord('z')

    for i in range(len(pwd_numbers)-1, -1, -1):
        pwd_numbers[i] += 1
        if pwd_numbers[i] > max_n:
            pwd_numbers[i] = min_n
            continue
        break
    return pwd_numbers

def is_valid(pwd_numbers):
    for i in [105, 108, 111]:
        if i in pwd_numbers:
            return False

    for i in range(2, len(pwd_numbers)):
        if pwd_numbers[i] - pwd_numbers[i-2] == 2 and pwd_numbers[i] - pwd_numbers[i-1] == 1:
            break
    else:
        return False

    i = 1
    count = 0
    while i < len(pwd_numbers):
        if pwd_numbers[i] == pwd_numbers[i-1]:
            i += 2
            count += 1
            continue
        i += 1
    
    return count >= 2


def solve(pwd):
    pwd_numbers = [ord(x) for x in pwd]
    while True:
        pwd_numbers = increase(pwd_numbers)
        if is_valid(pwd_numbers):
            return ''.join(map(chr, pwd_numbers))
        
def run():
    with open("./year2015/inputs/day11.txt", "r") as f:
        input_text = f.read().strip()

    start = time.time()
    part1 = solve(input_text)
    middle = time.time()
    print(f"Day 11 Part 1: {part1}")
    print(f"Day 11 Part 2: {solve(part1)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()