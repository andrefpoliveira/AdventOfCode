import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/09: Explosives in Cyberspace")
problem.preprocessor = ppr.I

def expand(s, part2=False):
    if "(" not in s: return len(s)
    else:
        if s[0] == "(":
            idx = s.index(")")
            nm, reps = [int(x) for x in re.findall(r"\d+", s[:idx])]
            if part2:
                return expand(s[idx+1:idx+1+nm], part2) * reps + expand(s[idx+1+nm:], part2)
            else:
                return len(s[idx+1:idx+1+nm]) * reps + expand(s[idx+1+nm:], part2)
        else:
            idx = s.index("(")
            return len(s[:idx]) + expand(s[idx:], part2)

@problem.solver(part=1)
def part1(s):
    return expand(s)

@problem.solver(part=2)
def part2(s):
    return expand(s, True)

if __name__ == "__main__":
    problem.solve()