from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2023/15: Lens Library")
problem.preprocessor = ppr.I

def hash_algo(s):
    v = 0
    for c in s:
        v = ((v + ord(c)) * 17 ) % 256
    return v

@problem.solver(part=1)
def part1(s):
    p1 = 0
    for _s in s.split(","):
        p1 += hash_algo(_s)
    return p1

@problem.solver(part=2)
def part2(s):
    boxes = [[] for _ in range(256)]

    for _s in s.split(","):
        label, lens = _s.split("=") if "=" in _s else (_s[:-1], None)
        h = hash_algo(label)

        if lens is None:
            boxes[h] = [x for x in boxes[h] if x[0] != label]
        else:
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == label:
                    boxes[h][i] = (label, int(lens))
                    break
            else:
                boxes[h].append((label, int(lens)))

    p2 = 0
    for id, b in enumerate(boxes):
        for _id, _b in enumerate(b):
            p2 += (id + 1) * (_id + 1) * _b[1]
    return p2

if __name__ == "__main__":
    problem.solve()