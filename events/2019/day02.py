from utils import problem
from utils import preprocessing as ppr
from utils import intcode

problem = problem.Problem("2019/02: 1202 Program Alarm")
problem.preprocessor = ppr.csi

@problem.solver(part=1)
def part1(ns):
    computer = intcode.Intcode(ns)
    computer.replace_noun_verb(12, 2)
    return computer.run()

@problem.solver(part=2)
def part2(ns):
    computer = intcode.Intcode(ns)
    for noun in range(100):
        for verb in range(100):
            computer.replace_noun_verb(noun, verb)
            halt_value = computer.run()
            if halt_value == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    problem.solve()