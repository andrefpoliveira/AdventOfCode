from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/14: Regolith Reservoir")
problem.preprocessor = ppr.lsv
  
def sign(x):
    return (x > 0) - (x < 0)

def find_below(obstacles, x, y, max_y, part2):
    for j in range(y, max_y+1):
        if (x,j) in obstacles: return(x,j-1)

    if part2:
        for j in range(max(y, max_y), max_y + 2):
            if (x,j) in obstacles: return(x,j-1)
        return (x, max_y + 1)
    return None

def is_stuck(obstacles, x, y, floor = None):
    if floor is not None and y == floor - 1: return True
    return (x-1,y+1) in obstacles and (x+1,y+1) in obstacles and (x,y+1) in obstacles

def create_obstacles(ls):
    obstacles = set()
    for l in ls:
        px = py = None
        
        for x,y in [map(int,x.split(",")) for x in l.split(" -> ")]:
            if px is None: obstacles.add((x,y))
            else:
                dx = sign(x - px)
                dy = sign(y - py)
                while x != px or y != py:
                    obstacles.add((px+dx,py+dy))
                    px,py=px+dx,py+dy
            px,py=x,y
    return obstacles

def solver(obstacles, part2 = False):
    deeper_height = max(x[1] for x in obstacles)
    count = 0
    while True:
        sand = (500,0)
        while True:
            sand = find_below(obstacles, *sand, deeper_height, part2)
            if sand is None: return count

            if is_stuck(obstacles, *sand, deeper_height + 2 if part2 else None): break

            if (sand[0] - 1, sand[1] + 1) not in obstacles:
                sand = (sand[0] - 1, sand[1] + 1)
            else:
                sand = (sand[0] + 1, sand[1] + 1)

        obstacles.add(sand)
        count += 1
        if (500,0) == sand: return count

@problem.solver(part=1)
def part1(ls):
    obstacles = create_obstacles(ls)
    return solver(obstacles)
    
@problem.solver(part=2)
def part2(ls):
    obstacles = create_obstacles(ls)
    return solver(obstacles, True)

if __name__ == "__main__":
    problem.solve()