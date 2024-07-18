from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/15: Rambunctious Recitation")
problem.preprocessor = ppr.csi

def solver(ns, target):
	d = {}
	
	for i, n in enumerate(ns):
		d[n] = i

	while i < target - 1:
		if n not in d or d[n] == i:
			d[n] = i
			n = 0

		elif n in d:
			m = i - d[n]
			d[n] = i
			n = m

		i += 1

	return n

@problem.solver(part=1)
def part1(ns):
	return solver(ns, 2020)

@problem.solver(part=2)
def part2(ns):
	return solver(ns, 30000000)

if __name__ == "__main__":
    problem.solve()