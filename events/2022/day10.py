from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/10: Cathode-Ray Tube")
problem.preprocessor = ppr.lsv

@problem.solver()
def solver(ls):
    X, cycles = 1, 0
    score, objective = 0, 20
    crt = ["."] * 40 * 6

    for l in ls:
        if "noop" in l: v, steps = 0, 1
        else: v, steps = int(l.split()[1]), 2

        for _ in range(steps):
            if cycles % 40 in (X-1, X, X+1):
                crt[cycles] = "#"

            cycles += 1
            if cycles == objective:
                score += X * objective
                objective += 40
        X += v

    for i in range(0, 40*6, 40):
        print(''.join(x if x=="#" else " " for x in crt[i:i+40]))

    return score, "BPJAZGAP"

if __name__ == "__main__":
    problem.solve()