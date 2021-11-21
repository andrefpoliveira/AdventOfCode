import time

def part1(input_text):
    x,y = 0,0
    visited = set()
    visited.add((0,0))
    d = {">": [0,1], "<": [0,-1], "v": [-1,0], "^": [1,0]}
    for i in input_text:
        x += d[i][0]
        y += d[i][1]
        visited.add((x,y))
    return len(visited)

def part2(input_text):
    x,y = 0,0
    x2,y2 = 0,0
    visited = set()
    visited.add((0,0))
    d = {">": [0,1], "<": [0,-1], "v": [-1,0], "^": [1,0]}
    for idx, i in enumerate(input_text):
        if idx % 2 == 0:
            x += d[i][0]
            y += d[i][1]
            visited.add((x,y))
        else:
            x2 += d[i][0]
            y2 += d[i][1]
            visited.add((x2,y2))

    return len(visited)

def run():
    with open("./2015/inputs/day3.txt", "r") as f:
        input_text = f.read()

    start = time.time()
    print(f"Day 3 Part 1: {part1(input_text)}")
    middle = time.time()
    print(f"Day 3 Part 2: {part2(input_text)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()