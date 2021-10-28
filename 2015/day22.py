from itertools import combinations

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

def part2():
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

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        boss_hit = int(lines[0].strip().split(" ")[-1])
        boss_dmg = int(lines[1].strip().split(" ")[-1])

    # Mana Cost, Immediate Dmg, Dmg By Turn, Immediate Healing, Armor by Turn, Mana by Turn, Turns
    spells = [
        [53, 4, 0, 0, 0, 0, 0],
        [73, 2, 0, 2, 0, 0, 0],
        [113, 0, 0, 0, 7, 0, 6],
        [173, 0, 3, 0, 0, 0, 6],
        [229, 0, 0, 0, 0, 101, 5]
    ]

    print(f"Day 20 Part 1: {part1(boss_hit, boss_dmg, spells)}")
    print(f"Day 20 Part 2: {part2()}")