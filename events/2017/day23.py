from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/23: Coprocessor Conflagration")
problem.preprocessor = ppr.lsv

class Simulator:
    def __init__(self, ls, values = {}):
        self.ls = ls
        self.values = values
        self.idx = 0
        self.mult_counter = 0

    def get_value(self, arg):
        try:
            return int(arg)
        except:
            return self.values.get(arg, 0)

    def execute_sub(self, args):
        self.values[args[0]] = self.get_value(args[0]) - self.get_value(args[1])
        self.idx += 1

    def execute_set(self, args):
        self.values[args[0]] = self.get_value(args[1])
        self.idx += 1

    def execute_mul(self, args):
        self.mult_counter += 1
        self.values[args[0]] = self.get_value(args[0]) * self.get_value(args[1])
        self.idx += 1

    def execute_jnz(self, args):
        if self.get_value(args[0]) != 0:
            self.idx += self.get_value(args[1])
        else:
            self.idx += 1
        
    def step(self):
        if self.idx >= len(self.ls): return -1
        inst, *args = self.ls[self.idx].split()
        func = getattr(self, f"execute_{inst}")
        value = func(args)
        return value 

@problem.solver(part=1)
def part1(ls):
    s = Simulator(ls)
    v = None
    while v is None:
        v = s.step()
    return s.mult_counter

@problem.solver(part=2)
def part2(ls):
    # Composite numbers
    b = 81 * 100 + 100000
    h = 0
    for i in range(b, b + 17001, 17):
        for x in range(2, i):
            if i % x == 0:
                h += 1
                break
    return h

if __name__ == "__main__":
    problem.solve()