from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/02: Bathroom Security")
problem.preprocessor = ppr.lsv

def find_comb(lines, buttons):
    x, y, res = 1, 1, ""
    d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    for line in lines:
        for dir in line:
            x += d[dir][0]
            y += d[dir][1]

            if x < 0 or x >= len(buttons) or y < 0 or y >= len(buttons) or buttons[x][y] == "#":
                x -= d[dir][0]
                y -= d[dir][1]

        res += buttons[x][y]
    return res

@problem.solver()
def solve(ls):
    bt1 = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    bt2 = [['#', '#', '1', '#', '#'], ['#', '2', '3', '4', '#'], ['5', '6', '7', '8', '9'], ['#', 'A', 'B', 'C', '#'], ['#', '#', 'D', '#', '#']]
    return find_comb(ls, bt1), find_comb(ls, bt2)

if __name__ == "__main__":
    problem.solve()