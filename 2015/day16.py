def part1(sues, info):
    matches = []
    for sue in sues:
        match = 0
        d = sue
        for key in d:
            if info[key] == d[key]: match += 1

        matches.append(match)
    return matches.index(max(matches))+1

def part2(sues, info):
    matches = []
    for sue in sues:
        match = 0
        d = sue
        for key in d:
            if key in ["cats", "trees"]:
                if info[key] < d[key]: match += 1
            elif key in ["pomeranians", "goldfish"]:
                if info[key] > d[key]: match += 1
            else:
                if info[key] == d[key]: match += 1

        matches.append(match)
    return matches.index(max(matches))+1

def run():
    with open("./2015/inputs/day16.txt", "r") as f:
        sues = []
        for line in f.readlines():
            splitted = line.strip().split(" ")
            c1, v1, c2, v2, c3, v3 = splitted[2][:-1], int(splitted[3][:-1]), splitted[4][:-1], int(splitted[5][:-1]), splitted[6][:-1], int(splitted[7])
        
            sues.append({c1: v1, c2:v2, c3:v3})

            info = {
                "children": 3,
                "cats": 7,
                "samoyeds": 2,
                "pomeranians": 3,
                "akitas": 0,
                "vizslas": 0,
                "goldfish": 5,
                "trees": 3,
                "cars": 2,
                "perfumes": 1
            }

    print(f"Day 16 Part 1: {part1(sues, info)}")
    print(f"Day 16 Part 2: {part2(sues, info)}")

if __name__ == "__main__":
    run()