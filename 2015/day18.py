def get_neighbours(x, y):
    l = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    res = []
    for i in l:
        dx = x + i[0]
        dy = y + i[1]
        if not (dx < 0 or dx > 99 or dy < 0 or dy > 99):
            res.append((dx, dy))

    return res

def part1(map, neighbours):
    for _ in range(100):
        new_map = []
        for y in range(100):
            line = []
            for x in range(100):
                on = map[x][y] == 1
                lights_on = sum([map[c[0]][c[1]] for c in neighbours[(x, y)]])

                if (on and (lights_on == 2 or lights_on == 3)) or (not on and lights_on == 3):
                    line.append(1)
                else:
                    line.append(0)
            new_map.append(line)
        map = new_map

    return sum([item for sublist in map for item in sublist])

def part2(map, neighbours):
    for _ in range(100):
        new_map = []
        for y in range(100):
            line = []
            for x in range(100):
                if (x == 0 or x == 99) and (y == 0 or y == 99):
                    line.append(1)
                    continue

                on = map[x][y] == 1
                lights_on = sum([map[c[0]][c[1]] for c in neighbours[(x, y)]])

                if (on and (lights_on == 2 or lights_on == 3)) or (not on and lights_on == 3):
                    line.append(1)
                else:
                    line.append(0)
            new_map.append(line)
        map = new_map

    return sum([item for sublist in map for item in sublist])

def run():
    with open("./2015/inputs/day18.txt", "r") as f:
        map = [[1 if x == "#" else 0 for x in l.strip()] for l in f.readlines()]

    neighbours = {}
    for x in range(100):
        for y in range(100):
            neighbours[(x, y)] = get_neighbours(x, y)


    print(f"Day 18 Part 1: {part1(map, neighbours)}")

    map[0][0] = 1
    map[0][99] = 1
    map[99][0] = 1
    map[99][99] = 1

    print(f"Day 18 Part 2: {part2(map, neighbours)}")

if __name__ == "__main__":
    run()