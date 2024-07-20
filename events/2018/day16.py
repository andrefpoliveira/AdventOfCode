from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2018/16: Chronal Classification")
problem.preprocessor = ppr.I

def addr(a, b, c, registers):
	registers[c] = registers[a] + registers[b]

def addi(a, b, c, registers):
	registers[c] = registers[a] + b

def mulr(a, b, c, registers):
	registers[c] = registers[a] * registers[b]

def muli(a, b, c, registers):
	registers[c] = registers[a] * b

def banr(a, b, c, registers):
	registers[c] = registers[a] & registers[b]

def bani(a, b, c, registers):
	registers[c] = registers[a] & b

def borr(a, b, c, registers):
	registers[c] = registers[a] | registers[b]

def bori(a, b, c, registers):
	registers[c] = registers[a] | b

def setr(a, b, c, registers):
	registers[c] = registers[a]

def seti(a, b, c, registers):
	registers[c] = a

def gtir(a, b, c, registers):
	registers[c] = 1 if a > registers[b] else 0

def gtri(a, b, c, registers):
	registers[c] = 1 if registers[a] > b else 0

def gtrr(a, b, c, registers):
	registers[c] = 1 if registers[a] > registers[b] else 0

def eqir(a, b, c, registers):
	registers[c] = 1 if a == registers[b] else 0

def eqri(a, b, c, registers):
	registers[c] = 1 if registers[a] == b else 0

def eqrr(a, b, c, registers):
	registers[c] = 1 if registers[a] == registers[b] else 0

operations = set([addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr])

@problem.solver(part=1)
def part1(s):
	v = 0
	for l in s.split("\n\n")[:-2]:
		ns = [int(x) for x in re.findall(r"\d+", l)]
		before, inp, after = ns[:4], ns[4:8], ns[8:]

		count = 0
		opcode, *inputs =  inp
		for op in operations:
			_bef = before[:]
			op(*inputs, _bef)
			if after == _bef:
				count += 1

		if count >= 3:
			v += 1
	return v


@problem.solver(part=2)
def part2(s):
	opcode_mapping = {k: [x for x in operations] for k in range(17)}

	for l in s.split("\n\n")[:-2]:
		ns = [int(x) for x in re.findall(r"\d+", l)]
		before, inp, after = ns[:4], ns[4:8], ns[8:]

		count = 0
		opcode, *inputs =  inp
		keeping_ops = []
		ops = opcode_mapping[opcode]
		for op in operations:
			_bef = before[:]
			op(*inputs, _bef)
			if after == _bef:
				keeping_ops.append(op)
		opcode_mapping[opcode] = keeping_ops

	opcodes_used = set()
	while len(opcodes_used) != 16:
		k = sorted(
			list(opcode_mapping.keys()),
			key=lambda k: len(opcode_mapping[k]) if isinstance(opcode_mapping[k], list) else 100
		)[0]

		op = opcode_mapping[k][0]
		opcodes_used.add(op)
		opcode_mapping[k] = op

		for v in opcode_mapping.values():
			if isinstance(v, list) and op in v:
				v.remove(op)

	before = [0,0,0,0]
	for l in s.split("\n\n")[-1].split("\n"):
		ns = list(map(int, re.findall("\d+", l)))
		op = opcode_mapping[ns[0]]
		op(*ns[1:], before)

	return before[0]


if __name__ == "__main__":
    problem.solve()