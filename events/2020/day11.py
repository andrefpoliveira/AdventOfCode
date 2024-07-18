from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo

problem = problem.Problem("2020/11: Seating System")
problem.preprocessor = lambda x: [[{"L": 1, ".": 0, "#": -1}[seat] for seat in row] for row in x.split()]

def load_seen_seets(grid, part2 = False):
	seen_seats = {}
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 0:
				continue
			else:
				if not part2:
					seen_seats[(x, y)] = [
						(x + dx, y + dy) for dx, dy in geo.NEIGHBOURS8
						if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)
					]
				else:
					seen = []
					for dx, dy in geo.NEIGHBOURS8:
						_x, _y = x + dx, y + dy
						while 0 <= _x < len(grid[0]) and 0 <= _y < len(grid):
							if grid[_y][_x] != 0:
								seen.append((_x, _y))
								break
							_x += dx
							_y += dy

					seen_seats[(x, y)] = seen
	
	return seen_seats

def iterate_grid(grid, seen_seats, part2 = False):
	_grid = [[x for x in row] for row in grid]

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 0:
				continue

			adjacent = 0
			for _x, _y in seen_seats[(x, y)]:
				adjacent += grid[_y][_x] == -1

			if grid[y][x] == 1 and adjacent == 0:
				_grid[y][x] = -1
			elif grid[y][x] == -1 and adjacent >= (4 if not part2 else 5):
				_grid[y][x] = 1

	return _grid

@problem.solver(part=1)
def part1(grid):
	seen_seats = load_seen_seets(grid)
	while True:
		_grid = iterate_grid(grid, seen_seats)
		if _grid == grid:
			break

		grid = _grid
	
	return sum(row.count(-1) for row in grid)

@problem.solver(part=2)
def part2(grid):
	seen_seats = load_seen_seets(grid, part2=True)
	while True:
		_grid = iterate_grid(grid, seen_seats, part2=True)
		if _grid == grid:
			break

		grid = _grid
	
	return sum(row.count(-1) for row in grid)
 
if __name__ == "__main__":
    problem.solve()