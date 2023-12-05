from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/02: Rock Paper Scissors")
problem.preprocessor = ppr.lsv

@problem.solver()
def solver(ls):
    score1 = score2 = 0
    for l in ls:
        score1 += {"X": 1, "Y": 2, "Z": 3}[l[-1]]
        if l in ["A X", "B Y", "C Z"]: score1 += 3
        elif l in ["A Y", "B Z", "C X"]: score1 += 6

        score2 += {"X": 0, "Y": 3, "Z": 6}[l[-1]]
        if l in ["B X", "A Y", "C Z"]: score2 += 1
        elif l in ["C X", "B Y", "A Z"]: score2 += 2
        else: score2 += 3

    return score1, score2

if __name__ == "__main__":
    problem.solve()