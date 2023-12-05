from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/09: Marble Mania")
problem.preprocessor = ppr.I

class Node:
    previous, next = None, None
    def __init__(self, value):
        self.value = value

def print_linked(player, linked, value):
    head = linked
    print(f"[{player}] {head.value}", end=" ")
    head = head.next
    while head.value != linked.value:
        if value == head.value:
            print(f"*({head.value})*", end=" ")
        else:
            print(head.value, end=" ")
        head = head.next
    print()

def insert_node(linked, node):
    node.next = linked.next
    node.previous = linked
    linked.next.previous = node
    linked.next = node

def solve(players, marbles):
    player, scores = 0, [0 for _ in range(players)]

    head = Node(0)
    head.next = head
    head.previous = head

    for i in range(1, marbles+1):
        if i % 23 != 0:
            node = Node(i)
            head = head.next
            insert_node(head, node)
            head = head.next
        else:
            for _ in range(8):
                head = head.previous
            scores[player] += head.next.value + i
            head.next = head.next.next
            head = head.next
            
        player = (player + 1) % players

    return max(scores)

@problem.solver(part=1)
def part1(s):
    players, marbles = map(int, re.match(r"(\d+) players; last marble is worth (\d+) points", s).groups())
    return solve(players, marbles)

@problem.solver(part=2)
def part2(s):
    players, marbles = map(int, re.match(r"(\d+) players; last marble is worth (\d+) points", s).groups())
    return solve(players, marbles * 100)

if __name__ == "__main__":
    problem.solve()