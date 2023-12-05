import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/05: Doesn't He Have Intern-Elves For This?")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(input_text):
    total = 0
    for word in input_text:
        if word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u') < 3: continue
        if not re.match(r'.*(\w)\1+.*', word): continue
        if "ab" in word or "cd" in word or "pq" in word or "xy" in word: continue

        total += 1
    return total

@problem.solver(part=2)
def part2(input_text):
    total = 0
    for word in input_text:
        if not re.match(r'.*(\w\w).*(\1).*', word): continue
        if not re.match(r'.*(\w)[a-z](\1).*', word): continue

        total += 1
    return total

if __name__ == "__main__":
    problem.solve()