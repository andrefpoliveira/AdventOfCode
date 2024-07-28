from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/17: Reservoir Research")
problem.preprocessor = ppr.lsv

def create_map(ls):
	m = {}

	for l in ls:
		c1, n1, c2, n2, n3 = re.findall('(\w)=(\d+), (\w)=(\d+)\.\.(\d+)', l)[0]
		
		for i in range(int(n2), int(n3) + 1):
			if c1 == "x":
				k = (int(n1), i)
			else:
				k = (i, int(n1))

			m[k] = 0

	return m
	

def join_dicts(d1, d2):
	new_d = {}
	for k in d1:
		new_d[k] = max(new_d.get(k, 0), d1[k])
	for k in d2:
		new_d[k] = max(new_d.get(k, 0), d2[k])
	return new_d


def simulate(m, drop=(500,0), drops=[]):
	if drop in drops:
		return {}
	else:
		drops.append(drop)

	water = {}

	max_y = max(x[1] for x in m)
	dx, dy = drop

	while (dx, dy) not in m | water and dy <= max_y:
		water[(dx, dy)] = 0
		dy += 1

	if dy > max_y:
		return water

	dy -= 1

	while dy > drop[1]:
		# While it is contained
		left_contained = right_contained = True

		# Going left
		_ldx = dx - 1
		while (_ldx, dy) not in m | water:

			if (_ldx, dy + 1) not in m | water:
				new_water = simulate(m, (_ldx, dy), drops)
				water = join_dicts(water, new_water)

				if (_ldx - 1, dy + 1) not in m | water:
					left_contained = False
					break
			else:
				water[(_ldx, dy)] = max(water.get((_ldx, dy), 0), 0)

			_ldx -= 1

		# Going right
		_rdx = dx + 1
		while (_rdx, dy) not in m | water:

			if (_rdx, dy + 1) not in m | water:
				new_water = simulate(m, (_rdx, dy), drops)
				water = join_dicts(water, new_water)

				if (_rdx + 1, dy + 1) not in m | water:
					right_contained = False
					break
			else:
				water[(_rdx, dy)] = max(water.get((_rdx, dy), 0), 0)

			_rdx += 1

		if not left_contained or not right_contained:
			break
		else:
			for _x in range(_ldx + 1, _rdx):
				water[(_x, dy)] = 1
		
		dy -= 1

	return water

@problem.solver()
def solver(ls):
	m = create_map(ls)
	min_y, max_y = min(x[1] for x in m), max(x[1] for x in m)

	water = simulate(m)

	return len([x for x in water if min_y <= x[1] <= max_y]), sum(water.values())

if __name__ == "__main__":
    problem.solve()