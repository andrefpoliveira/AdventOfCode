from utils import problem

problem = problem.Problem("2019/03: Crossed Wires")
problem.preprocessor = lambda x: [l.split(",") for l in x.strip().split("\n")]



@problem.solver()
def solver(ls):
    visits = {}
    distances = {}
    dirs = {'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0)}

    for id, wire in enumerate(ls):
        x = y = 0
        count = 0
        f = []
        for dir in wire:
            dx, dy = dirs[dir[0]]
            amount = int(dir[1:])

            for _ in range(amount):
                count += 1
                x += dx
                y += dy
                if visits.get((x, y), 0) == id:
                    distances[(x, y)] = distances.get((x, y), 0) + count
                    visits[(x, y)] = id + 1

    intersections = [k for k, v in visits.items() if v > 1 and k != (0,0)]
    closest = sorted([abs(k[0]) + abs(k[1]) for k in intersections])[0]
    less_steps = sorted(distances[k] for k in intersections)[0]
    return closest, less_steps

if __name__ == "__main__":
    problem.solve()