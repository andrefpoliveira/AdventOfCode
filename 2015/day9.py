from itertools import permutations

def solve(grid, locs, fc, starting_value):
    best_path = starting_value
    for p in permutations(locs, len(locs)):
        current_path = 0
        for i in range(1, len(locs)):
            current_path += grid[f"{p[i-1]}-{p[i]}"]

        best_path = fc(best_path, current_path)
    return best_path

def run():
    with open("./2015/inputs/day9.txt", "r") as f:
        input_text = f.readlines()

    grid = {}
    locs = set()
    for line in input_text:
        l = line.split(" ")
        f, t, d = l[0], l[2], int(l[4])
        locs.add(f)
        locs.add(t)
        
        grid[f"{f}-{t}"] = d
        grid[f"{t}-{f}"] = d

    print(f"Day 9 Part 1: {solve(grid, locs, min, float('Inf'))}")
    print(f"Day 9 Part 2: {solve(grid, locs, max, -float('Inf'))}")

if __name__ == "__main__":
    run()