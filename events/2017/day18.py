from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2017/18: Duet")
problem.preprocessor = ppr.lsv

class Simulator:
    def __init__(self, ls, values = {}):
        self.ls = ls
        self.values = values
        self.waiting = False
        self.played = []
        self.idx = 0
        self.sent_count = 0
        self.pair = None

    def get_sent_value(self):
        if not self.played: return None
        return self.played.pop(0)

    def get_value(self, arg):
        try:
            return int(arg)
        except:
            return self.values.get(arg, 0)

    def execute_snd(self, args):
        self.sent_count += 1
        self.played.append(self.get_value(args[0]))
        self.idx += 1

    def execute_set(self, args):
        self.values[args[0]] = self.get_value(args[1])
        self.idx += 1

    def execute_add(self, args):
        self.values[args[0]] = self.get_value(args[0]) + self.get_value(args[1])
        self.idx += 1

    def execute_mul(self, args):
        self.values[args[0]] = self.get_value(args[0]) * self.get_value(args[1])
        self.idx += 1
                
    def execute_mod(self, args):
        self.values[args[0]] = self.get_value(args[0]) % self.get_value(args[1])
        self.idx += 1

    def execute_rcv(self, args):
        if self.pair:
            value = self.pair.get_sent_value()
            if value != None:
                self.idx += 1
                self.waiting = False
                self.values[args[0]] = value
                return value
            else:
                self.waiting = True

        else:    
            if self.get_value(args[0]) > 0:
                return self.played[-1]
        
            self.idx += 1

    def execute_jgz(self, args):
        if self.get_value(args[0]) > 0:
            self.idx += self.get_value(args[1])
        else:
            self.idx += 1
        
    def step(self):
        inst, *args = self.ls[self.idx].split()
        func = getattr(self, f"execute_{inst}")
        value = func(args)
        return value    

@problem.solver(part=1)
def part1(ls):
    s = Simulator(ls)
    while True:
        v = s.step()
        if v: return v

@problem.solver(part=2)
def part2(ls):
    s0 = Simulator(ls, {"p": 0})
    s1 = Simulator(ls, {"p": 1})
    s0.pair = s1
    s1.pair = s0

    while not s0.waiting or not s1.waiting:
        s0.step()
        s1.step()

    return s1.sent_count

if __name__ == "__main__":
    problem.solve()