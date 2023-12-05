from utils import problem
from utils import preprocessing as ppr

from itertools import permutations

problem = problem.Problem("2016/24: Air Duct Spelunking")
problem.preprocessor = ppr.grid

def distance(x, y, tx, ty): return abs(x - tx) + abs(y -ty)

def find_shortest_path(start, end, grid):
    queue = [(start, 0)]
    seen = set()

    while queue:
        queue.sort(key=lambda x: (x[1], distance(*x[0], *end)))
        current_pos, steps = queue.pop(0)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            x, y = current_pos[0] + dx, current_pos[1] + dy

            if grid[y][x] == "#": continue
            if (x, y) == end: return steps + 1

            if (x, y) not in seen:
                seen.add((x, y))
                queue.append(((x,y), steps+1))

def get_distances(start, points, grid):
    d = dict()
    for id, p in enumerate(points):
        dist = find_shortest_path(start, p, grid)
        d[f'start-{id+1}'] = dist
        d[f'{id+1}-start'] = dist
    for id1, p1 in enumerate(points):
        for id2, p2 in enumerate(points):
            if id1 == id2: continue
            d[f'{id1+1}-{id2+1}'] = find_shortest_path(p1, p2, grid)
    return d

@problem.solver(part=1)
def part1(grid):
    start = [(x,y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == '0'][0]
    points = [(x,y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] not in ['0', '#', '.']]
    d = get_distances(start, points, grid)
    
    shortest = float("inf")
    perms = permutations([str(x+1) for x in range(len(points))], len(points))
    for p in perms:
        p = ('start',) + p
        current = sum([d[f"{p[i-1]}-{p[i]}"] for i in range(1, len(p))])
        if current < shortest: shortest = current
    
    return shortest

@problem.solver(part=2)
def part2(grid):
    start = [(x,y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == '0'][0]
    points = [(x,y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] not in ['0', '#', '.']]
    d = get_distances(start, points, grid)
    
    shortest = float("inf")
    perms = permutations([str(x+1) for x in range(len(points))], len(points))
    for p in perms:
        p = ('start',) + p + ('start',)
        current = sum([d[f"{p[i-1]}-{p[i]}"] for i in range(1, len(p))])
        if current < shortest: shortest = current
    
    return shortest


if __name__ == "__main__":
    problem.solve()