import time, re

def solve(row, col):
    value = 31916031
    current_row, current_col = 1, 2
    max_row = 3

    while row != current_row or col != current_col:
        value = (value * 252533) % 33554393

        current_row -= 1
        current_col += 1

        if current_row == 0:
            current_row = max_row
            current_col = 1
            max_row += 1

    return (value * 252533) % 33554393

def run():
    with open("./2015/inputs/day25.txt", "r") as f:
        numbers = list(map(int, re.findall(r"\d+", f.readline())))

    start = time.time()
    print(f"Day 25 Part 1: {solve(numbers[0], numbers[1])}")
    end = time.time()

    return ["-", "-", end - start]

if __name__ == "__main__":
    print(run())