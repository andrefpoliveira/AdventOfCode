from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/08: Matchsticks")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(input_text):
    return sum([len(word.strip()) - len(eval(word.strip())) for word in input_text])

@problem.solver(part=2)
def part2(input_text):
    return sum([len('"' + word.strip().replace('\\', '\\\\').replace('"', '\\"') + '"') - len(word.strip()) for word in input_text])

if __name__ == "__main__":
    problem.solve()