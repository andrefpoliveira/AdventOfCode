from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2017/20: A Series of Tubes")
problem.preprocessor = ppr.lsv

def manhattan_distance(x, y, z):
    return abs(x) + abs(y) + abs(z)

particles = []

@problem.solver(part=1)
def part1(ls):
    global particles

    for i in range(len(ls)):
        numbers = [int(x) for x in re.findall("-?\d+", ls[i])]
        p = numbers[:3]
        v = numbers[3:6]
        a = numbers[6:]
        particles.append((i, p, v, a))
    
    particles.sort(key = lambda x: (manhattan_distance(*x[3]), manhattan_distance(*x[2]), manhattan_distance(*x[1])))
    print(particles[0])
    return particles[0][0]

@problem.solver(part=2)
def part2(_):
    global particles
    for _ in range(50):
        new_particles = []

        table = {}
        for part in particles:
            id, p, v, a = part
            v = tuple([v[i] + a[i] for i in range(3)])
            p = tuple([p[i] + v[i] for i in range(3)])

            l = table.get(p, [])
            l.append((id, p, v, a))
            table[p] = l
    
        for k in table:
            l = table[k]
            if len(l) == 1:
                new_particles += l

        particles = new_particles
    return len(particles)

if __name__ == "__main__":
    problem.solve()