import re
from itertools import chain, combinations
from collections import Counter

from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/11: Radioisotope Thermoelectric Generators")
problem.preprocessor = ppr.lsv

def parse_ls(ls):
    floors = []
    for l in ls:
        generator = ["G" + x[0].upper() + x[1] for x in re.findall(r"([^ ]+) generator", l)]
        microchip = ["M" + x[0].upper() + x[1] for x in re.findall(r"([^ ]+)-compatible microchip", l)]

        floors.append(set(generator + microchip))
    return floors

def finished(floors):
    return all(not floor for floor in floors[:-1])

def is_valid_floor(floor):
    return len(set(x[0] for x in floor)) < 2 or \
        all("G" + x[1:] in floor for x in floor if x[0] == "M")

def find_valid_moves(state):
    floors, depth, elevator = state

    moves = chain(combinations(floors[elevator], 2), combinations(floors[elevator], 1))

    for move in moves:
        for dir in [-1, 1]:
            next_elevator = elevator + dir
            if not 0 <= next_elevator < len(floors): continue

            next_floors = floors.copy()
            next_floors[elevator] = next_floors[elevator].difference(move)
            next_floors[next_elevator] = next_floors[next_elevator].union(move)

            if (is_valid_floor(next_floors[elevator]) and is_valid_floor(next_floors[next_elevator])):
                yield (next_floors, depth+1, next_elevator)

def floor_representation(state):
    floors, _, elevator = state
    return elevator, tuple(tuple(Counter(x[0] for x in floor).most_common()) for floor in floors)

def search(floors):
    visited = set()
    queue = [(floors, 0, 0)]

    while queue:
        state = queue.pop(0)
        floors, depth, _ = state

        if finished(floors): return depth

        for next_state in find_valid_moves(state):
            key = floor_representation(next_state)
            if key not in visited:
                visited.add(key)
                queue.append(next_state)

@problem.solver(part=1)
def part1(ls):
    floors = parse_ls(ls)
    return search(floors)

@problem.solver(part=2)
def part2(ls):
    floors = parse_ls(ls)
    floors[0] = floors[0].union(["GEl", "MEl", "GDi", "MDi"])
    return search(floors)

if __name__ == "__main__":
    problem.solve()