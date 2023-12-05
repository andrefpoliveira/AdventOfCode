from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/04: High-Entropy Passphrases")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
    return len([l for l in ls if len(set(l.split())) == len(l.split())])
    
@problem.solver(part=2)
def part2(ls):
    return len([l for l in ls if len(set(map(lambda x: "".join(sorted(x)), l.split()))) == len(l.split())])

if __name__ == "__main__":
    problem.solve()