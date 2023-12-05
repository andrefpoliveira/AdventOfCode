from itertools import permutations
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/13: Knights of the Dinner Table")
problem.preprocessor = ppr.lsv

def seating_arrangement(d, list_people):
    max_hap = 0
    for p in permutations(list_people, len(list_people)):
        current_hap = d[f"{p[-1]}-{p[0]}"]
        current_hap += d[f"{p[0]}-{p[-1]}"]

        for i in range(1, len(list_people)):
            current_hap += d[f"{p[i-1]}-{p[i]}"]
            current_hap += d[f"{p[i]}-{p[i-1]}"]

        if current_hap > max_hap:
            max_hap = current_hap
    return max_hap

@problem.solver()
def solve(input_text):
    d = {}
    list_people = set()
    for line in input_text:
        splitted = line.strip().split(" ")
        if "lose" in line:
            p1, hap, p2 = splitted[0], -int(splitted[3]), splitted[10][:-1]
        else:
            p1, hap, p2 = splitted[0], int(splitted[3]), splitted[10][:-1]

        d[f"me-{p1}"] = 0
        d[f"{p1}-me"] = 0
        d[f"{p1}-{p2}"] = hap

        list_people.add(p1)

    p1 = seating_arrangement(d, list_people)
    list_people.add("me")
    return p1, seating_arrangement(d, list_people)

if __name__ == "__main__":
    problem.solve()