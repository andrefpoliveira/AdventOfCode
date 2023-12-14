from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2023/14: Parabolic Reflector Dish")
problem.preprocessor = ppr.grid

def tilt_north(grid):
    for x in range(len(grid[0])):
        dy = 0
        for y in range(len(grid)):
            if grid[y][x] == "#":
                dy = 0
            elif grid[y][x] == ".":
                dy += 1
            else:
                grid[y][x] = "."
                grid[y-dy][x] = "O"

def tilt_south(grid):
    for x in range(len(grid[0])):
        dy = 0
        for y in range(len(grid)-1, -1, -1):
            if grid[y][x] == "#":
                dy = 0
            elif grid[y][x] == ".":
                dy += 1
            else:
                grid[y][x] = "."
                grid[y+dy][x] = "O"

def tilt_west(grid):
    for y in range(len(grid)):
        dx = 0
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                dx = 0
            elif grid[y][x] == ".":
                dx += 1
            else:
                grid[y][x] = "."
                grid[y][x-dx] = "O"

def tilt_east(grid):
    for y in range(len(grid)):
        dx = 0
        for x in range(len(grid[0])-1, -1, -1):
            if grid[y][x] == "#":
                dx = 0
            elif grid[y][x] == ".":
                dx += 1
            else:
                grid[y][x] = "."
                grid[y][x+dx] = "O"

def calculate_load(grid):
    load = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                load += len(grid) - y
    return load

def grid_to_hash(grid):
    return hash("".join(["".join(row) for row in grid]))

@problem.solver(part=1)
def part1(grid):
    tilt_north(grid)
    return calculate_load(grid)

@problem.solver(part=2)
def part2(grid):
    loads = [0]
    seen = [0]

    while True:
        tilt_north(grid)
        tilt_west(grid)
        tilt_south(grid)
        tilt_east(grid)

        h = grid_to_hash(grid)
        loads.append(calculate_load(grid))

        if h in seen:
            break

        seen.append(h)

    current_index = seen.index(h)
    cycle = len(seen) - current_index

    return loads[(1000000000 - current_index) % cycle + current_index]
    



if __name__ == "__main__":
    problem.solve()