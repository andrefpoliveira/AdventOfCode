import re
from utils import problem

problem = problem.Problem("2016/15: Timing is Everything")
problem.preprocessor = lambda inp: [[int(x) for x in re.findall(r"\d+", l)][1:] for l in inp.strip().split("\n")]

def calculate_position(n_pos, init_pos, secs):
    return (init_pos + secs) % n_pos

@problem.solver(part=1)
def part1(ls):
    t = 0
    while True:
        for id, disc in enumerate(ls):
            if calculate_position(disc[0], disc[2], t + id + 1) != 0: break
        else:
            return t

        t += 1

@problem.solver(part=2)
def part2(ls):
    ls.append([11, 0, 0])
    t = 0
    while True:
        for id, disc in enumerate(ls):
            if calculate_position(disc[0], disc[2], t + id + 1) != 0: break
        else:
            return t

        t += 1

if __name__ == "__main__":
    problem.solve()