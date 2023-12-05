from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/11: Corporate Policy")
problem.preprocessor = ppr.I

def increase(pwd_numbers):
    min_n = ord('a')
    max_n = ord('z')

    for i in range(len(pwd_numbers)-1, -1, -1):
        pwd_numbers[i] += 1
        if pwd_numbers[i] > max_n:
            pwd_numbers[i] = min_n
            continue
        break
    return pwd_numbers

def is_valid(pwd_numbers):
    for i in [105, 108, 111]:
        if i in pwd_numbers:
            return False

    for i in range(2, len(pwd_numbers)):
        if pwd_numbers[i] - pwd_numbers[i-2] == 2 and pwd_numbers[i] - pwd_numbers[i-1] == 1:
            break
    else:
        return False

    i = 1
    count = 0
    while i < len(pwd_numbers):
        if pwd_numbers[i] == pwd_numbers[i-1]:
            i += 2
            count += 1
            continue
        i += 1
    
    return count >= 2

def find_password(pwd):
    pwd_numbers = [ord(x) for x in pwd]
    while True:
        pwd_numbers = increase(pwd_numbers)
        if is_valid(pwd_numbers):
            return ''.join(map(chr, pwd_numbers))

@problem.solver()
def solve(input_text):
    p1 = find_password(input_text)
    p2 = find_password(p1)

    return p1, p2

if __name__ == "__main__":
    problem.solve()