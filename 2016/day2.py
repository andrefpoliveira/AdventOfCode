import time

def solve(lines, buttons):
    x, y, res = 1, 1, ""
    d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    for line in lines:
        for dir in line:
            x += d[dir][0]
            y += d[dir][1]

            if x < 0 or x >= len(buttons) or y < 0 or y >= len(buttons) or buttons[x][y] == "#":
                x -= d[dir][0]
                y -= d[dir][1]

        res += buttons[x][y]
    return res

def run():
    with open("./2016/inputs/day2.txt", "r") as f:
        lines = [x.strip() for x in f.readlines()]

    start = time.time()
    print(f"Day 2 Part 1: {solve(lines, [['1','2','3'], ['4','5','6'], ['7','8','9']])}")
    middle = time.time()
    print(f"Day 2 Part 2: {solve(lines, [['#', '#', '1', '#', '#'], ['#', '2', '3', '4', '#'], ['5', '6', '7', '8', '9'], ['#', 'A', 'B', 'C', '#'], ['#', '#', 'D', '#', '#']])}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()