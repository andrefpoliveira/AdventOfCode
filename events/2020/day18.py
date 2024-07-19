from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2020/18: Operation Order")
problem.preprocessor = ppr.lsv

mult = lambda x, y: x * y
add = lambda x, y: x + y

def evaluate_expression(expression, part2=False):
	# evaluate the expression, recursively
	value = 0
	operator = add
	i = 0
	while i < len(expression):
		
		if expression[i] == '(':
			parentheses = 1
			j = i + 1
			while parentheses > 0:
				if expression[j] == '(':
					parentheses = parentheses + 1
				elif expression[j] == ')':
					parentheses = parentheses - 1
				j = j + 1

			value = operator(value,evaluate_expression(expression[i + 1:j - 1], part2))
			i = j

		elif expression[i] == '+':
			i += 1
			operator = add
		elif expression[i] == '*':
			if part2:
				r = evaluate_expression(expression[i+1:], part2)
				value *= r
				i = len(expression)
			else:
				i += 1
				operator = mult
		elif expression[i] == ' ':
			i += 1
		else:
			j = i + 1
			while j < len(expression) and expression[j].isdigit():
				j += 1
				
			value = operator(value, int(expression[i:j]))
			i = j

	return value

@problem.solver()
def solver(ls):
	p1 = p2 = 0
	for l in ls:
		l = l.replace(" ", "")
		p1 += evaluate_expression(l)
		p2 += evaluate_expression(l, part2=True)
	return p1, p2
	
if __name__ == "__main__":
	problem.solve()