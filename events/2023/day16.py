from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2023/16: The Floor Will Be Lava")
problem.preprocessor = ppr.grid

def get_energized(grid, start, direction):
    energized = set()
    beams = [(start, direction)]

    while beams:
        b = beams.pop(0)

        while True:
            if not(0 <= b[0][0] < len(grid[0]) and 0 <= b[0][1] < len(grid)): break

            if b in energized: break
            energized.add(b)

            (x, y), (dx, dy) = b

            if grid[y][x] == "/":
                dx, dy = -dy, -dx
            elif grid[y][x] == "\\":
                dx, dy = dy, dx
            elif grid[y][x] == "|" and dy == 0:
                beams.append(((x, y-1), (0, -1)))
                beams.append(((x, y+1), (0, 1)))
                break
            elif grid[y][x] == "-" and dx == 0:
                beams.append(((x-1, y), (-1, 0)))
                beams.append(((x+1, y), (1, 0)))
                break

            b = ((x + dx, y + dy), (dx, dy))

    return len(set([b[0] for b in energized]))

@problem.solver(part=1)
def part1(grid):
    return get_energized(grid, (0, 0), (1, 0))

@problem.solver(part=2)
def part2(grid):
    part2 = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if y == 0: part2 = max(part2, get_energized(grid, (x, y), (0, 1)))
            if y == len(grid) - 1: part2 = max(part2, get_energized(grid, (x, y), (0, -1)))
            if x == 0: part2 = max(part2, get_energized(grid, (x, y), (1, 0)))
            if x == len(grid[0]) - 1: part2 = max(part2, get_energized(grid, (x, y), (-1, 0)))
    return part2

if __name__ == "__main__":
    problem.solve()