from utils import problem
from utils import geometry as geo

problem = problem.Problem("2018/06: Chronal Coordinates")
problem.preprocessor = lambda x: [list(map(int, l.split(", "))) for l in x.split("\n")]

@problem.solver(part=1)
def part1(ls):
    d = {}
    
    x_coords = [l[0] for l in ls]
    y_coords = [l[1] for l in ls]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    for id, c in enumerate(ls):
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                _, best_dist = d.get((x, y), [None, None])
                dist = geo.manhattan(c, (x, y))

                if best_dist is None:
                    d[(x, y)] = [id, dist]
                elif dist > best_dist:
                    continue
                elif dist == best_dist:
                    d[(x, y)] = [-1, dist]
                else:
                    d[(x, y)] = [id, dist]

    ids = [x for x in range(len(ls))]
    
    for x in range(min_x, max_x + 1):
        for y in [min_y, max_y]:
            id, _ = d.get((x, y), [None, None])
            if id in ids:
                ids.remove(id)

    for y in range(min_y, max_y + 1):
        for x in [min_x, max_x]:
            id, _ = d.get((x, y), [None, None])
            if id in ids:
                ids.remove(id)

    count = 0
    for id in ids:
        curr_count = sum(True for x in d.values() if x[0] == id)
        count = max(count, curr_count)
    return count

@problem.solver(part=2)
def part2(ls): 
    x_coords = [l[0] for l in ls]
    y_coords = [l[1] for l in ls]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    count = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            dist = sum(geo.manhattan(c, (x, y)) for c in ls)

            if dist < 10000:
                count += 1

    return count

if __name__ == "__main__":
    problem.solve()