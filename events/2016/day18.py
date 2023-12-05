from utils import problem

problem = problem.Problem("2016/18: Like a Rogue")
problem.preprocessor = lambda x: [True if i == "^" else False for i in x.strip()]

def is_trap(left, center, right):
    if left and center and not right: return True
    if center and right and not left: return True
    if left and not center and not right: return True
    return not left and not center and right

def solve(arr, rows):
    safe_tiles = len(arr) - sum(arr)
    for _ in range(rows):
        new_arr = [is_trap(False, arr[0], arr[1])]

        for i in range(2, len(arr)):
            new_arr.append(is_trap(arr[i-2], arr[i-1], arr[i]))

        new_arr.append(is_trap(arr[-2], arr[-1], False))
        safe_tiles += len(new_arr) - sum(new_arr)
        arr = new_arr

    return safe_tiles

@problem.solver()
def solver(arr):
    return solve(arr, 39), solve(arr, 399999)

if __name__ == "__main__":
    problem.solve()