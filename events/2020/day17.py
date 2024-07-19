from utils import problem
from utils import preprocessing as ppr

from itertools import product

import re

problem = problem.Problem("2020/17: Conway Cubes")
problem.preprocessor = ppr.grid

def parse_input(grid, part2 = False):
	m = {}
	for y, row in enumerate(grid):
		for x, cell in enumerate(row):
			if part2:
				m[(x, y, 0, 0)] = 1 if cell == "#" else 0
			else:
				m[(x, y, 0)] = 1 if cell == "#" else 0

	return m

def iterate(grid):
	_grid = {}

	cols = len(list(grid.keys())[0])
	mins_maxs = [(min([x[i] for x in grid]), max([x[i] for x in grid])) for i in range(cols)]
	
	for pos in product(*[range(mins_max[0] - 1, mins_max[1] + 2) for mins_max in mins_maxs]):
		active = 0
		for d in product(*[range(-1, 2) for _ in range(cols)]):
			if set(d) == {0}:
				continue

			_c = tuple([pos[i] + d[i] for i in range(cols)])

			if grid.get(_c, 0) == 1:
				active += 1

		if grid.get(pos, 0) == 1:
			_grid[pos] = 1 if active in [2, 3] else 0
		else:
			_grid[pos] = 1 if active == 3 else 0

	return _grid

@problem.solver(part=1)
def part1(grid):
	m = parse_input(grid)

	for _ in range(6):
		m = iterate(m)

	return sum([v for v in m.values()])

@problem.solver(part=2)
def part2(grid):
	m = parse_input(grid, part2=True)

	for _ in range(6):
		m = iterate(m)

	return sum([v for v in m.values()])

if __name__ == "__main__":
	problem.solve()