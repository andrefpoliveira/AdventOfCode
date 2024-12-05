from utils import problem
from utils import preprocessing as ppr

problem = problem.Problem("2024/02: Red-Nosed Reports")
problem.preprocessor = ppr.int_grid


def is_valid(report):
    if report not in (sorted(report), sorted(report, reverse=True)):
        return False

    return all(1 <= abs(report[i] - report[i-1]) <= 3 for i in range(1, len(report)))

def is_report_safe(report, part2 = False):
    if is_valid(report):
        return True
    
    if part2:
        for i in range(len(report)):
            temp_report = report[:i] + report[i+1:]
            if is_valid(temp_report):
                return True
    
    return False


@problem.solver(part=1)
def part1(grid):
    return sum(is_report_safe(report) for report in grid)


@problem.solver(part=2)
def part2(grid):
    return sum(is_report_safe(report, part2=True) for report in grid)


if __name__ == "__main__":
    problem.solve()