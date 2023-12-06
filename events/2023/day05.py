from utils import problem
from utils import preprocessing as ppr

import re
from functools import cache

problem = problem.Problem("2023/05: If You Give A Seed A Fertilizer")
problem.preprocessor = lambda x: x.split("\n\n")

def create_mapping(ls):
    _map = []
    for l in ls[1:]:
        ns = tuple(map(int, re.findall(r"\d+", l)))
        _map.append(ns)
    return tuple(sorted(_map, key=lambda x: x[0]))

def seed_to_loc(seed, maps):
    for m in maps:
        for d, s, r in m:
            if s <= seed <= s + r - 1:
                seed = d + (seed - s)
                break
    return seed

@problem.solver(part=1)
def part1(ls):
    seeds = tuple(map(int, re.findall(r"\d+", ls[0])))
    maps = tuple([create_mapping(l.split("\n")) for l in ls[1:]])
    
    min_loc = float("inf")
    for s in seeds:
        s = seed_to_loc(s, maps)
        min_loc = min(min_loc, s)
    return min_loc

def loc_to_seed(loc, maps, seeds):
    for m in reversed(maps):
        for d, s, r in m:
            if d <= loc <= d + r - 1:
                loc = s + (loc - d)
                break

    for s, r in seeds:
        if s <= loc <= s + r:
            return True
    return False
        

@problem.solver(part=2)
def part2(ls):
    seeds = tuple(map(int, re.findall(r"\d+", ls[0])))
    maps = tuple([create_mapping(l.split("\n")) for l in ls[1:]])

    seeds_row = tuple((seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2))

    last_map = maps[-1]
    for s in range(0, last_map[-1][0] + last_map[-1][2]):
        if loc_to_seed(s, maps, seeds_row):
            return s

if __name__ == "__main__":
    problem.solve()