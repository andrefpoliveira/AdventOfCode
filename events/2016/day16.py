from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/16: Dragon Checksum")
problem.preprocessor = ppr.I

def generate_data(s):
    copy = "".join(["0" if x == "1" else "1" for x in s[::-1]])
    s += "0" + copy
    return s

def checksum(s):
    res = ""
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            res += "1"
        else:
            res += "0"
    return res

def solve(s, disc_size):
    while len(s) < disc_size:
        s = generate_data(s)
    
    checks = checksum(s[:disc_size])
    while len(checks) % 2 == 0:
        checks = checksum(checks)
    return checks

@problem.solver()
def solver(s):
    return solve(s, 272), solve(s, 35651584)

if __name__ == "__main__":
    problem.solve()