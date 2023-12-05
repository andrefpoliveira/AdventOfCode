from utils import problem

problem = problem.Problem("2018/13: Mine Cart Madness")
problem.preprocessor = lambda s: s.split("\n")

class Cart:
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.previous_coords = None
        self.crashed = False

        self.dir_id = 0
        self.dirs = [
            lambda x, y: (y, -x),
            lambda x, y: (x, y),
            lambda x, y: (-y, x)
        ]

    def get_coords(self):
        return (self.x, self.y)

    def make_turn(self, graph):
        corner = graph[self.get_coords()]
        if corner == "\\":
            self.dx, self.dy = self.dy, self.dx
        elif corner == "/":
            self.dx, self.dy = -self.dy, -self.dx
        else:
            self.dx, self.dy = self.dirs[self.dir_id](self.dx, self.dy)
            self.dir_id = (self.dir_id + 1) % 3

    def move(self):
        self.previous_coords = self.get_coords()
        self.x += self.dx
        self.y += self.dy

    def __repr__(self):
        return f"Car: ({self.x}, {self.y})"

def build_graph(ls):
    graph, carts = {}, []

    dirs = {">": (1,0), "<": (-1,0), "^": (0,-1), "v": (0,1)}

    for y, l in enumerate(ls):
        for x, c in enumerate(l):
            if c in "^v<>":
                carts.append(Cart(x, y, *dirs[c]))

            if c in "/\\+":
                graph[(x, y)] = c
    return graph, carts
            
@problem.solver(part=1)
def part1(ls):
    graph, carts = build_graph(ls)

    while True:
        carts.sort(key = lambda c: (c.x, c.y))

        for id, c in enumerate(carts):
            c.move()
            if any(cart.get_coords() == c.get_coords() for id2, cart in enumerate(carts) if id2 != id):
                return f"{c.x},{c.y}"
            
            if c.get_coords() in graph:
                c.make_turn(graph)

@problem.solver(part=2)
def part2(ls):
    graph, carts = build_graph(ls)

    while len(carts) > 1:
        carts.sort(key = lambda c: (c.x, c.y))

        for id, c in enumerate(carts):
            if c.crashed: continue

            c.move()

            for id2, cart in enumerate(carts):
                if id2 == id: continue
                if cart.crashed: continue
                if cart.get_coords() == c.get_coords():
                    cart.crashed = True
                    c.crashed = True
                    break

            if c.crashed: continue
            
            if c.get_coords() in graph:
                c.make_turn(graph)

        carts = [c for c in carts if not c.crashed]

    cart = carts[0]
    return f"{cart.x},{cart.y}"

if __name__ == "__main__":
    problem.solve()