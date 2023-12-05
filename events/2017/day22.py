from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/22: Sporifica Virus")
problem.preprocessor = ppr.grid

def get_points(grid, infected_value):
    mid = len(grid) // 2
    points = {}
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "#":
                points[(i - mid, j - mid)] = infected_value
    return points

@problem.solver(part=1)
def part1(grid):
    count, dir_idx = 0, 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    points = get_points(grid, 1)
    x, y = 0, 0

    for _ in range(10000):
        state = points.get((x, y), 0)
        if state:
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx - 1) % 4
            count += 1

        points[(x, y)] = (state + 1) % 2

        dir = dirs[dir_idx]
        x += dir[0]
        y += dir[1]

    return count

def build_grid(points, pos):
    xs = [x[0] for x in points] + [pos[0]]
    ys = [x[1] for x in points] + [pos[1]]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)

    letter = [".", "W", "#", "F"]
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) == pos:
                print("[" + letter[points.get((x, y), 0)] + "]", end="")
            else:
                print(" " + letter[points.get((x, y), 0)] + " ", end="")
        print()
    print()

@problem.solver(part=2)
def part2(grid):
    count, dir_idx = 0, 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    points = get_points(grid, 2)
    x, y = 0, 0

    for _ in range(10000000):
        state = points.get((x, y), 0)
        if state == 0:
            dir_idx = (dir_idx - 1) % 4
        elif state == 1:
            count += 1
        elif state == 2: 
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx + 2) % 4
            
        points[(x, y)] = (state + 1) % 4

        dir = dirs[dir_idx]
        x += dir[0]
        y += dir[1]

    return count

if __name__ == "__main__":
    problem.solve()