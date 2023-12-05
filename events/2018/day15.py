from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/15: Beverage Bandits")
problem.preprocessor = ppr.lsv

def print_board(entities, walls):
    max_x, max_y = max(x[0] for x in walls), max(x[1] for x in walls)
    for y in range(max_y + 1):
        ent = []
        for x in range(max_x + 1):
            if (x, y) in walls: print("#", end="")
            else:
                for e in entities:
                    if e.get_coords() == (x, y):
                        print("G" if type(e) == Goblin else "E", end="")
                        ent.append(e)
                        break
                else:
                    print(".", end="")

        print('\t' + ', '.join([str(e) for e in ent]))

class Entity:
    def __init__(self, target, x, y):
        self.target = target
        self.x = x
        self.y = y
        self.life = 200

    def __eq__(self, other):
        return self.get_coords() == other.get_coords()

    def get_coords(self):
        return (self.x, self.y)
    
    def get_adjacent_coords(self, walls, entities):
        for dx, dy in [(0,-1), (-1,0), (1,0), (0,1)]:
            x, y = self.x + dx, self.y + dy
            if (x, y) in walls: continue
            for e in entities:
                if e == self: continue
                if e.get_coords() == (x, y): break
            else:
                yield (x, y)
    
    def attack(self, entities):
        targets = []
        for dx, dy in [(0,-1), (-1,0), (1,0), (0,1)]:
            x, y = self.x + dx, self.y + dy
            for e in entities:
                if type(self) == type(e): continue
                if e.get_coords() == (x, y):
                    targets.append(e)
        if not targets: return False
        targets.sort(key=lambda x: x.life)
        targets[0].life -= 3
        return True
    
    def get_path(self, target, paths):
        possible_steps = []
        queue = [target]
        while queue:
            current = queue.pop(0)
            parents = paths[current]
            if (self.x, self.y) in parents:
                possible_steps.append(current)
                continue

            for p in parents:
                queue.append(p)

        possible_steps.sort(key=lambda x: (x[1], x[0]))
        return possible_steps[0]

    def take_action(self, grid, entities):
        if self.attack(entities): return
                
        inserted = [(self.x, self.y)]
        queue = [(self.x, self.y, 0)]

        distances = dict()
        distances[(self.x, self.y)] = 0

        path = dict()
        path[(self.x, self.y)] = None

        entity_coords = [e.get_coords() for e in entities]

        # Create a distance map
        while queue:
            queue.sort(key = lambda x: (x[2], x[1], x[0]))
            cx, cy, depth = queue.pop(0)

            for dx, dy in [(0,-1), (-1,0), (1,0), (0,1)]:
                x, y = cx + dx, cy + dy
                if (x, y) in grid: continue
                if (x, y) in entity_coords: continue

                if (x, y) in inserted:
                    if distances[(x, y)] == depth + 1:
                        path[(x, y)] = path.get((x, y), []) + [(cx, cy)]
                else:
                    queue.append((x, y, depth + 1))
                    inserted.append((x, y))
                    distances[(x, y)] = depth + 1
                    path[(x, y)] = [(cx, cy)]

        # Get all the reachable targets
        reachable_squares = []
        for e in entities:
            if e == self: continue
            if type(e) == type(self): continue
            for c in e.get_adjacent_coords(grid, entities):
                if c in distances:
                    reachable_squares.append((c, distances[c]))

        if not reachable_squares: return

        # Calculate the closest ones
        min_distance = min(x[1] for x in reachable_squares)
        reachable_squares = [x for x in reachable_squares if x[1] == min_distance]

        # Calculate the target based on position
        reachable_squares.sort(key=lambda x: (x[0][1], x[0][0]))
        target = reachable_squares[0][0]

        # Get the first step
        step = self.get_path(target, path)

        self.x, self.y = step
        self.attack(entities)

class Goblin(Entity):
    def __init__(self, x, y):
        super().__init__("E", x, y)

    def __repr__(self):
        return f"G({self.life}) ({self.x}, {self.y})"
    
    def copy(self):
        return Goblin(self.x, self.y)

class Elf(Entity):
    def __init__(self, x, y):
        super().__init__("G", x, y)

    def __repr__(self):
        return f"E({self.life}) ({self.x}, {self.y})"
    
    def copy(self):
        return Elf(self.x, self.y)


def create_grid(ls):
    entities = []
    walls = set()
    for y, line in enumerate(ls):
        for x, c in enumerate(line):
            if c == "#": walls.add((x, y))
            elif c == "E": entities.append(Elf(x, y))
            elif c == "G": entities.append(Goblin(x, y))

    return entities, walls

@problem.solver(part=1)
def part1(ls):
    entities, walls = create_grid(ls)

    rounds = 0
    while len(set(type(e) for e in entities)) > 1:

        print(f"\n--- ROUND {rounds} ---")
        # print_board(entities, walls)

        entities.sort(key = lambda e: (e.y, e.x))
        
        for e in entities:
            if e.life > 0:
                e.take_action(walls, entities)

        entities = [e for e in entities if e.life > 0]

        rounds += 1

    print(f"\n--- ROUND {rounds} ---")
    print_board(entities, walls)

    entities.sort(key = lambda e: (e.y, e.x))
    print(entities)
    print(rounds)

    return rounds * sum(e.life for e in entities)

if __name__ == "__main__":
    problem.solve()