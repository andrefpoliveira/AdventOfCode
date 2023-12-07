from utils import problem
from utils import preprocessing as ppr

from collections import Counter
from functools import cmp_to_key

problem = problem.Problem("2023/07: Camel Cards")
problem.preprocessor = ppr.lsv

DESCENDING_PART1 = "AKQJT98765432"
DESCENDING_PART2 = "AKQT98765432J"

def get_type(hand, part2 = False):
    j_count = 0
    if part2:
        j_count = hand.count("J")
        hand = hand.replace("J", "")

    c = sorted(Counter(hand).values(), reverse=True) if hand else [0]
    c[0] += j_count
    
    # 5 of a kind
    if len(c) == 1: return 7

    # 4 of a kind or full house
    if len(c) == 2:
        if c[0] == 4: return 6
        if c[0] == 3: return 5

    # 3 of a kind or two pair
    if len(c) == 3:
        if c[0] == 3: return 4
        if c[0] == 2: return 3

    if len(c) == 4: return 2
    return 1

def order_hands(h1, t1, h2, t2, part2 = False):
    if t1 > t2: return 1
    if t1 < t2: return -1

    descending_list = DESCENDING_PART1 if not part2 else DESCENDING_PART2

    for i in range(5):
        if descending_list.index(h1[i]) < descending_list.index(h2[i]): return 1
        if descending_list.index(h1[i]) > descending_list.index(h2[i]): return -1
    return 0

@problem.solver(part=1)
def part1(ls):
    hands = []
    for l in ls:
        h, m = l.split()
        hands.append((h, get_type(h), int(m)))
        
    hands = sorted(hands, key=cmp_to_key(lambda x, y: order_hands(*x[:2], *y[:2])))
    return sum([m * (i + 1) for i, (_, _, m) in enumerate(hands)])


@problem.solver(part=2)
def part2(ls):
    hands = []
    for l in ls:
        h, m = l.split()
        hands.append((h, get_type(h, True), int(m)))
        
    hands = sorted(hands, key=cmp_to_key(lambda x, y: order_hands(*x[:2], *y[:2], True)))
    return sum([m * (i + 1) for i, (_, _, m) in enumerate(hands)])

if __name__ == "__main__":
    problem.solve()