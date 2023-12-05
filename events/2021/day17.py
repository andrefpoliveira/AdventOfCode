import re
from utils import problem
from utils import preprocessing as ppr
from utils import ntheory as nt

problem = problem.Problem("2021/17: Trick Shot")
problem.preprocessor = ppr.I

@problem.solver(part=1)
def part1(s):
    _, _, y, _ = [int(x) for x in re.findall("-?\d+", s)]
    return nt.triangular_number(abs(y)-1)

@problem.solver(part=2)
def part2(s):
    x1, x2, y1, y2 = [int(x) for x in re.findall("-?\d+", s)]

    possible = 0
    for initial_speed_x in range(1, x2+1):
        for initial_speed_y in range(-abs(y1), abs(y1)+1):
            current_speed_x = initial_speed_x
            current_speed_y = initial_speed_y
            x, y = 0, 0

            while True:
                if x > x2: break
                if y < y1: break

                x += current_speed_x
                y += current_speed_y

                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    possible += 1
                    break

                if current_speed_x != 0:
                    current_speed_x -= 1
                current_speed_y -= 1
    return possible

if __name__ == "__main__":
    problem.solve()