from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/12: Subterranean Sustainability")
problem.preprocessor = ppr.lsv

def fill_points(config):
    beg = re.search(r"^\.+", config)
    end = re.search(r"\.+$", config)
    return (
        5 if beg == None else max(0, 5 - len(beg.group(0))),
        5 if end == None else max(0, 5 - len(end.group(0)))
    )

def sum_plants(config, index_of_0):
    return sum(id - index_of_0 for id, v in enumerate(config) if v == "#")
    
def evolve(generations, config, rules):
    index_of_0 = 0
    beg, end = fill_points(config)
    index_of_0 += beg
    config = beg * "." + config + end * "."

    for _ in range(generations):
        new_config = ""
        for p in range(len(config)):
            piece = config[p-2:p+3]
            new_config += rules.get(piece, ".")

        config = new_config
        beg, end = fill_points(config)
        index_of_0 += beg
        config = beg * "." + config + end * "."

        score = sum_plants(config, index_of_0)

    return score
            
@problem.solver()
def solver(ls):
    config = ls[0].split()[2]

    rules = {}
    for l in ls[2:]:
        before, _, after = l.split()
        rules[before] = after

    return (
        evolve(20, config, rules),
        evolve(100, config, rules) + (50000000000 - 100) * 38
    )

if __name__ == "__main__":
    problem.solve()