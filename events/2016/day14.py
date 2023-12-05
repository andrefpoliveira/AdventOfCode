from utils import problem
from utils import preprocessing as ppr

import re
from hashlib import md5

problem = problem.Problem("2016/14: One-Time Pad")
problem.preprocessor = ppr.I

def find_consecutive(s, amount):
    pattern = r"([a-z0-9])" + r"\1" * (amount-1)
    res = re.findall(pattern, s)
    return (True, res[0][0]) if len(res) > 0 else (False, None)

def hash_string(s, reps):
    for _ in range(reps):
        s = md5(s.encode()).hexdigest()
    return s

def solve(s, reps):
    keys, pending, id = [], [], 0
    while len(keys) < 64:
        h = hash_string(f"{s}{id}", reps)

        found5, letter5 = find_consecutive(h, 5)
        found3, letter3 = find_consecutive(h, 3)

        if found5:
            new_pending = []
            for key in pending:
                _, hex_id, letter = key
                if id - hex_id > 1000: pass 
                elif letter5 == letter: keys.append(key)
                else: new_pending.append(key)

            pending = new_pending

        if found3:
            pending.append((h, id, letter3))

        id += 1
    return keys[63][1]

@problem.solver()
def solver(s):
    return solve(s, 1), solve(s, 2017)

if __name__ == "__main__":
    problem.solve()