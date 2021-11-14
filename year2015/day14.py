import time

def part1 (d):
    max_distance = 0

    for r in d:
        spd, time, rest = d[r]
        current_time = 2503
        current_dist = 0
        while current_time > 0:
            current_dist += spd * (time if current_time - time > 0 else current_time - time)
            current_time -= (time + rest)

        if current_dist > max_distance:
            max_distance = current_dist

    return max_distance

def part2 (d):
    distances = []
    for r in d:
        l = []
        spd, time, rest = d[r]
        current_time = 2503
        current_dist = 0
        t1, t2 = time, rest
        while current_time > 0:
            if t1 > 0:
                current_dist += spd
                t1 -= 1
            elif t2 > 0:
                t2 -= 1
            else:
                t1, t2 = time,rest
                continue
            l.append(current_dist)
            current_time -= 1

        distances.append(l)

    points = [0 for _ in range(len(d.keys()))]
    for i in range(2503):
        max_distance = max(x[i] for x in distances)
        for j in range(len(d.keys())):
            if distances[j][i] == max_distance:
                points[j] += 1

    return max(points)

def run():
    with open("./year2015/inputs/day14.txt", "r") as f:
        d = {}
        for line in f.readlines():
            splitted = line.strip().split(" ")
            r, s, t1, rest = splitted[0], int(splitted[3]), int(splitted[6]), int(splitted[-2])
        
            d[r] = [s, t1, rest]

    start = time.time()
    print(f"Day 14 Part 1: {part1(d)}")
    middle = time.time()
    print(f"Day 14 Part 2: {part2(d)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()