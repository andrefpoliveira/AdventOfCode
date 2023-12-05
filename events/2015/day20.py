from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/20: Infinite Elves and Infinite Houses")
problem.preprocessor = ppr.intI

@problem.solver(part=1)
def part1(number):
    houses = [0 for x in range(number//10)]
    for elf in range(1, number//10):
        for house in range(elf, number//10, elf):
            houses[house-1] += elf * 10

    for i in range(len(houses)):
        if houses[i] >= number:
            return i+1

@problem.solver(part=2)
def part2(number):
    houses = [0 for x in range(number//10)]
    for elf in range(1, number//10):
        for house in range(elf, min(number//10, elf*50 + 1), elf):
            houses[house-1] += elf * 11

    for i in range(len(houses)):
        if houses[i] >= number:
            return i+1

if __name__ == "__main__":
    problem.solve()