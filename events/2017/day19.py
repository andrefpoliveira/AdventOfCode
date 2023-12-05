from utils import problem

problem = problem.Problem("2017/19: A Series of Tubes")
problem.preprocessor = lambda x: [[x for x in r] for r in x.split("\n")]

def get_char(mtx, x, y):
    try: return mtx[x][y]
    except: return None

def get_dir(mtx, coords, curr_dir):
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if curr_dir == dir or curr_dir == (-x, -y): continue
        if get_char(mtx, coords[0] + x, coords[1] + y) not in [None, ' ']:
            return (x, y)
    return None

@problem.solver()
def part1(mtx):
    dir = (1, 0)
    count = 0
    coords = (0, mtx[0].index('|'))
    letters = ""

    while True:
        char = mtx[coords[0]][coords[1]]

        if char == ' ': break

        if char not in ['|', '-', '+']:
            letters += char
        elif char == '+':
            dir = get_dir(mtx, coords, dir)

        curr_pos = (coords[0] + dir[0], coords[1] + dir[1])
        count += 1
        coords = curr_pos
    
    return letters, count

if __name__ == "__main__":
    problem.solve()