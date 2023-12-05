from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/19: An Elephant Named Joseph")
problem.preprocessor = ppr.intI

@problem.solver(part=1)
def part1(n):
    # See https://www.youtube.com/watch?v=uCsD3ZGzMgE&t=659s (Numberphile - The Josephus Problem)
    return int("0b" + bin(n)[3:] + "1", 2)

@problem.solver(part=2)
def part2(n):
    previous_power = 1
    power = 3
    while power <= n:
        previous_power = power
        power *= 3

    return n - previous_power

if __name__ == "__main__":
    problem.solve()