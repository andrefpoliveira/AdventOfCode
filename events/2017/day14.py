from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/14: Disk Defragmentation")
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

def hex_to_bin(s):
    return bin(int(s, 16))[2:].zfill(128)

@problem.solver()
def solver(s):
    part2 = 0
    unseen = []
    for i in range(128):
        ns = [ord(x) for x in f"{s}-{i}"] + [17, 31, 73, 47, 23]
        sparse = reverse(ns, 64)
        dense_l = dense(sparse)
        hash = knot_hash(dense_l)
        binary = hex_to_bin(hash)
        unseen += [(i, j) for j, d in enumerate(binary) if d == "1"]

    part1 = len(unseen)

    while unseen:
        queue = [unseen[0]]
        while queue:
            (x, y) = queue.pop()
            if (x, y) in unseen:
                unseen.remove((x, y))
                queue += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        part2 += 1

    return part1, part2

if __name__ == "__main__":
    problem.solve()