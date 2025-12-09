from utils import problem
from utils import preprocessing as ppr
from utils import geometry as geo
problem = problem.Problem("2025/08: Playground")
problem.preprocessor = ppr.lsv

def calculate_distances(boxes):
    distances = {}
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if i >= j:
                continue
            d = geo.euclidean(box1, box2)
            distances[(i, j)] = d
    
    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    return sorted_distances

def find_group(groups, id):
    for g in groups:
        if id in g:
            return g
    return None

@problem.solver()
def solve(inp):
    p1, p2 = 0, 0

    boxes = []

    for v in inp:
        boxes.append(tuple(map(int, v.split(','))))

    cons = 0
    groups = []
    distances = calculate_distances(boxes)

    for k in distances.keys():
        i, j = k
        group_i = find_group(groups, i)
        group_j = find_group(groups, j)

        if group_i is None and group_j is None:
            groups.append(set([i, j]))
        elif group_i is not None and group_j is None:
            group_i.add(j)
        elif group_i is None and group_j is not None:
            group_j.add(i)
        elif group_i is not group_j:
            group_i.update(group_j)
            groups.remove(group_j)

        cons += 1

        if len(groups) == 1 and sum(len(x) for x in groups) == len(boxes):
            b1, b2 = boxes[i], boxes[j]
            p2 = b1[0] * b2[0]
            return p1, p2

        if cons >= 1000 and p1 == 0:
            _groups = sorted([len(x) for x in groups], reverse=True)
            p1 = _groups[0] * _groups[1] * _groups[2]

if __name__ == "__main__":
    problem.solve()