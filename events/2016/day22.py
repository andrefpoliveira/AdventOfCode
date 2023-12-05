from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2016/22: Grid Computing")
problem.preprocessor = ppr.lsv

d = dict()

@problem.solver(part=1)
def part1(ls):
    global d
    for l in ls:
        if l[0] != "/": continue
        x, y, _, used, avail, _ = [int(x) for x in re.findall(r"\d+", l)]
        d[(x,y)] = {'used': used, 'avail': avail}

    pairs = 0
    values = list(d.values())

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i]['used'] > 0 and values[i]['used'] <= values[j]['avail']: pairs += 1
            if values[j]['used'] > 0 and values[j]['used'] <= values[i]['avail']: pairs += 1
    return pairs

def find_path(max_x, max_y, start, end, obst=None):
    for value in d.values():
        value['dist'] = float('inf')
        value['prev'] = None

    queue = [start]
    d[start]['dist'] = 0
    while queue:
        n = queue.pop(0)
        nx, ny = n
        for x, y in [(nx+1, ny), (nx-1, ny), (nx, ny+1), (nx, ny-1)]:
            if 0 <= x < max_x and 0 <= y < max_y and d[(x, y)]['used'] < 100 and (x, y) != obst:
                if d[(x, y)]['dist'] > d[n]['dist'] + 1:
                    d[(x, y)]['dist'] = d[n]['dist'] + 1
                    d[(x, y)]['prev'] = n
                    queue.append((x, y))
                if (x, y) == end:
                    path = [(x, y)]
                    while d[path[-1]]['prev'] != None:
                        path.append(d[path[-1]]['prev'])
                    return path[-2::-1]

@problem.solver(part=2)
def part2(ls):
    global d
    
    max_x = max([val[0] for val in d.keys()])+1
    max_y = max([val[1] for val in d.keys()])+1
    start = (0, 0)
    goal = (max_x - 1, 0)
    empty = [key for key in d if d[key]['used'] == 0][0]

    pathGS = find_path(max_x, max_y, goal, start)
    res = 0
    while goal != start:
        path = find_path(max_x, max_y, empty, pathGS.pop(0), obst=goal)
        res += len(path) + 1
        empty = goal
        goal = path[-1]

    return res

if __name__ == "__main__":
    problem.solve()