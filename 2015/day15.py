import numpy, time

def get_spoon_combs(l):
    spoons = [0 for _ in range(l)]

    while sum(spoons) != l*100:
        for i in range(l):
            spoons[i] += 1
            if spoons[i] > 100:
                spoons[i] = 0
            else:
                break
        if sum(spoons) == 100:
            yield spoons

def solve(d):
    lts = list(d.values())
    part1 = 0
    part2 = 0
    for spoons in get_spoon_combs(len(d.keys())):
        l = [0, 0, 0, 0]
        cal = 0
        for ingr, spoon in enumerate(spoons):
            if spoon != 0:
                for char in range(4):
                    l[char] += spoon * lts[ingr][char]
                cal += spoon * lts[ingr][-1]

        current_sum = numpy.prod([x if x > 0 else 0 for x in l])

        if current_sum > part1:
            part1 = current_sum

        if current_sum > part2 and cal == 500:
            part2 = current_sum

    return part1, part2

def run():
    with open("./2015/inputs/day15.txt", "r") as f:
        d = {}
        for line in f.readlines():
            splitted = line.strip().split(" ")
            ingr, cap, dur, fla, tex, cal = splitted[0][:-1], int(splitted[2][:-1]), int(splitted[4][:-1]), int(splitted[6][:-1]), int(splitted[8][:-1]), int(splitted[10])
        
            d[ingr] = [cap, dur, fla, tex, cal]

    start = time.time()
    part1, part2 = solve(d)
    end = time.time()
    print(f"Day 15 Part 1: {part1}")
    print(f"Day 15 Part 2: {part2}")

    return ["-", "-", end - start]

if __name__ == "__main__":
    run()