from itertools import permutations
import time

def solve(number, reps):
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

def run():
    with open("./year2015/inputs/day10.txt", "r") as f:
        input_text = f.read().strip()

    start = time.time()
    print(f"Day 10 Part 1: {solve(input_text, 40)}")
    middle = time.time()
    print(f"Day 10 Part 2: {solve(input_text, 50)}")
    end = time.time()

    return [middle - start, end - middle, end - start]

if __name__ == "__main__":
    run()