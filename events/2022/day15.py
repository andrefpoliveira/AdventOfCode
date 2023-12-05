from utils import problem
from utils import geometry as geo

import re

problem = problem.Problem("2022/15: Beacon Exclusion Zone")
problem.preprocessor = lambda x: [map(int,re.findall(r'(-?\d+)', l)) for l in x.splitlines()]

@problem.solver(part=1)
def part1(ls):
    target = 2000000
    occupied = set()
    sens_beacons = set()

    for sx,sy,bx,by in ls:
        sens_beacons.add((sx,sy))
        sens_beacons.add((bx,by))

        distance = geo.manhattan((sx,sy), (bx,by))
        diff = abs(sy - target)

        if diff > distance: continue

        sides = distance - diff
        for x in range(sx - sides, sx + sides + 1):
            occupied.add((x, target))

    return len(occupied - sens_beacons)    

@problem.solver(part=2)
def part2(ls):
    size = 4000000
    grid = [[] for _ in range(size + 1)]

    for sx,sy,bx,by in ls:
        distance = geo.manhattan((sx, sy), (bx, by))
        dy = 0
        while distance > 0:
            start_x = max(0, sx - distance)
            end_x = min(size, sx + distance)
            if sy - dy >= 0: grid[sy - dy].append([start_x, end_x])
            if sy + dy <= size and dy != 0: grid[sy + dy].append([start_x, end_x])

            dy += 1
            distance -= 1

    for y in range(size+1):
        row = grid[y]
        row.sort()
        # print(row)

        if row[0][0] != 0:
            x = 0
            break
    
        start, end = row[0]
        for i in range(len(row)):
            cs, ce = row[i]
            if end >= cs - 1: end = max(end, ce)
            else: break

        if size != end:
            x = end + 1
            break

    
    return 4000000 * x + y

if __name__ == "__main__":
    problem.solve()