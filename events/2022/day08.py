from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/08: Treetop Tree House")
problem.preprocessor = ppr.int_grid

def is_visible(grid, x, y, coords, is_horizontal):
    size = len(grid)
    if x in (0, size - 1) or y in (0, size - 1): return True, 0

    visible, score = True, 0
    for coord in coords:
        score += 1
        if (grid[y][coord] if is_horizontal else grid[coord][x]) >= grid[y][x]:
            visible = False
            break

    return visible, score

@problem.solver()
def solver(grid):
    size = len(grid)
    
    visible = {}
    scores = {}

    for y in range(size):
        for x in range(size):
            coords = range(x-1,-1,-1), range(x+1,size), range(y-1,-1,-1), range(y+1,size)
            for coord, dir in zip(coords, [True, True, False, False]):
                vis, score = is_visible(grid, x, y, coord, dir)
                if not visible.get((x, y), False): visible[(x, y)] = vis
                scores[(x, y)] = scores.get((x, y), 1) * score

    return sum(visible.values()), max(scores.values())

if __name__ == "__main__":
    problem.solve()