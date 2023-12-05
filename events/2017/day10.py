from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/10: Knot Hash")
problem.preprocessor = ppr.I

def reverse(ns, repeatitions = 1):
    l = list(range(256))
    pos, skip = 0, 0
    for _ in range(repeatitions):
        for n in ns:
            reverse_ns = []
            for j in range(n):
                reverse_ns.append(l[(pos + j) % 256])
            for j in range(n):
                l[(pos + j) % 256] = reverse_ns[-j - 1]

            pos += skip + n
            skip += 1
    return l

def dense(ns):
    dense = []
    for i in range(16):
        v = ns[16 * i]
        for j in range(1, 16):
            v ^= ns[16 * i + j]
        dense.append(v)
    return dense

def knot_hash(dense):
    return "".join(f'{i:02x}' for i in dense)

@problem.solver(part=1)
def part1(s):
    ns = [int(x) for x in s.strip().split(",")]
    sparse = reverse(ns)
    return sparse[0] * sparse[1]

@problem.solver(part=2)
def part2(s):
    ns = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    sparse = reverse(ns, 64)
    dense_l = dense(sparse)
    return knot_hash(dense_l)

if __name__ == "__main__":
    problem.solve()