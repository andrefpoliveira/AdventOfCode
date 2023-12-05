from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2017/15: Dueling Generators")
problem.preprocessor = ppr.lsv

FACTOR_A = 16807
FACTOR_B = 48271
DIVIDER = 2147483647

def generate_values(value, factor, multiplier = 1):
    while True:
        value *= factor
        value %= DIVIDER
        if not value % multiplier: yield value

@problem.solver(part=1)
def part1(ls):
    value_a = int(re.findall("\d+", ls[0])[0])
    value_b = int(re.findall("\d+", ls[1])[0])

    a_generator = generate_values(value_a, FACTOR_A)
    b_generator = generate_values(value_b, FACTOR_B)

    count = 0
    
    for _ in range(40000000):
        a = a_generator.__next__()
        b = b_generator.__next__()
        if a & 0xFFFF == b & 0xFFFF: count += 1

    return count

@problem.solver(part=2)
def part2(ls):
    value_a = int(re.findall("\d+", ls[0])[0])
    value_b = int(re.findall("\d+", ls[1])[0])

    a_generator = generate_values(value_a, FACTOR_A, 4)
    b_generator = generate_values(value_b, FACTOR_B, 8)

    count = 0
    
    for _ in range(5000000):
        a = a_generator.__next__()
        b = b_generator.__next__()
        if a & 0xFFFF == b & 0xFFFF: count += 1

    return count

if __name__ == "__main__":
    problem.solve()