from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/05: Alchemical Reduction")
problem.preprocessor = ppr.I

letters = "abcdefghijklmnopqrstuvwxyz"

def react(s):
    diff = 32
    w = ""
    for i in range(0, len(s)):
        if not w: w = s[i]
        else:
            if abs(ord(s[i]) - ord(w[-1])) == diff:
                w = w[:-1]
                continue
            
            w += s[i]
    return w

@problem.solver(part=1)
def part1(s):
    w = react(s)
    return len(w)

@problem.solver(part=2)
def part2(s):
    min_size = len(s)
    for l in letters:
        new_s = s.replace(l, "").replace(l.upper(), "")
        min_size = min(min_size, len(react(new_s)))
    return min_size

if __name__ == "__main__":
    problem.solve()