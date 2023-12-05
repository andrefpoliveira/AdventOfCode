from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/08: I Heard You Like Registers")
problem.preprocessor = ppr.lsv
    
def get_value(s, d):
    return d.get(s, 0)

@problem.solver()
def solver(ls):
    d = dict()
    part2 = 0
    for l in ls:
        strp = l.split()
        if eval(f"{get_value(strp[-3], d)} {' '.join(strp[-2:])}"):
            v = get_value(strp[0], d)
            if "inc" in strp:
                d[strp[0]] = v + int(strp[2])
            else:
                d[strp[0]] = v - int(strp[2])

            part2 = max(part2, max(d.values()))

    return max(d.values()), part2

if __name__ == "__main__":
    problem.solve()