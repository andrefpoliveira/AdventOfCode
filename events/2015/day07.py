from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/07: Some Assembly Required")
problem.preprocessor = ppr.lsv

def transform_left(d, left):
    if left.isdigit(): return int(left)
    return d[left]

def wiring(input_text, initial_d = {}):
    d = initial_d
    part2 = len(initial_d) == 1
    while "a" not in d:
        for line in input_text:
            left, right = line.strip().split(" -> ")

            try:
                if "AND" in left:
                    left = transform_left(d, left.split(" AND ")[0]) & transform_left(d, left.split(" AND ")[1])
                elif "OR" in left:
                    left = transform_left(d, left.split(" OR ")[0]) | transform_left(d, left.split(" OR ")[1])
                elif "LSHIFT" in left:
                    left = transform_left(d, left.split(" LSHIFT ")[0]) << int(left.split(" LSHIFT ")[1])
                elif "RSHIFT" in left:
                    left = transform_left(d, left.split(" RSHIFT ")[0]) >> int(left.split(" RSHIFT ")[1])
                elif "NOT" in left:
                    left = 65525 - transform_left(d, left.replace("NOT ", ""))
                else:
                    left = transform_left(d, left)

                if part2 == False or right != "b":
                    d[right] = left
            except:
                pass
    return d['a']

@problem.solver()
def solve(input_text):
    p1 = wiring(input_text)
    p2 = wiring(input_text, {'b': p1})
    return p1, p2

if __name__ == "__main__":
    problem.solve()