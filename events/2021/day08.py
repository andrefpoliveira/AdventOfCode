from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/08: Seven Segment Search")
problem.preprocessor = ppr.lsv

conv = {
    'abcefg': '0', 
    'cf': '1', 
    'acdeg': '2', 
    'acdfg': '3', 
    'bcdf': '4', 
    'abdfg': '5', 
    'abdefg': '6', 
    'acf': '7', 
    'abcdefg': '8', 
    'abcdfg': '9' 
}

@problem.solver(part=1)
def part1(ls):
    count = 0
    for l in ls:
        output = l.split("|")[1].strip().split()
        for i in output:
            if len(i) in [2, 3, 4, 7]:
                count += 1
    return count

def find_combination(numbers):
    d = {}
    for n in numbers:
        if len(n) == 2: _2 = n

    # Get a
    for n in numbers:
        if len(n) == 3: # 7
            _7 = n
            break
    for c in _7:
        if c not in _2:
            d[c] = 'a'
            break

    # Get c and f
    for n in numbers:
        if len(n) == 6 and (_2[0] in n) != (_2[1] in n):
            if _2[0] in n:
                d[_2[0]] = 'f'
                d[_2[1]] = 'c'
            else:
                d[_2[0]] = 'c'
                d[_2[1]] = 'f'
            break

    # Get hipothesis for b and d
    for n in numbers:
        if len(n) == 4:
            bd = ''.join(x for x in n if x not in _2)

    # Get b and d
    for n in numbers:
        if len(n) == 6 and (bd[0] in n) != (bd[1] in n):
            if bd[0] in n:
                d[bd[0]] = 'b'
                d[bd[1]] = 'd'
            else:
                d[bd[0]] = 'd'
                d[bd[1]] = 'b'

    # Get hipothesis for e and g
    eg = ''.join(x for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] if x not in d.keys())

    # Get e and g
    for n in numbers:
        if len(n) == 5 and (eg[0] in n) != (eg[1] in n):
            if eg[0] in n:
                d[eg[0]] = 'g'
                d[eg[1]] = 'e'
            else:
                d[eg[0]] = 'e'
                d[eg[1]] = 'g'
    
    return d

@problem.solver(part=2)
def part2(ls):
    total = 0
    for l in ls:
        nums, output = l.split("|")
        d = find_combination(nums.strip().split())

        segments = [''.join([d[c] for c in word]) for word in output.strip().split()]
        real_outputs = [''.join(sorted(w)) for w in segments]
        total += int(''.join(conv[n] for n in real_outputs))

    return total

if __name__ == "__main__":
    problem.solve()