from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2020/14: Docking Data")
problem.preprocessor = ppr.lsv

def process_mask(mask):
	return (
		[(len(mask) - 1 - i, int(bit)) for i, bit in enumerate(mask) if bit != "X"],
		[len(mask) - 1 - i for i, bit in enumerate(mask) if bit == "X"]
	)

def get_bits(value):
	return [i for i in range(32) if value & (1 << i)]

def set_bit(value, bit):
	return value | (1 << bit)

def clear_bit(value, bit):
	return value & ~(1 << bit)

def generate_registres(reg, floatings):
	if not floatings:
		return [reg]

	bit = floatings[0]
	floatings = floatings[1:]

	return generate_registres(set_bit(reg, bit), floatings) + generate_registres(clear_bit(reg, bit), floatings)

@problem.solver(part=1)
def part1(ls):
	memory = {}

	for inst in ls:
		if "mask" in inst:
			mask, _ = process_mask(inst.split(" = ")[1])
			continue

		reg, value = map(int,re.findall(r"(\d+)", inst))
		for bit, bit_value in mask:
			if bit_value == 1:
				value = set_bit(value, bit)
			else:
				value = clear_bit(value, bit)

		memory[reg] = value

	return sum(memory.values())

@problem.solver(part=2)
def part2(ls):
	memory = {}

	for inst in ls:
		if "mask" in inst:
			mask, floating = process_mask(inst.split(" = ")[1])
			continue

		reg, value = map(int,re.findall(r"(\d+)", inst))
		for bit, bit_value in mask:
			if bit_value == 1:
				reg = set_bit(reg, bit)

		for r in generate_registres(reg, floating):
			memory[r] = value

	return sum(memory.values())

if __name__ == "__main__":
    problem.solve()