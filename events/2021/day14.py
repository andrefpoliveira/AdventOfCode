from collections import Counter

from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/14: Extended Polymerization")
problem.preprocessor = ppr.lsv

def solve(template, rules, iterations):
    letters = Counter(template)
    pairs = Counter(template[i-1:i+1] for i in range(1, len(template)))
    for t in range(iterations):
        new_pairs = Counter()
        for pair, num in pairs.items():
            if pair in rules:
                l1, l2 = pair
                new_l = rules[pair]
                new_pairs[l1 + new_l] += num
                new_pairs[new_l + l2] += num
                letters[new_l] += num
            else:
                new_pairs[pair] = num
        pairs = new_pairs
    return max(letters.values()) - min(letters.values())

@problem.solver()
def solver(ls):
    template = ls[0]
    rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in ls[2:]}
    return solve(template, rules, 10), solve(template, rules, 40)

if __name__ == "__main__":
    problem.solve()