import re
from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/09: Explosives in Cyberspace")
problem.preprocessor = ppr.I

def decompress(s, part2=False):
    if "(" not in s: return len(s)-1, s

    if s[0] != "(":
        return 0, s[0]
    else:
        id = s.find(")")
        chars, reps = [int(x) for x in re.findall(r"\d+", s[:id+1])]
        obtain_chars = s[id+1: id+1+chars]

        # print(obtain_chars)

        if part2:
            new_obtain_chars = ""
            total_size = 0
            while total_size != id + chars:
                print(obtain_chars)
                s_size, c_obtain_chars = decompress(obtain_chars, True)
                obtain_chars = obtain_chars[s_size:]
                new_obtain_chars += c_obtain_chars
                total_size += s_size
                print(total_size, id + chars)
            obtain_chars = new_obtain_chars
            # print(obtain_chars)
            # print(obtain_chars)

        res = obtain_chars * reps
        return id + chars, res

@problem.solver()
def solve(s):
    res1 = ""
    res2 = ""
    while len(s) > 0:
        size, txt = decompress(s)
        _, txt2 = decompress(s, True)
        s = s[size+1:]
        # print(s)
        res1 += txt
        res2 += txt2

    # print(res2)

    return len(res1), len(res2)

if __name__ == "__main__":
    problem.solve()