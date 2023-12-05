import math

from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/16: Packet Decoder")
problem.preprocessor = ppr.I

rules = [sum,
         math.prod,
         min,
         max,
         lambda x: x[0],
         lambda x: 1 if x[0] > x[1] else 0,
         lambda x: 1 if x[0] < x[1] else 0,
         lambda x: 1 if x[0] == x[1] else 0]

def process_packet(s, i):
    tv = int(s[i:i+3], 2)
    id = int(s[i+3:i+6], 2)
    i += 6

    if id == 4:
        vals = [0]
        while True:
            vals[0] = 16 * vals[0] + int(s[i+1:i+5], 2)
            i += 5
            if s[i-5] == '0': break
    else:
        vals = []
        if s[i] == '0':
            end = i + 16 + int(s[i+1:i+16], 2)
            i += 16
            while i < end:
                i, v, v2 = process_packet(s, i)
                tv += v
                vals.append(v2)
        else:
            np = int(s[i+1:i+12], 2)
            i += 12
            for _ in range(np):
                i, v, v2 = process_packet(s, i)
                tv += v
                vals.append(v2)
    return i, tv, rules[id](vals)

@problem.solver()
def solver(s):
    binary = bin(int('1'+s,16))[3:]
    _, part1, part2 = process_packet(binary, 0)
    return part1, part2

if __name__ == "__main__":
    problem.solve()