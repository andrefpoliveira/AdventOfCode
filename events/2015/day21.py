from itertools import combinations
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/21: RPG Simulator 20XX")
problem.preprocessor = ppr.lsv

def part1(boss_hit, boss_dmg, boss_armor, weapons, armor, rings):
    min_cost = float("Inf")
    for weapon in weapons:
        for arm in armor + [(0,0,0)]:
            for c in list(combinations(rings, 2)) + list(combinations(rings, 1)) + list(combinations(rings, 0)):

                items = [weapon, arm]
                for i in c:
                    items.append(i)
                
                cost = sum([x[0] for x in items])
                my_dmg = sum([x[1] for x in items])
                my_armor = sum([x[2] for x in items])

                dmg_dealt = max(1, my_dmg - boss_armor)
                dmg_rec = max(1, boss_dmg - my_armor)

                turns_needed_to_kill = boss_hit // dmg_dealt + (0 if boss_hit % dmg_dealt == 0 else 1)
                turns_needed_to_die = 100 // dmg_rec + + (0 if 100 % dmg_rec == 0 else 1)

                if turns_needed_to_die >= turns_needed_to_kill and cost < min_cost:
                    min_cost = cost
    return min_cost         

def part2(boss_hit, boss_dmg, boss_armor, weapons, armor, rings):
    max_cost = 0
    for weapon in weapons:
        for arm in armor + [(0,0,0)]:
            for c in list(combinations(rings, 2)) + list(combinations(rings, 1)) + list(combinations(rings, 0)):

                items = [weapon, arm]
                for i in c:
                    items.append(i)
                
                cost = sum([x[0] for x in items])
                my_dmg = sum([x[1] for x in items])
                my_armor = sum([x[2] for x in items])

                dmg_dealt = max(1, my_dmg - boss_armor)
                dmg_rec = max(1, boss_dmg - my_armor)

                turns_needed_to_kill = boss_hit // dmg_dealt + (0 if boss_hit % dmg_dealt == 0 else 1)
                turns_needed_to_die = 100 // dmg_rec + + (0 if 100 % dmg_rec == 0 else 1)

                if turns_needed_to_die < turns_needed_to_kill and cost > max_cost:
                    max_cost = cost
    return max_cost 

@problem.solver()
def solve(ls):
    boss_hit = int(ls[0].strip().split(" ")[-1])
    boss_dmg = int(ls[1].strip().split(" ")[-1])
    boss_armor = int(ls[2].strip().split(" ")[-1])

    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]

    armor = [
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]

    rings = [
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]

    return part1(boss_hit, boss_dmg, boss_armor, weapons, armor, rings), part2(boss_hit, boss_dmg, boss_armor, weapons, armor, rings)

if __name__ == "__main__":
    problem.solve()