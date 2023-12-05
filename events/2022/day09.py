from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/09: Rope Bridge")
problem.preprocessor = ppr.lsv

def step(diff):
    return (diff > 0) - (diff < 0)

def move_head(h, dir):
    h[0] += dir[0]
    h[1] += dir[1]

def move_body(r1, r2):
    dx, dy = r1[0] - r2[0], r1[1] - r2[1]
    if abs(dx) > 1 or abs(dy) > 1:
        r2[0] += step(dx)
        r2[1] += step(dy)

def move(rope, dir):
    move_head(rope[0], dir)

    for i in range(1, len(rope)):
        move_body(rope[i-1], rope[i])

    return tuple(rope[-1])

def execute(ls, size):
    rope = [[0,0] for _ in range(size)]
    dirs = {"R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1)}
    return len({ move(rope, dirs[dir]) for dir, count in (l.split() for l in ls) for _ in range(int(count))})

@problem.solver(part=1)
def part1(ls):
    return execute(ls, 2)

@problem.solver(part=2)
def part2(ls):
    return execute(ls, 10)

if __name__ == "__main__":
    problem.solve()