from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/12: Rain Risk")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
	dir = (1, 0)
	x, y = 0, 0

	for inst in ls:
		d, steps = inst[0], int(inst[1:])
		if d in ["N", "S"]:
			y += steps * (1 if d == "N" else -1)
		elif d in ["E", "W"]:
			x += steps * (1 if d == "E" else -1)
		elif d == "F":
			x += steps * dir[0]
			y += steps * dir[1]
		elif d in ["L", "R"]:
			steps = steps // 90
			if d == "L":
				steps = 4 - steps
			for _ in range(steps):
				dir = (dir[1], -dir[0])

	return abs(x) + abs(y)

@problem.solver(part=2)
def part2(ls):
	x, y = 0, 0
	w_x, w_y = 10, 1

	for inst in ls:
		d, steps = inst[0], int(inst[1:])
		if d in ["N", "S"]:
			w_y += steps * (1 if d == "N" else -1)
		elif d in ["E", "W"]:
			w_x += steps * (1 if d == "E" else -1)
		elif d == "F":
			x += steps * w_x
			y += steps * w_y
		elif d in ["L", "R"]:
			steps = steps // 90
			if d == "L":
				steps = 4 - steps
			for _ in range(steps):
				w_x, w_y = w_y, -w_x

	return abs(x) + abs(y)
 
if __name__ == "__main__":
    problem.solve()