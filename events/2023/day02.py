from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2023/02: Cube Conundrum")
problem.preprocessor = ppr.lsv

@problem.solver()
def solver(ls):
    CUBES = dict(red=12, green=13, blue=14)

    part1 = part2 = 0

    for l in ls:
        game_id = int(re.findall(r"Game (\d+): ", l)[0])
        games = l.split(": ")[1].split(";")
        
        max_r = max_g = max_b = 0
        valid = True
        for game in games:
            d = dict(red=0, green=0, blue=0)
            info = game.replace(",", "").split()

            for i in range(0, len(info), 2):
                n, color = info[i:i+2]
                d[color] = int(n)

                if d["red"] > CUBES["red"] or d["green"] > CUBES["green"] or d["blue"] > CUBES["blue"]:
                    valid = False

                max_r = max(max_r, d["red"])
                max_g = max(max_g, d["green"])
                max_b = max(max_b, d["blue"])

        part2 += max_r * max_g * max_b

        if valid:
            part1 += game_id

    return part1, part2

if __name__ == "__main__":
    problem.solve()