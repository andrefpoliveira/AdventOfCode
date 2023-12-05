from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/03: Binary Diagnostic")
problem.preprocessor = ppr.lsv

def count_bits(ls, id):
    n1 = len([x for x in ls if x[id] == "1"])
    return n1, len(ls)-n1

@problem.solver(part=1)
def part1(ls):
    gamma, eps = "", ""
    for i in range(len(ls[0])):
        _1c , _0c = count_bits(ls, i)

        if _1c > _0c:
            gamma += "1"
            eps += "0"
        else:
            gamma += "0"
            eps += "1"
    return int(gamma, 2) * int(eps, 2)

@problem.solver(part=2)
def part2(ls):
    ls1 = [x for x in ls]

    for i in range(len(ls[0])):
        _1c , _0c = count_bits(ls, i)
        _1c1 , _0c1 = count_bits(ls1, i)

        if len(ls) != 1:
            new_list = [x for x in ls if x[i] == "1"] if _1c >= _0c else [x for x in ls if x[i] == "0"]
        if len(ls1) != 1:
            new_list1 = [x for x in ls1 if x[i] == "0"] if _1c1 >= _0c1 else [x for x in ls1 if x[i] == "1"]

        if len(new_list) == 1 and len(new_list1) == 1:
            break

        ls, ls1 = new_list, new_list1
    return int(new_list[0], 2) * int(new_list1[0], 2)

if __name__ == "__main__":
    problem.solve()