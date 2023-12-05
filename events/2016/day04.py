from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2016/04: Security Through Obscurity")
problem.preprocessor = ppr.lsv

def valid_room(room, checksum):
    letters = list(set([x for x in room if x != "-"]))
    letters.sort(key=lambda x: (-room.count(x), ord(x)))
    return ''.join(letters[:5]) == checksum

@problem.solver(part=1)
def part1(rooms):
    count = 0

    for room in rooms:
        spl = room.split("-")
        room = '-'.join(spl[:-1])
        sector_id = int(spl[-1].split("[")[0])
        checksum = spl[-1].split("[")[1][:-1]

        if valid_room(room, checksum):
            count += sector_id

    return count

def decrypt(room, sector_id):
    dec = ""
    for c in room:
        if c == "-":
            dec += " "
        else:
            n = (ord(c) - ord('a') + sector_id) % 26
            dec += chr(ord('a') + n)
    return dec

@problem.solver(part=2)
def part2(rooms):
    for room in rooms:
        spl = room.split("-")
        room = '-'.join(spl[:-1])
        sector_id = int(spl[-1].split("[")[0])
        checksum = spl[-1].split("[")[1][:-1]

        if "northpole" in decrypt(room, sector_id):
            return sector_id

if __name__ == "__main__":
    problem.solve()