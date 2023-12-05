from utils import problem

problem = problem.Problem("2018/07: The Sum of Its Parts")
problem.preprocessor = lambda x: [(l.split()[1], l.split()[7]) for l in x.split("\n")]

def find_candidates(steps, ls):
    return [s for s in steps if all(b != s for (_, b) in ls)]

def time(c):
    return 60 + ord(c) - ord('A')

@problem.solver(part=1)
def part1(ls):
    steps = set([s[0] for s in ls] + [s[1] for s in ls])
    order = ""

    while steps:
        candidates = sorted(find_candidates(steps, ls))

        n = candidates[0]
        order += n
        steps.remove(n)
        ls = [(a, b) for (a, b) in ls if a != n]

    return order

@problem.solver(part=2)
def part2(ls):
    steps = set([s[0] for s in ls] + [s[1] for s in ls])

    t = 0
    workers = [0 for _ in range(5)]
    work = [None for _ in range(5)]
    while steps or any(w > 0 for w in workers):
        candidates = sorted(find_candidates(steps, ls))[::-1]

        for i in range(5):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    ls = [(a, b) for (a, b) in ls if a != work[i]]
                if candidates:
                    n = candidates.pop()
                    workers[i] = time(n)
                    work[i] = n
                    steps.remove(n)
        
        t += 1
    return t



if __name__ == "__main__":
    problem.solve()