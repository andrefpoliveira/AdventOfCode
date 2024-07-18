from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/13: Shuttle Search")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(ls):
	timestamp = int(ls[0])
	buses = [int(bus) for bus in ls[1].split(",") if bus != "x"]

	min_time = float("inf")
	_bus = None
	for bus in buses:
		time = bus + bus * (timestamp // bus)
		if time < min_time:
			min_time = time
			_bus = bus

	return _bus * (min_time - timestamp)

@problem.solver(part=2)
def part2(ls):
	timestamp = 100000000000000
	step = 1
	buses = [(offset, int(bus)) for offset, bus in enumerate(ls[1].split(",")) if bus != "x"]

	for offset, bus in buses:
		while (timestamp + offset) % bus != 0:
			timestamp += step

		step *= bus

	return timestamp
		
 
if __name__ == "__main__":
    problem.solve()