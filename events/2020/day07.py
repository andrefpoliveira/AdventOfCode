from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2020/07: Handy Haversacks")
problem.preprocessor = ppr.lsv

def _part1(g, start):
    queue = [start]
    added = set()
    count = 0

    while queue:
        bag = queue.pop()
        if bag != start: count += 1

        for b in g.get(bag, []):
            if b in added: continue
            added.add(b)
            queue.append(b)

    return count

@problem.solver(part=1)
def part1(ls):
    bags = {}
    for l in ls:
        container, bag = l.split(" contain ")
        c_bag = container.replace("bags", "").strip()
        bag = re.findall(r"\d+ ([^,]+) bag", bag)

        for b in bag:
            bags[b] = bags.get(b, []) + [c_bag]

    return _part1(bags, "shiny gold")

def _part2(g, start):
    next_bags = g.get(start, [])
    count = 1

    for n, bag in next_bags:
        count += int(n) * _part2(g, bag)

    return count


@problem.solver(part=2)
def part2(ls):
    bags = {}
    for l in ls:
        container, bag = l.split(" contain ")
        c_bag = container.replace("bags", "").strip()
        bag = re.findall(r"(\d+) ([^,]+) bag", bag)
        bags[c_bag] = bag

    return _part2(bags, "shiny gold") - 1
    
if __name__ == "__main__":
    problem.solve()