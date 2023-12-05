from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2021/04: Giant Squid")
problem.preprocessor = ppr.lsv

def fill_board(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = "X"
                return True
    return False

def bingo(board):
    if any(len(set(row)) == 1 for row in board): return True   # Rows
    return any(len(set([row[i] for row in board])) == 1 for i in range(5))

def part1(ns, boards):
    for n in ns:
        for board in boards:
            if fill_board(board, n):
                if bingo(board):
                    return n * sum([nb for row in board for nb in row if nb != "X"])

    return -1

def part2(ns, boards):
    for n in ns:
        incomplete_boards = []
        for board in boards:
            if not fill_board(board, n) or not bingo(board):
                incomplete_boards.append(board)

        if len(incomplete_boards) == 0:
            return n * sum([nb for row in boards[0] for nb in row if nb != "X"])

        boards = incomplete_boards

    return -1

@problem.solver()
def solve(ls):
    ns = [int(x) for x in ls[0].split(",")]
    boards = []
    ls = ls[2:]
    while len(ls) > 0:
        board = [[int(x) for x in ls[i].split()] for i in range(5)]
        boards.append(board)
        ls = ls[6:]
    
    return part1(ns, boards), part2(ns, boards)

if __name__ == "__main__":
    problem.solve()