from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo

from collections import Counter

problem = problem.Problem("2018/18: Settlers of The North Pole")
problem.preprocessor = ppr.grid

def create_map(grid):
	g = {}
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			v = grid[y][x]
			g[(x, y)] = 0 if v == '.' else 1 if v == '|' else 2

	return g


def show_map(g, w, h):
	for y in range(h):
		for x in range(w):
			v = g[(x, y)]
			print('.' if v == 0 else '|' if v == 1 else '#', end="")
		print()
	print()

def simulate(g, width, height):
	_g = {}

	for y in range(height):
		for x in range(width):
			c = g[(x, y)]

			trees = lumber = 0
			for dx, dy in geo.NEIGHBOURS8:
				_x, _y = x + dx, y + dy

				if g.get((_x, _y), 0) == 1:
					trees += 1
				elif g.get((_x, _y), 0) == 2:
					lumber += 1

			if c == 0 and trees >= 3:
				_g[(x, y)] = 1
			elif c == 1 and lumber >= 3:
				_g[(x, y)] = 2
			elif c == 2:
				_g[(x, y)] = 2 if trees >= 1 and lumber >= 1 else 0
			else:
				_g[(x, y)] = c

	return _g


@problem.solver(part=1)
def part1(grid):
	w, h = len(grid[0]), len(grid)

	g = create_map(grid)

	for _ in range(10):
		g = simulate(g, w, h)

	c = Counter(g.values())
	return c[1] * c[2]


@problem.solver(part=2)
def part2(grid):
	minutes = 1000000000
	w, h = len(grid[0]), len(grid)

	g = create_map(grid)

	l = [g]

	for m in range(minutes):
		g = simulate(g, w, h)
		if g in l:
			idx = l.index(g)
			size = len(l) - idx
			final_idx = (minutes - idx) % size

			g = l[idx + final_idx]

			c = Counter(g.values())
			return c[1] * c[2]

		l.append(g)
		

if __name__ == "__main__":
    problem.solve()