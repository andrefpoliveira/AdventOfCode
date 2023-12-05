from hashlib import md5
from utils import problem
from utils import geometry
from utils import preprocessing as ppr

problem = problem.Problem("2016/17: Two Steps Forward")
problem.preprocessor = ppr.I

def door_is_open(c):
    return c in ["b", "c", "d", "e", "f"]

@problem.solver()
def solve(s):
    x, y = 0, 0
    stack = [(x, y, "")]
    part1, part2 = None, 0

    while stack:
        stack.sort(key = lambda x: len(x[2]))
        cx, cy, path = stack.pop(0)

        if cx == 3 and cy == 3:
            if part1 == None:
                part1 = path
                part2 = len(path)
            part2 = max(part2, len(path))
            continue

        h = md5(f"{s}{path}".encode()).hexdigest()

        open_doors = [door_is_open(h[0]), door_is_open(h[1]), door_is_open(h[2]), door_is_open(h[3])]
        dirs = ["U", "D", "L", "R"]

        for id, d in enumerate([[-1,0], [1,0], [0,-1], [0,1]]):
            dx, dy = d
            tx = dx + cx
            ty = dy + cy

            if tx < 0 or tx >= 4 or ty < 0 or ty >= 4: continue
            if open_doors[id]:
                stack.append((tx, ty, path + dirs[id]))

    return part1, part2

if __name__ == "__main__":
    problem.solve()