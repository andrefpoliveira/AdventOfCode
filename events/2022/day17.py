from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/17: Pyroclastic Flow")
problem.preprocessor = ppr.I

ROCKS = [
    (4, (15,)),
    (3, (2, 7, 2,)),
    (3, (7, 4, 4)),
    (1, (1, 1, 1, 1,)),
    (2, (3, 3,))
]

def is_free(rock, lines, x, y):
    return all(not (line & row << x) for line, row in zip(lines[y:], rock))

def get_visible(rows):
    visible, queue = [0] * len(rows) + [1], [(0, len(rows))]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            x2, y2 = x + dx, y + dy
            if (x2 in range(7) and y2 in range(len(visible)) and not (visible[y2] & 1 << x2)):
                visible[y2] |= 1 << x2
                if not (y2 < len(rows) and rows[y2] & 1 << x2):
                    queue.append((x2, y2))
    return visible

def place_rock(width, rock, dirs, dir_id, height, rows):
    x, y = 2, len(rows) + 3
    while is_free(rock, rows, x, y):
        dx =  {"<":-1, ">":1}[dirs[dir_id]]
        dir_id = (dir_id + 1) % len(dirs)

        if 0 <= x + dx <= 7 - width and is_free(rock, rows, x + dx, y):
            x = x + dx

        y -= 1

    y += 1
    for id, row in enumerate(rock):
        if y + id >= len(rows):
            rows.append(row << x)
            height += 1
        else:
            rows[y + id] = rows[y + id] | (row << x)

    visible = get_visible(rows)
    rows = [line & row for line, row in zip(visible, rows)]

    trim = 0
    while not rows[trim]:
        trim += 1

    return dir_id, height, rows[trim:]

def solve(dirs, pieces):
    dir_id, height, rows = 0, 0, [127]
    seen, heights = {}, []
    for i in range(pieces):
        rock_id = i % len(ROCKS)
        width, rock = ROCKS[rock_id]

        j = seen.setdefault((tuple(rows), dir_id, rock_id), i)
        if j < i:
            return heights[j + (pieces - j) % (i - j)] + (pieces - j) // (i - j) * (height - heights[j])

        heights.append(height)
        dir_id, height, rows = place_rock(width, rock, dirs, dir_id, height, rows)

    return height

@problem.solver(part=1)
def part1(s):
    return solve(s, 2022)   

@problem.solver(part=2)
def part2(s):
    return solve(s, 1000000000000)

if __name__ == "__main__":
    problem.solve()