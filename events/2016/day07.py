import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/07: Internet Protocol Version 7")
problem.preprocessor = ppr.lsv

def has_abba(ls):
    for l in ls:
        for i in range(3, len(l)):
            if l[i-3] == l[i] and l[i-2] == l[i-1] and l[i] != l[i-1]: return True
    return False

def has_aba(ls, previous_combs=[]):
    combs = []
    for l in ls:
        for i in range(2, len(l)):
            if l[i-2] == l[i] and l[i-1] != l[i]:
                if previous_combs != [] and (l[i], l[i-1]) in previous_combs:
                    return True, []

                combs.append((l[i-1], l[i]))

    return len(combs) > 0 if previous_combs == [] else False, combs

@problem.solver(part=1)
def part1(ls):
    count = 0
    for l in ls:
        splt = l.replace("[", " ").replace("]", " ").split(" ")
        
        brackets = [splt[i] for i in range(1, len(splt), 2)]
        no_brackets = [splt[i] for i in range(0, len(splt), 2)]

        if not has_abba(brackets) and has_abba(no_brackets): count += 1
        
    return count

@problem.solver(part=2)
def part2(ls):
    count = 0
    for l in ls:
        splt = l.replace("[", " ").replace("]", " ").split(" ")
        
        brackets = [splt[i] for i in range(1, len(splt), 2)]
        no_brackets = [splt[i] for i in range(0, len(splt), 2)]

        brack_aba, combs = has_aba(brackets)
        if brack_aba:
            no_brack_aba, _ = has_aba(no_brackets, combs)
            if no_brack_aba: 
                count += 1
        
    return count

if __name__ == "__main__":
    problem.solve()