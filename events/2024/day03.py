from utils import problem
from utils import preprocessing as ppr
from utils import corrupted_computer as cc

problem = problem.Problem("2024/03: Mull It Over")
problem.preprocessor = ppr.lsv


@problem.solver(part=1)
def part1(ls):
    return cc.CorruptedComputer(ls, [cc.InstructionsList.MULTIPLY]).run()


@problem.solver(part=2)
def part2(ls):
    return cc.CorruptedComputer(ls, [
        cc.InstructionsList.MULTIPLY,
        cc.InstructionsList.DO,
        cc.InstructionsList.DONT
    ]).run()


if __name__ == "__main__":
    problem.solve()