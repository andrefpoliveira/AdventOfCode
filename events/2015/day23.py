from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/23: Opening the Turing Lock")
problem.preprocessor = ppr.lsv

def compute(lines, a=0):
    line = 0
    values = {"a": a, "b": 0}
    while line < len(lines):
        current = lines[line].split(" ")
        register = current[1] if current[0] not in ["jie", "jio"] else current[1][:-1]

        if "hlf" == current[0]:
            values[register] //= 2
            line += 1
        elif "tpl" == current[0]:
            values[register] *= 3
            line += 1
        elif "inc" == current[0]:
            values[register] += 1
            line += 1
        elif "jmp" == current[0]:
            offset = int(register[1:])
            line += offset if register[0] == "+" else -offset
        elif "jie" == current[0]:
            if values[register] % 2 == 0:
                offset = int(current[2][1:])
                line += offset if current[2][0] == "+" else -offset
            else:
                line += 1
        else:
            if values[register] == 1:
                offset = int(current[2][1:])
                line += offset if current[2][0] == "+" else -offset
            else:
                line += 1

    return values["b"]

@problem.solver()
def solve(ls):
    return compute(ls), compute(ls, 1)

if __name__ == "__main__":
    problem.solve()
