from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo

import heapq

problem = problem.Problem("2023/17: Clumsy Crucible")
problem.preprocessor = ppr.int_grid

def dijkstra_modified(grid, min_consecutive, max_consecutive):
    visited = set()
    queue = [(0, (0, 0), (1, 0), 1), (0, (0, 0), (0, 1), 1)]

    while queue:
        cost, coords, direction, consecutive = heapq.heappop(queue)
        if (coords, direction, consecutive) in visited: continue
        
        visited.add((coords, direction, consecutive))

        cx = coords[0] + direction[0]
        cy = coords[1] + direction[1]

        if not(0 <= cx < len(grid[0]) and 0 <= cy < len(grid)): continue

        _cost = cost + grid[cy][cx]
        if min_consecutive <= consecutive <= max_consecutive and (cx, cy) == (len(grid[0]) - 1, len(grid) - 1):
            return _cost
        
        for dx, dy in geo.NEIGHBOURS4:
            if (dx, dy) == (-direction[0], -direction[1]): continue
            new_consecutive = consecutive + 1 if (dx, dy) == direction else 1

            if ((dx, dy) != direction and consecutive < min_consecutive) or new_consecutive > max_consecutive: continue

            heapq.heappush(queue, (_cost, (cx, cy), (dx, dy), new_consecutive))


@problem.solver(part=1)
def part1(grid):
    return dijkstra_modified(grid, 1, 3)

@problem.solver(part=2)
def part2(grid):
    return dijkstra_modified(grid, 4, 10)

if __name__ == "__main__":
    problem.solve()