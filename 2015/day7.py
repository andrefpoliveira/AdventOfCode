def transform_left(d, left):
    if left.isdigit():
        return int(left)
    else:
        return d[left]

def solve(input_text, initial_d = {}):
    d = initial_d
    part2 = len(initial_d) == 1
    while "a" not in d:
        for line in input_text:
            line = line.strip()
            left = line.split(" -> ")[0]
            right = line.split(" -> ")[1]

            try:
                if "AND" in left:
                    left = transform_left(d, left.split(" AND ")[0]) & transform_left(d, left.split(" AND ")[1])
                elif "OR" in left:
                    left = transform_left(d, left.split(" OR ")[0]) | transform_left(d, left.split(" OR ")[1])
                elif "LSHIFT" in left:
                    left = transform_left(d, left.split(" LSHIFT ")[0]) << int(left.split(" LSHIFT ")[1])
                elif "RSHIFT" in left:
                    left = transform_left(d, left.split(" RSHIFT ")[0]) >> int(left.split(" RSHIFT ")[1])
                elif "NOT" in left:
                    left = 65525 - transform_left(d, left.replace("NOT ", ""))
                else:
                    left = transform_left(d, left)

                if part2 == False or right != "b":
                    d[right] = left
            except:
                pass
    return d['a']

def run():
    with open("./2015/inputs/day7.txt", "r") as f:
        input_text = f.readlines()

    res = solve(input_text)
    print(f"Day 7 Part 1: {res}")
    print(f"Day 7 Part 2: {solve(input_text, {'b':res})}")

if __name__ == "__main__":
    run()