from utils import problem

import re

problem = problem.Problem("2020/04: Passport Processing")
problem.preprocessor = lambda x: x.split("\n\n")

byr = lambda x: 1920 <= int(x) <= 2002
iyr = lambda x: 2010 <= int(x) <= 2020
eyr = lambda x: 2020 <= int(x) <= 2030
hgt = lambda x: False if not x[:-2].isdigit() or not x[-2:] in ["cm", "in"] else 150 <= int(x[:-2]) <= 193 if x[-2:] == "cm" else 59 <= int(x[:-2]) <= 76
hcl = lambda x: x[0] == "#" and all([c in "0123456789abcdef" for c in x[1:]])
ecl = lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
pid = lambda x: x.isdigit() and len(x) == 9

checks = [byr, iyr, eyr, hgt, hcl, ecl, pid]

@problem.solver(part=1)
def part1(ls):
    count = 0
    for l in ls:
        for header in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            m = re.findall(rf"{header}:([^ \n]+)", l)

            if not m: break
        else:
            count += 1

    return count

@problem.solver(part=2)
def part2(ls):
    count = 0
    for l in ls:
        for id, header in enumerate(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
            m = re.findall(rf"{header}:([^ \n]+)", l)

            if not m: break
            if not checks[id](m[0]): break
        else:
            count += 1

    return count
            
if __name__ == "__main__":
    problem.solve()