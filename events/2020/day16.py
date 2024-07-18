from utils import problem
from utils import preprocessing as ppr

import re

problem = problem.Problem("2020/16: Ticket Translation")
problem.preprocessor = ppr.lsv

def parse_input(ls):
	fields = {}
	ticket = []
	nearby = []

	for i in range(len(ls)):
		if ls[i] == "":
			break

		field, *ranges = re.findall(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", ls[i])[0]
		fields[field] = [(int(ranges[0]), int(ranges[1])), (int(ranges[2]), int(ranges[3]))]
	
	ticket = list(map(int, ls[i + 2].split(",")))

	for i in range(i + 5, len(ls)):
		nearby.append(list(map(int, ls[i].split(","))))

	return fields, ticket, nearby

def part1(fields, ticket, nearby):
	invalid = 0
	valid_tickets = []

	for n in nearby:
		ticket_valid = True

		for v in n:
			valid = False
			for r in fields.values():
				if r[0][0] <= v <= r[0][1] or r[1][0] <= v <= r[1][1]:
					valid = True
					break

			if not valid:
				invalid += v
				ticket_valid = False

		if ticket_valid:
			valid_tickets.append(n)

	return invalid, valid_tickets
			
@problem.solver()
def solver(ls):
	fields, ticket, nearby = parse_input(ls)
	p1, valid_tickets = part1(fields, ticket, nearby)

	valid_cols_to_field = {}

	for field in fields:
		r = fields[field]
		for col in range(len(ticket)):
			values = [x[col] for x in valid_tickets]
			if all(
				(
					(r[0][0] <= v <= r[0][1]) or (r[1][0] <= v <= r[1][1])
					for v in values
				)
			):
				valid_cols_to_field[field] = valid_cols_to_field.get(field, []) + [col]

	# Sort the dictionary by the number of possible columns
	valid_cols_to_field = dict(
		sorted(
			valid_cols_to_field.items(),
			key=lambda x: len(x[1]),
		)
	)

	field_to_col = {}
	cols = set()
	for f in valid_cols_to_field:
		options = set(valid_cols_to_field[f]) - cols
		if len(options) != 1:
			raise Exception("Too many options", options)
		field_to_col[f] = options.pop()
		cols.add(field_to_col[f])

	p2 = 1
	for field, col in field_to_col.items():
		if field.startswith("departure"):
			p2 *= ticket[col]

	return p1, p2

if __name__ == "__main__":
    problem.solve()