from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/10: Syntax Scoring")
problem.preprocessor = ppr.lsv

points_part1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137 
}

points_part2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4 
}

match = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

incomplete = []
@problem.solver(part=1)
def part1(ls):
    points = 0
    for l in ls:
        stack = []
        for c in l:
            if c in ["(", "[", "{", "<"]: stack.append(c)
            else:
                v = stack.pop()
                if match[v] != c:
                    points += points_part1[c]
                    break
        else:
            incomplete.append(stack)
    return points

@problem.solver(part=2)
def part2(ls):
    scores = []
    for l in incomplete:
        score = 0
        for c in l[::-1]:
            score *= 5
            score += points_part2[c]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == "__main__":
    problem.solve()
