from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo
problem = problem.Problem("2025/04: Printing Department")
problem.preprocessor = ppr.grid

def remove_paper(igrid):
    locs = []

    for (x, y), v in igrid.items():
        count = 0
        if not v: continue
        for (dx, dy) in geo.NEIGHBOURS8:
            nx, ny = x + dx, y + dy
            if (nx, ny) in igrid and igrid[(nx, ny)]:
                count += 1
        if count < 4:
            locs.append((x, y))
    return locs

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    igrid = {
        (x, y): inp[y][x] == '@'
        for y in range(len(inp))
        for x in range(len(inp[y]))
    }
    
    locs = remove_paper(igrid)
    p1 = len(locs)

    while locs:
        for (x, y) in locs:
            igrid[(x, y)] = False
        locs = remove_paper(igrid)
        if locs:
            p2 += len(locs)

    return p1, p1 + p2

if __name__ == "__main__":
    problem.solve()