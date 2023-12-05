from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2019/01: The Tyranny of the Rocket Equation")
problem.preprocessor = ppr.lsi

def calculate_fuel(n, part2=False):
    fuel = n // 3 - 2
    if part2:
        if fuel <= 0: return 0
        return fuel + calculate_fuel(fuel, True)
    return fuel

@problem.solver(part=1)
def part1(ns):
    return sum([calculate_fuel(n) for n in ns])

@problem.solver(part=2)
def part2(ns):
    return sum([calculate_fuel(n, True) for n in ns])

if __name__ == "__main__":
    problem.solve()