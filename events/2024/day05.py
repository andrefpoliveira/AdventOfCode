from utils import problem
from utils import preprocessing as ppr

from collections import defaultdict

problem = problem.Problem("2024/05: Print Queue")
problem.preprocessor = ppr.lsv


def build_precendeces(ls):
    orders = defaultdict(list)

    i = 0
    while True:
        line = ls[i]
        i += 1
        if not line:
            break

        bef, aft = [int(x) for x in line.split('|')]
        orders[bef] = orders[bef] + [aft]

    return orders, i


def is_valid_update(orders, update):
    seen = set()
    for page in update:
        pages_after = orders[page]

        if seen and seen.intersection(pages_after):
            return False
        
        seen.add(page)
    return True


def reorder_update(orders, update):
    new_update = [None for _ in range(len(update))]
    for i in range(len(update)):
        page = update[i]
        pages = set([x for id, x in enumerate(update) if id != i])

        intersections = len(set(orders[page]).intersection(pages))

        new_update[intersections] = page

    return new_update


@problem.solver()
def part1(ls):
    orders, i = build_precendeces(ls)

    part1 = part2 = 0

    while i < len(ls):
        update = ls[i]
        pages = [int(x) for x in update.split(',')]
        
        if is_valid_update(orders, pages):
            part1 += pages[len(pages) // 2]    
        else:
            pages = reorder_update(orders, pages)
            part2 += pages[len(pages) // 2]
        
        i += 1

    return part1, part2

if __name__ == "__main__":
    problem.solve()