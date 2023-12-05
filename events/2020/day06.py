from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/06: Custom Customs")
problem.preprocessor = lambda x: x.split("\n\n")

@problem.solver(part=1)
def part1(ls):
    return sum([len(set(l.replace("\n", ""))) for l in ls])

@problem.solver(part=2)
def part2(ls):
    count = 0
    for l in ls:
        p = l.split()
        s = set(p[0])
        for answers in p[1:]:
            s = s.intersection(set(answers))
        count += len(s)
    return count
    

if __name__ == "__main__":
    problem.solve()