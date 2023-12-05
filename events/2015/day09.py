from itertools import permutations
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/09: All in a Single Night")
problem.preprocessor = ppr.lsv

def delivers(grid, locs, fc, starting_value):
    best_path = starting_value
    for p in permutations(locs, len(locs)):
        current_path = 0
        for i in range(1, len(locs)):
            current_path += grid[f"{p[i-1]}-{p[i]}"]

        best_path = fc(best_path, current_path)
    return best_path

@problem.solver()
def solve(input_text):
    grid = {}
    locs = set()
    for line in input_text:
        l = line.split(" ")
        f, t, d = l[0], l[2], int(l[4])
        locs.add(f)
        locs.add(t)
        
        grid[f"{f}-{t}"] = d
        grid[f"{t}-{f}"] = d

    return delivers(grid, locs, min, float('Inf')), delivers(grid, locs, max, -float('Inf'))

if __name__ == "__main__":
    problem.solve()