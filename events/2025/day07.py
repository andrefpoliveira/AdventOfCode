from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2025/07: Laboratories")
problem.preprocessor = ppr.grid

def build_map(grid):
    start = (0, 0)
    _map = set()

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                start = (r, c)
            elif val == '^':
                _map.add((r, c))
    return start, _map

def explore_map(_map, beams, level = 0):
    p1 = 0

    while level <= max(r for r, c in _map) + 1:
        new_beams = {}

        for c in beams:
            if (level, c) in _map:
                new_beams[c - 1] = new_beams.get(c - 1, 0) + beams[c]
                new_beams[c + 1] = new_beams.get(c + 1, 0) + beams[c]
                p1 += 1
            else:
                new_beams[c] = new_beams.get(c, 0) + beams[c]
        beams = new_beams

        level += 1

    return p1, sum(beams.values())

@problem.solver()
def solver(inp):
    start, _map = build_map(inp)
    beams = {start[1]: 1}

    return explore_map(_map, beams.copy())

if __name__ == "__main__":
    problem.solve()