from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2022/16: Proboscidea Volcanium")
problem.preprocessor = ppr.lsv

def create_graph(ls):
    graph = {}
    for l in ls:
        flow, connections = l.split(";")
        section, flow = re.findall(r"Valve ([A-Z]+) has flow rate=(\d+)", flow)[0]
        connections = re.findall(r"([A-Z]+)", connections)

        graph[section] = {
            "flow": int(flow),
            "conns": connections
        }
    return graph

def find_shortest_path(graph, frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            for y in graph[x]['conns']:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1


@problem.solver(part=1)
def part1(ls):
    graph = create_graph(ls)
    non_zero_valves = [x for x in graph.keys() if graph[x]["flow"] != 0]

    for k in non_zero_valves + ['AA']:
        graph[k]['distances'] = {}
        for k2 in non_zero_valves:
            graph[k]['distances'][k2] = find_shortest_path(graph, graph[k]["conns"], k2)

    res = 0

    def explore(valve, opened, minutes, pressure):
        nonlocal res

        if pressure > res: res = pressure
        if minutes <= 0: return

        if valve not in opened:
            new_pressure = pressure + graph[valve]["flow"] * minutes
            explore(valve, [x for x in opened] + [valve], minutes - 1, new_pressure)
        else:
            for k in [x for x in graph[valve]["distances"] if x not in opened]:
                explore(k, opened, minutes - graph[valve]["distances"][k], pressure)

    explore('AA', [], 30, 0)
    return res

@problem.solver(part=2)
def part2(ls):
    graph = create_graph(ls)
    non_zero_valves = [x for x in graph.keys() if graph[x]["flow"] != 0]

    for k in non_zero_valves + ['AA']:
        graph[k]['distances'] = {}
        for k2 in non_zero_valves:
            graph[k]['distances'][k2] = find_shortest_path(graph, graph[k]["conns"], k2)

    res = 0

    def explore(valve, opened, minutes, pressure, elephant):
        nonlocal res

        if pressure > res:
            res = pressure

        if minutes <= 0: return

        if valve not in opened:
            new_pressure = pressure + graph[valve]["flow"] * minutes
            explore(valve, [x for x in opened] + [valve], minutes - 1, new_pressure, elephant)
            if not elephant:
                explore('AA', [x for x in opened] + [valve], 25, new_pressure, True)
        else:
            for k in [x for x in graph[valve]["distances"] if x not in opened]:
                explore(k, opened, minutes - graph[valve]["distances"][k], pressure, elephant)

    explore('AA', [], 26, 0, False)
    return res

if __name__ == "__main__":
    problem.solve()