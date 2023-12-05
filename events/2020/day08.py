from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/08: Handheld Halting")
problem.preprocessor = ppr.lsv

def get_acc_value(ls):
    acc = pointer = 0
    visited = set()

    while pointer not in visited and pointer < len(ls):
        visited.add(pointer)
        inst, number = ls[pointer].split()

        if inst == "acc":
            acc += int(number)
            pointer += 1
        elif inst == "jmp":
            pointer += int(number)
        else:
            pointer += 1

    return acc, pointer >= len(ls)

@problem.solver(part=1)
def part1(ls):
    acc, _ = get_acc_value(ls)
    return acc

@problem.solver(part=2)
def part2(ls):
    for i in range(len(ls)):
        line = ls[i]

        if "jmp" in line or "nop" in line:
            copy = [x for x in ls]
            
            if "jmp" in line: copy[i] = copy[i].replace("jmp", "nop")
            else: copy[i] = copy[i].replace("nop", "jmp")

            acc, valid = get_acc_value(copy)

            if valid: return acc

    
if __name__ == "__main__":
    problem.solve()