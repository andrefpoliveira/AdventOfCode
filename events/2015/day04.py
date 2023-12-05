import hashlib
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2015/04: The Ideal Stocking Stuffer")
problem.preprocessor = ppr.I

def ac_miner(input_text):
    lead = 5
    n = 0
    while True:
        h = hashlib.md5((input_text + str(n)).encode())
        if h.hexdigest()[:lead] == "0"*lead:
            yield n
            lead += 1
        n += 1

@problem.solver()
def solve(input_text):
    m = ac_miner(input_text)
    return (next(m), next(m))

if __name__ == "__main__":
    problem.solve()