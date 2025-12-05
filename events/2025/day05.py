from utils import problem
problem = problem.Problem("2025/05: Cafeteria")
problem.preprocessor = lambda x: x.split('\n\n')

def get_ranges(ls):
    ranges = []
    for l in ls:
        a, b = l.split('-')
        ranges.append(range(int(a), int(b)+1))
    return ranges

def merge_ranges(ranges):
    ranges.sort(key=lambda r: r.start)
    merged_ranges = []

    for r in ranges:
        if merged_ranges and merged_ranges[-1].stop >= r.start:
            merged_ranges[-1] = range(merged_ranges[-1].start, max(merged_ranges[-1].stop, r.stop))
        else:
            merged_ranges.append(r)

    return merged_ranges

@problem.solver(part=1)
def part1(inp):
    p1 = 0

    ranges = get_ranges(inp[0].splitlines())
    ranges = merge_ranges(ranges)

    for line in inp[1].splitlines():
        v = int(line)
        in_any = any(v in r for r in ranges)
        if in_any:
            p1 += 1

    return p1

@problem.solver(part=2)
def part2(inp):
    p2 = 0

    ranges = get_ranges(inp[0].splitlines())
    ranges = merge_ranges(ranges)

    return sum(len(r) for r in ranges)

if __name__ == "__main__":
    problem.solve()