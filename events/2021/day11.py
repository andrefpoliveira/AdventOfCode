from utils import problem
from utils import preprocessing as ppr
from utils import geometry

problem = problem.Problem("2021/11: Dumbo Octopus")
problem.preprocessor = ppr.int_grid

def process_round(grid):
    blinks, blinking = 0, []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                blinking.append((i, j))

    visited = set()
    while len(blinking) > 0:
        b = blinking.pop()
        if b in visited: continue

        visited.add(b)
        blinks += 1
        l = [b]
        while len(l) > 0:
            current = l.pop()
            for x, y in geometry.get_neighbours(current, 0, len(grid), len(grid), geometry.NEIGHBOURS8):
                grid[x][y] += 1
                if grid[x][y] > 9 and (x, y) not in visited:
                    blinking.append((x, y))
            
                    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                grid[i][j] = 0
    return blinks

@problem.solver(part=1)
def part1(grid):
    blinks = 0
    for _ in range(100):
        blinks += process_round(grid)
    return blinks

@problem.solver(part=2)
def part2(grid):
    turn = 1
    while True:
        process_round(grid)
        if len(set([x for row in grid for x in row])) == 1: return turn
        turn += 1

if __name__ == "__main__":
    problem.solve()
