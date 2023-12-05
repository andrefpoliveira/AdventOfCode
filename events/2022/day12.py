from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/12: Hill Climbing Algorithm")
problem.preprocessor = ppr.grid

def parse_input(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                S = (x,y)
                grid[y][x]='a'
            if grid[y][x] == 'E':
                E = (x,y)
                grid[y][x]='z'
    return S, E

def solver(grid, start, end, part2=False):
    queue = [(start, 0)]
    added = set([start])

    while queue:
        queue.sort(key=lambda x: x[1])
        c, depth = queue.pop(0)

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            x, y = c[0]+dx,c[1]+dy

            if x<0 or x>=len(grid[0]) or y<0 or y>=len(grid): continue

            if (x,y) in added: continue

            if ord(grid[y][x]) - ord(grid[c[1]][c[0]]) <-1: continue

            if part2 and grid[y][x] == "a": return depth+1
            if not part2 and (x, y) == end: return depth+1

            queue.append(((x,y),depth+1))
            added.add((x,y))
  
@problem.solver(part=1)
def part1(g):
    s, e = parse_input(g)
    return solver(g, e, s)

@problem.solver(part=2)
def part2(g):
    s, e = parse_input(g)
    return solver(g, e, s, True)

if __name__ == "__main__":
    problem.solve()