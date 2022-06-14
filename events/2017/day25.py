from utils import problem
from utils import preprocessing as ppr
import re

problem = problem.Problem("2017/25: The Halting Problem")
problem.preprocessor = ppr.I

def create_state_rules(info):
    state_rules = {}

    for id, s in enumerate(info):
        numbers = [int(x) for x in re.findall("value (\d+)", s)]
        dir = re.findall("right|left", s)
        state = re.findall("([A-Z])\.", s)

        state_rules[chr(ord('A') + id)] = list(zip(numbers, dir, state))

    return state_rules

@problem.solver()
def part1(I):
    info = I.split("\n\n")
    steps = int(re.findall("\d+", info[0])[0])

    state_rules = create_state_rules(info[1:])

    pos = 0
    dirs = {"right": 1, "left": -1}
    values = {}
    curr_state = 'A'
    for _ in range(steps):
        value = values.get(pos, 0)
        new_v, direction, curr_state = state_rules[curr_state][value]
        values[pos] = new_v
        pos += dirs[direction]    

    return sum(values.values()), None

if __name__ == "__main__":
    problem.solve()