from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/01: Calorie Counting")
problem.preprocessor = ppr.I

@problem.solver()
def solver(s):
    scores = sorted([sum(int(x) for x in elf.split("\n")) for elf in s.split("\n\n")], reverse=True)
    return scores[0], sum(scores[:3])

if __name__ == "__main__":
    problem.solve()