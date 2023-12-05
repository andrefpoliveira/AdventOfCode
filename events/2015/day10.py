from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/10: Elves Look, Elves Say")
problem.preprocessor = ppr.I

def look_and_say(number, reps):
    for i in range(reps):
        new_number = ""
        c = number[0]
        count = 1
        for j in range(1, len(number)):
            if number[j] == c:
                count+=1
            else:
                new_number += str(count) + c
                count = 1
                c = number[j]
        new_number += str(count) + c

        number = new_number
    return len(number)

@problem.solver()
def solve(input_text):
    return look_and_say(input_text, 40), look_and_say(input_text, 50)

if __name__ == "__main__":
    problem.solve()