from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/02: Password Philosophy")
problem.preprocessor = ppr.lsv

@problem.solver()
def solver(ls):
    part1 = part2 = 0
    for l in ls:
        numbers, char, password = l.split()
        min_range, max_range = map(int, numbers.split("-"))
        char = char[0]

        if min_range <= password.count(char) <= max_range:
            part1 += 1

        if (password[min_range-1] == char) != (password[max_range-1] == char):
            part2 += 1

    return part1, part2
            
if __name__ == "__main__":
    problem.solve()