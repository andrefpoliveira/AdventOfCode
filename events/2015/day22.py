import copy
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/22: Wizard Simulator 20XX")
problem.preprocessor = ppr.lsv

min_mana = float("Inf")

# Id, Mana Cost, Dmg, Healing, Armor, Mana, Turns
spells = [
    [0, 53, 4, 0, 0, 0, 0],
    [1, 73, 2, 2, 0, 0, 0],
    [2, 113, 0, 0, 7, 0, 6],
    [3, 173, 3, 0, 0, 0, 6],
    [4, 229, 0, 0, 0, 101, 5]
]

def battle(boss_hp, boss_dmg, active_spells, player_turn, mana_spent, my_hp = 50, mana_available = 500, part2=False):
    global min_mana

    my_armor = 0

    if part2:
        my_hp -= 1
        if my_hp <= 0: return -1

    new_active_spells = []
    for active_spell in active_spells:
        if active_spell[6] >= 0:
            boss_hp -= active_spell[2]
            my_hp += active_spell[3]
            my_armor += active_spell[4]
            mana_available += active_spell[5]

        if active_spell[6] > 1:
            new_active_spells.append([active_spell[0], active_spell[1], active_spell[2], active_spell[3], active_spell[4], active_spell[5], active_spell[6] - 1])

    if boss_hp <= 0:
        min_mana = min(min_mana, mana_spent)
        return min_mana

    if mana_spent > min_mana:
        return -1

    if player_turn:
        ids = [x[0] for x in new_active_spells]
        for spell in spells:
            if spell[0] not in ids and spell[1] <= mana_available:
                copy_active_spells = copy.deepcopy(new_active_spells)
                copy_active_spells.append(spell)
                battle(boss_hp, boss_dmg, copy_active_spells, False, mana_spent + spell[1], my_hp, mana_available - spell[1], part2=part2)
    else:
        my_hp += my_armor - boss_dmg if my_armor - boss_dmg < 0 else -1
        if my_hp > 0:
            battle(boss_hp, boss_dmg, new_active_spells, True, mana_spent, my_hp, mana_available, part2=part2)
    
    return min_mana

@problem.solver()
def solve(ls):
    global min_mana
    boss_hit = int(ls[0].strip().split(" ")[-1])
    boss_dmg = int(ls[1].strip().split(" ")[-1])

    part1 = battle(boss_hit, boss_dmg, [], True, 0)
    min_mana = float("Inf")
    return part1, battle(boss_hit, boss_dmg, [], True, 0, part2=True)

if __name__ == "__main__":
    problem.solve()