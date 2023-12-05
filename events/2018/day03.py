from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/03: No Matter How You Slice It")
problem.preprocessor = ppr.lsv

@problem.solver()
def solver(ls):
    claims = {}
    clear = []

    for l in ls:
        m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', l)
        id, x, y, w, h = map(int, m.groups())

        clear.append(id)

        for i in range(x, x + w):
            for j in range(y, y + h):
                data = claims.get((i, j), {"c": 0, "id": -1})
                data["c"] += 1
                p_id = data["id"]
                if p_id != -1:
                    if id in clear: clear.remove(id)
                    if p_id in clear: clear.remove(p_id)
                data["id"] = id
                claims[(i, j)] = data

    return sum(1 for v in claims.values() if v["c"] > 1), clear[0]

if __name__ == "__main__":
    problem.solve()