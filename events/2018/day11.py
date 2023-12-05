from utils import problem
from utils import preprocessing as ppr

import numpy as np

problem = problem.Problem("2018/11: Chronal Charge")
problem.preprocessor = ppr.intI

@problem.solver()
def part1(v):
    grid = [
        [
            (((x + 10) * y + v) * (x + 10))//100%10 - 5
        for x in range(300)]
    for y in range(300)]

    arr = np.array(grid)
    
    best_3, best_all, sum_all = (0,0), (0,0), 0
    for size in range(3, 299):
        best_coords, best_sum = (0, 0), 0
        for y in range(299-size):
            for x in range(299-size):
                sum = np.sum(arr[y:y+size, x:x+size])
                if sum > best_sum:
                    best_sum = sum
                    best_coords = (x, y)

        if best_sum > sum_all:
            sum_all = best_sum
            best_all = best_coords + (size,)

        if size == 3:
            best_3 = best_coords

    return best_3, best_all

if __name__ == "__main__":
    problem.solve()