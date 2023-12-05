from utils import problem
from utils import preprocessing as ppr
from utils import geometry

problem = problem.Problem("2021/09: Smoke Basin")
problem.preprocessor = ppr.int_grid

coords = []

@problem.solver(part=1)
def part1(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            v = grid[i][j]
            for x, y in geometry.get_neighbours((i, j), 0, len(grid), len(grid[0]), geometry.NEIGHBOURS4):
                if v >= grid[x][y]: break
            else:
                total += v + 1
                coords.append((i, j))
    return total

@problem.solver(part=2)
def part2(grid):
    sizes = []
    for i, j in coords:
        pos = [(i, j)]
        visited = set()
        size = 0

        while len(pos) > 0:
            c = pos.pop(0)

            if c in visited: continue
            visited.add(c)

            v = grid[c[0]][c[1]]
            size += 1

            for n in geometry.get_neighbours((c[0], c[1]), 0, len(grid), len(grid[0]), geometry.NEIGHBOURS4):
                if n in visited: continue
                if grid[n[0]][n[1]] > v and grid[n[0]][n[1]] != 9:
                    pos.append(n)

        sizes.append(size)

    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]

if __name__ == "__main__":
    problem.solve()
