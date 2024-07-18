import sys, re, os, json
from datetime import date

def load_results() -> dict:
	if os.path.exists("results.json"):
		with open("results.json") as f:
			return json.load(f)
	return {}


def save_results(results: dict):
	with open("results.json", "w") as f:
		json.dump(results, f, indent=2)


def commit_update(commit_message) -> list:
	match = re.match(r"^(\d{2})-(\d{4})$", commit_message)
	if match is None:
		return None

	day, year = [x for x in match.groups()]

	#Run the AoC day code
	previous_stdout = sys.stdout
	with open("res.txt", "w") as out:
		sys.stdout = out
		with open(f"events/{year}/day{int(day):02d}.py") as f:
			exec(f.read(), globals(), globals())
	sys.stdout = previous_stdout

    # Get the final results from the code
	with open("res.txt") as f:
		text = f.read()
		results = re.findall(r"(\d+\.\d+.?s)", text)
		for id, v in enumerate(results):
			if v[-2:] in ["us", "ns"]:
				results[id] = "0.000"
			elif v[-2:] == "ms":
				results[id] = f"{float(v[:-2])/1000:.3f}"
			else:
				results[id] = f"{float(v[:-1]):.3f}"

	return results


def build_report(results):
	with open("README.md", "w", encoding="utf-8") as f:
		f.write('# Advent Of Code\n')
		f.write('<p align="center">\n')
		for year in range(2015, date.today().year + (1 if date.today().month == 12 else 0)):

			days = 25 if year != date.today().year else date.today().day
			solved_days = len(results.get(str(year), []))
			status = "green" if solved_days == days else "red"

			f.write(f'''<a href="https://github.com/andrefpoliveira/AdventOfCode#{year}" alt="Year{year}">
				<img src="https://img.shields.io/badge/{year}-{solved_days:02d}%2F{days}-{status}" />
			</a>\n'''
			)

		f.write('</p>\n')

		f.write('My solutions for the Advent Of Code 🎅🏻🎄⛄\n\n')
		f.write('Some of these solutions need some optimization tho 😄\n\n')

		for year in range(2015, date.today().year + (1 if date.today().month == 12 else 0)):
			f.write(f'## {year}\n')
			f.write('| Day | Link | Part 1 Solve Time (s) | Part 2 Solve Time (s) | Total Solve Time (s) |\n')
			f.write('|:---:|:----:|:---------------------:|:---------------------:|:--------------------:|\n')

			for day in sorted(int(x) for x in results.get(str(year), [])):
				res = results[str(year)][f"{day:02d}"]
				if len(res) == 1:
					res = ["-", "-"] + res
				f.write(f'| {day} | [Solution](https://github.com/andrefpoliveira/AdventOfCode/blob/main/events/{year}/day{day:02d}.py) | {res[0]} | {res[1]} | {res[2]} |\n')

if __name__ == "__main__":
	results = load_results()

	task = sys.argv[1]

	if task == "daily":
		print("Daily update!")
		build_report(results)
		
	elif task == "commit":
		commit_message = sys.argv[2]
		print(f"Commit {commit_message}")
		res = commit_update(commit_message)

		if res is None:
			print("Not a day commit :) nothing to do")
			exit(0)

		day, year = commit_message.split("-")
		year_results = results.get(year, {})
		year_results[day] = res
		results[year] = year_results

		save_results(results)
		build_report(results)
