import hashlib
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/05: How About a Nice Game of Chess?")
problem.preprocessor = ppr.I

@problem.solver(part=1)
def part1(s):
    res = ""
    n = 0
    while len(res) < len(s):
        h = hashlib.md5((s + str(n)).encode()).hexdigest()
        if h[:5] == "0" * 5:
            res += h[5]
        n += 1
    return res

@problem.solver(part=2)
def part2(s):
    res = ["_" for _ in range(len(s))]
    n = 0
    while "_" in res:
        h = hashlib.md5((s + str(n)).encode()).hexdigest()
        if h[:5] == "0" * 5:
            id, v = h[5], h[6]
            if id.isdigit() and int(id) < len(res) and res[int(id)] == "_":
                res[int(id)] = v
        n += 1
    return ''.join(res)

if __name__ == "__main__":
    problem.solve()