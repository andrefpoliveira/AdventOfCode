from utils import problem
from utils import preprocessing as ppr
problem = problem.Problem("2025/03: Lobby")
problem.preprocessor = ppr.lsv

def update_pointer(l, pointers, count):
    for i in range(1, count):
        digit = int(l[pointers[i]])

        for _i in range(i):
            _digit = int(l[pointers[_i]])
            if digit > _digit and pointers[i] < len(l) - (count - 1 - _i):
                pointers[_i] = pointers[i]

                for j in range(_i + 1, count):
                    pointers[j] = pointers[j - 1] + 1
                
                return
    pointers[-1] += 1


def find_joltage(l, count = 2):
    joltage = int(l[:count])
    pointers = [i-1 for i in range(1, count + 1)]

    while all(pointers[i] < len(l) - (count - 1 - i) for i in range(count)):
        v = ''.join(l[pointers[i]] for i in range(count))

        if int(v) > joltage:
            joltage = int(v)

        update_pointer(l, pointers, count)

    return joltage

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    for l in inp:
        p1 += find_joltage(l, 2)
        p2 += find_joltage(l, 12)

    return p1, p2

if __name__ == "__main__":
    problem.solve()