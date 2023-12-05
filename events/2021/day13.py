from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/13: Transparent Origami")
problem.preprocessor = ppr.lsv

def print_grid(points):
    rows = max(x[1] for x in points)+1
    cols = max(x[0] for x in points)+1
    grid = [["." for _ in range(cols)] for _ in range(rows)]

    for point in points:
        grid[point[1]][point[0]] = "#"

    for i in grid:
        print(''.join(i))

def fold(points, instrs):
    res = 0
    for inst in instrs:
        new_points = set()
        value = int(inst.split("=")[1])
        
        if "y" in inst:
            for x, y in points:
                if y < value:
                    new_points.add((x, y))
                elif y > value and y <= value*2:
                    new_points.add((x, y - abs(y - value) * 2))
        else:
            for x, y in points:
                if x < value:
                    new_points.add((x, y))
                elif x > value and x <= value*2:
                    new_points.add((x - abs(x - value) * 2, y))
        points = new_points
        if res == 0:
            res = len(points)

    print_grid(points)

    return res

@problem.solver()
def solver(ls):
    points = set()
    instrs = []
    is_inst = False

    for l in ls:
        if l == "":
            is_inst = True
            continue
        elif is_inst:
            instrs.append(l)
        else:
            x, y = int(l.split(",")[0]), int(l.split(",")[1])
            points.add((x, y))
            
    return fold(points, instrs)

if __name__ == "__main__":
    problem.solve()