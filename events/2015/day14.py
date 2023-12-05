from utils import problem

problem = problem.Problem("2015/14: Reindeer Olympics")
problem.preprocessor = lambda x: {line.split()[0]: [int(line.split()[3]), int(line.split()[6]), int(line.split()[-2])] for line in x.strip().split("\n")}

@problem.solver(part=1)
def part1(d):
    max_distance = 0

    for r in d:
        spd, time, rest = d[r]
        current_time = 2503
        current_dist = 0
        while current_time > 0:
            current_dist += spd * (time if current_time - time > 0 else current_time - time)
            current_time -= (time + rest)

        if current_dist > max_distance:
            max_distance = current_dist

    return max_distance

@problem.solver(part=2)
def part2(d):
    distances = []
    for r in d:
        l = []
        spd, time, rest = d[r]
        current_time = 2503
        current_dist = 0
        t1, t2 = time, rest
        while current_time > 0:
            if t1 > 0:
                current_dist += spd
                t1 -= 1
            elif t2 > 0:
                t2 -= 1
            else:
                t1, t2 = time,rest
                continue
            l.append(current_dist)
            current_time -= 1

        distances.append(l)

    points = [0 for _ in range(len(d.keys()))]
    for i in range(2503):
        max_distance = max(x[i] for x in distances)
        for j in range(len(d.keys())):
            if distances[j][i] == max_distance:
                points[j] += 1

    return max(points)

if __name__ == "__main__":
    problem.solve()