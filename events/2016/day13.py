from utils import problem
from utils import preprocessing as ppr
from utils import geometry

problem = problem.Problem("2016/13: A Maze of Twisty Little Cubicles")
problem.preprocessor = ppr.intI

def is_wall(x, y, fav_n):
    return sum(int(x) for x in bin(x*x + 3*x + 2*x*y + y + y*y + fav_n)[2:]) % 2 != 0

def distance(x, y, tx, ty):
    return abs(x - tx) + abs(y - ty)

@problem.solver()
def solve(fav_n):
    dest_x, dest_y = (31, 39)
    seen = set()
    queue = [(1, 1, 0, 0)] # x, y, distance, steps
    count = 0

    while queue:
        queue.sort(key = lambda x: (x[3], x[2]))
        current_x, current_y, _, steps = queue.pop(0)

        if steps < 50: count += 1

        for cx, cy in geometry.get_neighbours((current_x, current_y), 0, float("Inf"), float("Inf"), geometry.NEIGHBOURS4):
            if (cx, cy) in seen: continue
            seen.add((cx, cy))
            if cx == dest_x and cy == dest_y: return steps + 1, count

            if not is_wall(cx, cy, fav_n):
                queue.append((cx, cy, distance(cx, cy, dest_x, dest_y), steps+1))
    return -1

if __name__ == "__main__":
    problem.solve()