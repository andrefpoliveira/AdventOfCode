from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/01: Not Quite Lisp")
problem.preprocessor = ppr.I

@problem.solver(part=1)
def part1(input_text):
    return input_text.count("(") - input_text.count(")")

@problem.solver(part=2)
def part2(input_text):
    floor, l = 0, ["(", ")"]
    for i in range(len(input_text)):
        floor += [1, -1][l.index(input_text[i])]
        if floor == -1: return i+1
    return -1

if __name__ == "__main__":
    problem.solve()