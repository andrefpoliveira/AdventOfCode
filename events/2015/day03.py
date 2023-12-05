from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/03: Perfectly Spherical Houses in a Vacuum")
problem.preprocessor = ppr.I

@problem.solver(part=1)
def part1(input_text):
    x,y = 0,0
    visited = set()
    visited.add((0,0))
    d = {">": [0,1], "<": [0,-1], "v": [-1,0], "^": [1,0]}
    for i in input_text:
        x += d[i][0]
        y += d[i][1]
        visited.add((x,y))
    return len(visited)

@problem.solver(part=2)
def part2(input_text):
    x,y = 0,0
    x2,y2 = 0,0
    visited = set()
    visited.add((0,0))
    d = {">": [0,1], "<": [0,-1], "v": [-1,0], "^": [1,0]}
    for idx, i in enumerate(input_text):
        if idx % 2 == 0:
            x += d[i][0]
            y += d[i][1]
            visited.add((x,y))
        else:
            x2 += d[i][0]
            y2 += d[i][1]
            visited.add((x2,y2))

    return len(visited)

if __name__ == "__main__":
    problem.solve()