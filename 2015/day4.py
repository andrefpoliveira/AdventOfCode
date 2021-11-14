import hashlib

def solve(input_text, number_of_zeros, starting_value=1):
    n = starting_value
    while True:
        h = hashlib.md5((input_text + str(n)).encode())
        if h.hexdigest()[:number_of_zeros] == "0"*number_of_zeros:
            return n
        n += 1

if __name__ == "__main__":
    with open("./2015/inputs/day4.txt", "r") as f:
        input_text = f.read()

    part1 = solve(input_text, 5)
    print(f"Day 4 Part 1: {part1}")
    print(f"Day 4 Part 2: {solve(input_text, 6, part1)}")