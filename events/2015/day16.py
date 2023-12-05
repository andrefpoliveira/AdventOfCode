from utils import problem

problem = problem.Problem("2015/16: Aunt Sue")
problem.preprocessor = lambda x: [{l.split()[2][:-1]: int(l.split()[3][:-1]), l.split()[4][:-1]: int(l.split()[5][:-1]), l.split()[6][:-1]: int(l.split()[7])} for l in x.strip().split("\n")]

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

@problem.solver(part=1)
def part1(sues):
    matches = []
    for sue in sues:
        match = 0
        d = sue
        for key in d:
            if info[key] == d[key]: match += 1

        matches.append(match)
    return matches.index(max(matches))+1

@problem.solver(part=2)
def part2(sues):
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

if __name__ == "__main__":
    problem.solve()