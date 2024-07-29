from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2018/19: Go With The Flow")
problem.preprocessor = ppr.lsv

def execute(r0=0):
	"""
	# ip 2

	00 | addi 2 16 2		ip += 16
		goto 19

	01 | seti 1 1 1			r1 = 1
	02 | seti 1 4 3			r3 = 1
	03 | mulr 1 3 5			r5 = r1 * r3
	04 | eqrr 5 4 5			r5 = (r5 == r4)
	05 | addr 5 2 2			ip += r5
	06 | addi 2 1 2			ip += 1
	07 | addr 1 0 0			r0 += r1
	08 | addi 3 1 3			r3 += 1
	09 | gtrr 3 4 5			r5 = (r3 > r4)
	10 | addr 2 5 2			ip += r5
	11 | seti 2 4 2			ip = 2
	12 | addi 1 1 1			r1 += 1
	13 | gtrr 1 4 5			r5 = (r1 > r4)
	14 | addr 5 2 2			ip += r5
	15 | seti 1 0 2			ip = 1
	16 | mulr 2 2 2			ip *= ip

		for r1 = 1..r4
			for r3 = 1..r4
				if r1 * r3 == r5:
					r0 += r1


	17 | addi 4 2 4			r4 += 2
	18 | mulr 4 4 4			r4 = r4^2
	19 | mulr 2 4 4			r4 = ip * r4
	20 | muli 4 11 4		r4 = r4 * 11
	21 | addi 5 1 5			r5 += 1
	22 | mulr 5 2 5			r5 = r5 * ip
	23 | addi 5 17 5		r5 += 17
	24 | addr 4 5 4			r4 += r5
	25 | addr 2 0 2			ip += r0
	26 | seti 0 9 2			ip = 0

		r4 = 2^2 * 19 * 11 + (1 * 22 + 17) = 875

	27 | setr 2 3 5			r5 = ip
	28 | mulr 5 2 5			r5 *= ip
	29 | addr 2 5 5			r5 += ip
	30 | mulr 2 5 5			r5 *= ip
	31 | muli 5 14 5		r5 *= 14
	32 | mulr 5 2 5			r5 += ip
	33 | addr 4 5 4			r4 += r5
	34 | seti 0 9 0			r0 = 0
	35 | seti 0 6 2			ip = 0

		r4 = (27 * 28 + 29) * 30 * 14 * 32 = 10550400
	"""

	r4 = 875 + r0 * 10550400

	sqrt = int(r4 ** 0.5)
	result = sqrt if r4 % sqrt == 0 else 0
	for n in range(1, sqrt):
		if r4 % n == 0:
			result += n + r4 // n

	return result


@problem.solver(part=1)
def part1(ls):
	return execute(r0 = 0)


@problem.solver(part=2)
def part2(ls):
	return execute(r0 = 1)
		

if __name__ == "__main__":
    problem.solve()