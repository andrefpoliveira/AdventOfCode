import copy
import time

min_mana = float("Inf")
part2 = False

# Id, Mana Cost, Dmg, Healing, Armor, Mana, Turns
spells = [
    [0, 53, 4, 0, 0, 0, 0],
    [1, 73, 2, 2, 0, 0, 0],
    [2, 113, 0, 0, 7, 0, 6],
    [3, 173, 3, 0, 0, 0, 6],
    [4, 229, 0, 0, 0, 101, 5]
]

def solve(boss_hp, boss_dmg, active_spells, player_turn, mana_spent, my_hp = 50, mana_available = 500):
    global min_mana, part2

    my_armor = 0

    if player_turn and part2:
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
                solve(boss_hp, boss_dmg, copy_active_spells, False, mana_spent + spell[1], my_hp, mana_available - spell[1])
    else:
        my_hp += my_armor - boss_dmg if my_armor - boss_dmg < 0 else -1
        if my_hp > 0:
            solve(boss_hp, boss_dmg, new_active_spells, True, mana_spent, my_hp, mana_available)
    
    return min_mana

def run():
    with open("./2015/inputs/day22.txt", "r") as f:
        lines = f.readlines()
        boss_hit = int(lines[0].strip().split(" ")[-1])
        boss_dmg = int(lines[1].strip().split(" ")[-1])

    start = time.time()
    print(f"Day 22 Part 1: {solve(boss_hit, boss_dmg, [], True, 0)}")
    middle = time.time()
    min_mana, part2 = float("Inf"), True
    print(f"Day 22 Part 2: {solve(boss_hit, boss_dmg, [], True, 0)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()