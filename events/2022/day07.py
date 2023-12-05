from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2022/07: No Space Left On Device")
problem.preprocessor = ppr.lsv

def create_filesystem(ls):
    data, current = {'/': [None, 0]}, None
    id = 0

    while id < len(ls):
        line = ls[id]

        command = line.split()[1:]

        if command[0] == "cd":
            dir = command[1]
            if dir == '/':
                current = dir
                id += 1
            elif dir == '..':
                current = data[current][0]
                id += 1
            else:
                data[f"{current}_{dir}"] = [current, 0]
                current = f"{current}_{dir}"
                id += 1
        else:
            id += 1
            while id < len(ls) and ls[id][0] != '$':
                line = ls[id]
                if line[:3] == "dir": pass
                else:
                    size, _ = line.split()
                    temp = current
                    while temp != None:
                        d = data[temp]
                        d[1] += int(size)
                        data[temp] = d
                        temp = d[0]
                id += 1
    return data

@problem.solver()
def solver(ls):
    data = create_filesystem(ls)
    space_needed = 30000000 - (70000000 - data['/'][1])
    volumes = sorted([v[1] for _, v in data.items()])

    return sum([v for v in volumes if v <= 100000]), [v for v in volumes if v >= space_needed][0]

if __name__ == "__main__":
    problem.solve()