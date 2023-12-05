from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/09: Stream Processing")
problem.preprocessor = ppr.I

@problem.solver()
def solver(s):
    open, score, garbage_count = 1, 0, 0
    inside_garbage, exclamation = False, False

    for i in s:
        if exclamation:
            exclamation = False
        elif i == "!":
            exclamation = True
        
        elif i == "<" and not inside_garbage:
            inside_garbage = True
        elif i == ">" and inside_garbage:
            inside_garbage = False

        elif i == "{" and not inside_garbage:
            score += open
            open += 1

        elif i == "}" and not inside_garbage:
            open -= 1

        elif inside_garbage:
            garbage_count += 1

    return score, garbage_count

if __name__ == "__main__":
    problem.solve()