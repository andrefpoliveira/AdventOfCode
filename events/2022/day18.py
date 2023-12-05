from utils import problem
from utils import geometry as geo

problem = problem.Problem("2022/18: Boiling Boulders")
problem.preprocessor = lambda s: [tuple(int(n) for n in x.split(","))
        for x in s.strip().split("\n")]

def is_outside(cube, adjacent, middle):
    return geo.euclidean(cube, middle) < geo.euclidean(adjacent, middle)

@problem.solver(part=1)
def part1(ls):
    visited = [False for _ in ls]
    count = 0

    while not all(visited):
        id = visited.index(False)
        queue = [ls[id]]
        visited[id] = True

        while queue:
            x, y, z = queue.pop(0)
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                c = (x+dx, y+dy, z+dz)

                if c not in ls: count += 1

                elif not visited[ls.index(c)]:
                    queue.append(c)
                    visited[ls.index(c)] = True

    return count

@problem.solver(part=2)
def part2(ls):
    count = 0

    queue = [(0,0,0)]
    added = {(0,0,0)}
    while queue:
        x, y, z = queue.pop(0)

        for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            c = (x+dx, y+dy, z+dz)

            if -1 <= c[0] <= 22 and -1 <= c[1] <= 22 and -1 <= c[2] <= 22 and c not in added:
                if c in ls: count += 1
                else:
                    queue.append(c)
                    added.add(c)

    return count

if __name__ == "__main__":
    problem.solve()