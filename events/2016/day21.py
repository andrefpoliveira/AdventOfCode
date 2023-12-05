import re
from itertools import permutations
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/21: Scrambled Letters and Hash")
problem.preprocessor = ppr.lsv

pwd = "abcdefgh"

@problem.solver(part=1)
def part1(ls):
    global pwd
    for l in ls:
        ns = [int(x) for x in re.findall(r"\d+", l)]
        lets = [x.strip() for x in re.findall(r"( . | .$)", l)]
        left = "left" in l

        if "swap p" in l:
            ns = sorted(ns)
            lst = list(pwd)
            lst[ns[0]], lst[ns[1]] = lst[ns[1]], lst[ns[0]]
            pwd = "".join(lst)

        elif "swap l" in l:
            l1, l2 = lets[0], lets[1]
            new_pwd = ""
            for i in pwd:
                if i in [l1, l2]: new_pwd += l1 if i == l2 else l2
                else: new_pwd += i
            pwd = new_pwd

        elif "rotate b" in l:
            steps = pwd.index(lets[0])
            steps += 1 if steps < 4 else 2
            steps = steps % len(pwd)
            pwd = pwd[-steps:] + pwd[:-steps]

        elif "rotate " in l:
            steps = ns[0] % len(pwd)
            if left:
                pwd = pwd[steps:] + pwd[:steps]
            else:
                pwd = pwd[-steps:] + pwd[:-steps]

        elif "reverse" in l:
            ns = sorted(ns)
            pwd = pwd[:ns[0]] + (pwd[ns[0] : ns[1]+1])[::-1] + pwd[ns[1]+1:]

        else:
            l = pwd[ns[0]]
            pwd = pwd[:ns[0]] + pwd[ns[0]+1:]
            pwd = pwd[:ns[1]] + l + pwd[ns[1]:]
    return pwd

@problem.solver(part=2)
def part2(ls):
    global pwd
    target = "fbgdceah"
    for p in permutations("abcdefgh"):
        pwd = ''.join(p)
        if part1(ls) == target:
            return ''.join(p)

if __name__ == "__main__":
    problem.solve()