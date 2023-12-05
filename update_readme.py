import sys, re, os
from datetime import date

def daily_update():
    today = date.today()
    d, m, y = today.strftime("%d/%m/%Y").split("/")

    if int(d) > 25: return

    if m == "12":
        with open("README.md", encoding="utf-8") as f:
            lines = f.readlines()
            end_of_p = 0
            for id, line in enumerate(lines):
                if line == "</p>\n":
                    end_of_p = id
                    break

            if y in lines[end_of_p-1]:
                current_line = lines[end_of_p-1]
                splt = current_line.split("%2F")
                splt[1] = f"{int(d):02d}" + splt[1][2:].replace("green","red")
                lines[end_of_p-1] = '%2F'.join(splt)
            else:
                lines.insert(end_of_p, f'    <a href="https://github.com/andrefpoliveira/AdventOfCode#{y}" alt="Year{y}"><img src="https://img.shields.io/badge/{y}-00%2F01-red" /></a>\n')

        if int(d) == 1:
            lines.append(f"# {y}\n")
            lines.append("| Day | Link | Part 1 Solve Time (s) | Part 2 Solve Time (s) | Total Solve Time (s) |\n")
            lines.append("|:---:|:----:|:---------------------:|:---------------------:|:--------------------:|\n")

        with open("README.md", "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line)

def get_badge_line(year, lines):
    for id, line in enumerate(lines):
        if year in line:
            return id, line
    return len(lines), ""

def get_year_line(year, lines):
    for id, line in enumerate(lines):
        if f"## {year}" in line:
            return id
    return None

def get_day_line(day, lines, starting_line):
    for id, line in enumerate(lines[starting_line:]):

        numbers = re.findall(r"\d+", line)

        if line.strip() == "": return id + starting_line
        if not numbers: continue

        if int(numbers[0]) == day - 1: return id + 1 + starting_line
        if int(numbers[0]) > day: return id + starting_line
    return len(lines)

def commit_update(commit_message):
    match = re.match(r"^(\d+)-Day-(\d+)$", commit_message)
    if match is None: return

    year, day = [x for x in match.groups()]

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

    os.remove("res.txt")

    with open("README.md", encoding="utf-8") as f:
        lines = f.readlines()

        badge_line, line = get_badge_line(year, lines)

        splt = line.split("%2F")
        # f"{int(d):02d}"
        splt[0] = splt[0][:-2] + f"{int(splt[0][-2:]) + 1:02d}" # Increment the day

        # If we have 25 days, we can change the badge color
        if splt[0][-2:] == splt[1][:2]:
            splt[1] = splt[1].replace("red", "green")

        lines[badge_line] = '%2F'.join(splt)

        year_line = get_year_line(year, lines) or len(lines)
        day_line = get_day_line(int(day), lines, year_line+2)

        if len(results) == 1:
            line = f'| {day} | [Solution](https://github.com/andrefpoliveira/AdventOfCode/blob/main/events/{year}/day{f"{int(day):02d}"}.py) | - | - | {results[0]} |\n'
        else:
            line = f'| {day} | [Solution](https://github.com/andrefpoliveira/AdventOfCode/blob/main/events/{year}/day{f"{int(day):02d}"}.py) | {results[0]} | {results[1]} | {results[2]} |\n'
        
        lines.insert(day_line, line)

    with open("README.md", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    task = sys.argv[1]
    if task == "daily":
        print("Daily update!")
        daily_update()
    elif task == "commit":
        commit_message = sys.argv[2]
        print(f"Commit {commit_message}")
        commit_update(commit_message)
