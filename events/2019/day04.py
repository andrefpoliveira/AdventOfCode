from utils import problem

problem = problem.Problem("2019/04: Secure Container")
problem.preprocessor = lambda x: [int(n) for n in x.strip().split("-")]

def is_valid(n, part2=False):
    equal_found = False
    equal_in_row = 0
    for i in range(1, len(n)):
        if ord(n[i]) < ord(n[i-1]): return False
        elif ord(n[i]) == ord(n[i-1]):
            equal_in_row += 1
        else:
            if (not part2 and equal_in_row >= 1) or (part2 and equal_in_row == 1):
                equal_found = True
            equal_in_row = 0
    
    if (not part2 and equal_in_row >= 1) or (part2 and equal_in_row == 1): equal_found = True
         
    return equal_found

@problem.solver()
def solver(vs):
    min_v, max_v = vs
    part1 = part2 = 0
    for n in range(min_v + 1, max_v):
        v = str(n)
        if is_valid(v): part1 += 1
        if is_valid(v, part2=True): part2 += 1

    return part1, part2
        
print("Ok")

if __name__ == "__main__":
    problem.solve()