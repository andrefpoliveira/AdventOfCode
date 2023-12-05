import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/12: JSAbacusFramework.io")
problem.preprocessor = ppr.I

@problem.solver(part=1)
def part1 (input_text):
    return sum([int(x) for x in re.findall(r"-?\d+", input_text)])

def evaluate(data):
    total = 0
    if type(data) == list:
        for d in data:
            if type(d) in [list, dict]:
                total += evaluate(d)
            if type(d) == int:
                total += d

    else:
        if "red" not in data.keys() and "red" not in data.values():
            for d in data.values():
                if type(d) in [list, dict]:
                    total += evaluate(d)
                if type(d) == int:
                    total += d

    return total

@problem.solver(part=2)
def part2 (input_text):
    return evaluate(eval(input_text))

if __name__ == "__main__":
    problem.solve()