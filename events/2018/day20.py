from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/20: A Regular Map")
problem.preprocessor = ppr.I

DIRS = {
	"N": (0,-1),
	"S": (0,1),
	"E": (1,0),
	"W": (-1,0)
}


def move_coords(coords, dir, conns):
	_coords = []
	for c in coords:
		_c = tuple(sum(t) for t in zip(c, DIRS[dir]))
		_coords.append(_c)

		s = conns.get(c, set())
		s.add(_c)
		conns[c] = s

		s = conns.get(_c, set())
		s.add(c)
		conns[_c] = s

	return _coords


def separate_options(s):
	option = ""
	i = opened = 0
	options = []

	while i < len(s):
		c = s[i]
		if c == '|' and opened == 0:
			if option:
				options.append(option)
				option = ""
		else:
			option += c
			if c == "(":
				opened += 1
			elif c == ")":
				opened -= 1

		i += 1
	
	if option:
		options.append(option)

	return options


def get_branch(s):
	i = opened = 1
	while opened != 0:
		if s[i] == "(":
			opened += 1
		elif s[i] == ")":
			opened -= 1
		i += 1
	return i


def build_map(s, conns, coords = [(0, 0)], depth=0):
	# print(s, depth)

	if not s:
		return coords

	options = separate_options(s)
	final_coords = []

	for option in options:
		_coords = [x for x in coords]

		while option:
			if option[0] in DIRS:
				_coords = move_coords(_coords, option[0], conns)
				option = option[1:]
			else:
				j = get_branch(option)
				branch = option[1: j - 1]
				_coords = build_map(branch, conns, _coords, depth + 1)
				option = option[j:]

		final_coords += _coords


	return final_coords
	

@problem.solver()
def solver(s):
	conns = {}
	m = build_map(s[1:-1], conns)

	distances = {}
	queue = [(0, 0, 0)]		# x, y, distance

	while queue:
		x, y, d = queue.pop()

		if distances.get((x, y), float("inf")) > d:
			distances[(x, y)] = d
		else:
			continue

		for conn in conns[(x, y)]:
			queue.append((*conn, d + 1))

	return max(distances.values()), len([x for x in distances.values() if x >= 1000])
		

if __name__ == "__main__":
    problem.solve()