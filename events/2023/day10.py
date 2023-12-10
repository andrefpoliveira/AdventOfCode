from utils import problem
from utils import preprocessing as ppr

from math import ceil

problem = problem.Problem("2023/10: Pipe Maze")
problem.preprocessor = ppr.grid

def build_graph(grid):
    g = {}
    s = None
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "|": g[(x,y)] = [(x,y+1), (x, y-1)]
            elif c == "-": g[(x,y)] = [(x+1,y), (x-1, y)]
            elif c == "L": g[(x,y)] = [(x+1, y), (x, y-1)]
            elif c == "J": g[(x,y)] = [(x-1, y), (x, y-1)]
            elif c == "F": g[(x,y)] = [(x+1, y), (x, y+1)]
            elif c == "7": g[(x,y)] = [(x-1, y), (x, y+1)]
            elif c == "S": s = (x,y)

    return g, s

def explore(g, start):
    entry_points = [k for k,v in g.items() if start in v]
    for p in entry_points:
        path = []
        previous = start
        while p not in path and p != start:
            path.append(p)
            previous, p = p, g[p][0] if g[p][1] == previous else g[p][1]
        if p == start:
            return path

@problem.solver()
def solver(grid):
    g, s = build_graph(grid)
    path = explore(g, s)

    points = 0
    for y, row in enumerate(grid):
        inside = False
        for x, c in enumerate(row):
            if (x, y) in path + [s]:
                if c in '|LJ':
                    inside = not inside
                continue
            if inside: 
                points += 1

    return ceil(len(path) / 2), points

if __name__ == "__main__":
    problem.solve()