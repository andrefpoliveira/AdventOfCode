from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/06: Signals and Noise")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
    res = ""
    for i in range(len(ls[0])):
        letters = dict()
        for word in ls:
            letters[word[i]] = letters.get(word[i], 0) + 1

        res += max(letters, key=letters.get)
    return res

@problem.solver(part=2)
def part2(ls):
    res = ""
    for i in range(len(ls[0])):
        letters = dict()
        for word in ls:
            letters[word[i]] = letters.get(word[i], 0) + 1

        res += min(letters, key=letters.get)
    return res

if __name__ == "__main__":
    problem.solve()