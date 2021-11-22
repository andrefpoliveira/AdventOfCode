import time

def solve(directions):
    pos = [(0,0)]
    d, dir = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
    x, y = 0, 0
    part2 = float("Inf")

    for i in directions:
        if "L" == i[0]:
            dir -= 1
            if dir < 0:
                dir = 3

        if "R" == i[0]:
            dir += 1
            if dir > 3:
                dir = 0

        for i in range(1, 1 + int(i[1:])):
            x += d[dir][0]
            y += d[dir][1]

            if (x, y) in pos and part2 == float("Inf"):
                part2 = abs(x) + abs(y)
            else:
                pos.append((x, y))

    return abs(x) + abs(y), part2

def run():
    with open("./2016/inputs/day1.txt", "r") as f:
        directions = f.readline().split(", ")

    start = time.time()
    part1, part2 = solve(directions)
    end = time.time()
    print(f"Day 1 Part 1: {part1}")
    print(f"Day 1 Part 2: {part2}")

    return ["-", "-", end - start]

if __name__ == "__main__":
    run()