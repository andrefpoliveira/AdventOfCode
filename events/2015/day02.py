import math
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/02: I Was Told There Would Be No Math")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(input_text):
    t = 0
    for line in input_text:
        l,w,h = map(lambda x: int(x), line.split("x"))
        t += 2*l*w + 2*w*h + 2*h*l + min(l*w, min(w*h, h*l))
    return t

@problem.solver(part=2)
def part2(input_text):
    t = 0
    for line in input_text:
        v = list(map(lambda x: int(x), line.split("x")))
        m1 = min(v)
        v.remove(m1)
        m2 = min(v)

        t += 2*m1 + 2*m2 + math.prod(v)*m1
    return t

if __name__ == "__main__":
    problem.solve()