from utils import problem
from utils import preprocessing as ppr
from utils import geometry

problem = problem.Problem("2021/15: Chiton")
problem.preprocessor = ppr.int_grid

def create_grid(grid):
    # Create Initial rows
    new_grid = []
    for row in grid:
        new_row = [x for x in row]
        for i in range(1, 5):
            for c in row:
                new_v = c + i
                if new_v > 9: new_v += 1
                new_row.append(new_v%10)
        new_grid.append(new_row)

    # Copy grid
    for i in range(1, 5):
        for row in range(0, len(grid)):
            new_row = []
            for c in new_grid[row]:
                new_v = c + i
                if new_v > 9: new_v += 1
                new_row.append(new_v%10)
            new_grid.append(new_row)
    return new_grid

def bfs(grid):
    stack = [((0,0), 0, [(0,0)])]
    visited = set()

    while len(stack) > 0:
        stack.sort(key=lambda x: x[1])
        coords, cost, path = stack.pop(0)
        
        if coords in visited: continue
        visited.add(coords)

        for c in geometry.get_neighbours(coords, 0, len(grid), len(grid[0]), geometry.NEIGHBOURS4):
            if c in path: continue
            if c == (len(grid)-1, len(grid[0])-1): return cost + grid[-1][-1]

            stack.append((c, cost + grid[c[0]][c[1]], path + [c]))
    return -1

@problem.solver()
def solver(grid):
    part1 = bfs(grid)
    grid = create_grid(grid)
    return part1, bfs(grid)


if __name__ == "__main__":
    problem.solve()