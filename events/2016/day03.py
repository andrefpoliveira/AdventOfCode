import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/03: Squares With Three Sides")
problem.preprocessor = ppr.lsv

@problem.solver(part=1)
def part1(triangles):
    count = 0

    for tr in triangles:
        sides = list(map(int, re.findall(r"\d+", tr)))
        if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
            count += 1
    return count

@problem.solver(part=2)
def part2(triangles):
    count = 0
    for id in range(2, len(triangles), 3):
        sides_1 = list(map(int, re.findall(r"\d+", triangles[id-2])))
        sides_2 = list(map(int, re.findall(r"\d+", triangles[id-1])))
        sides_3 = list(map(int, re.findall(r"\d+", triangles[id])))

        for i in range(3):
            if sides_1[i] + sides_2[i] > sides_3[i] and sides_2[i] + sides_3[i] > sides_1[i] and sides_1[i] + sides_3[i] > sides_2[i]:
                count += 1
    return count

if __name__ == "__main__":
    problem.solve()