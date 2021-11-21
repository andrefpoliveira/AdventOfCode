import re, time

def part1(reactions, mol):
    s = set()
    for fr, t in reactions:
        matches = [(m.start(0), m.end(0)) for m in re.finditer(fr, mol)]

        for match in matches:

            new_s = mol[:match[0]] + t + mol[match[1]:]
            s.add(new_s)

    return len(s)

def part2(reactions, mol):
    count = 0
    while mol != "e":
        for fr, t in reactions:
            if t in mol:
                mol = mol.replace(t, fr, 1) 
                count += 1
    return count

def run():
    reactions = []

    with open("./2015/inputs/day19.txt", "r") as f:
        lines = f.readlines()
        for line in lines[:-2]:
            spl = line.strip().split(" => ")
            fr, t = spl[0], spl[1]
            reactions.append((fr, t))

        mol = lines[-1].strip() 

    start = time.time()
    print(f"Day 19 Part 1: {part1(reactions, mol)}")
    middle = time.time()
    print(f"Day 19 Part 2: {part2(reactions, mol)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()