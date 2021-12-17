import sys, re, os
from datetime import date

def daily_update():
    today = date.today()
    d, m, y = today.strftime("%d/%m/%Y").split("/")

    if m == "12":
        with open("README.md") as f:
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

        with open("README.md", "w") as f:
            for line in lines:
                f.write(line)

def commit_update(commit_message):
    match = re.match(r"^(\d+)-Day-(\d+)$", commit_message)
    if match == None: return

    numbers = [x for x in match.groups()]

    previous_stdout = sys.stdout
    with open("res.txt", "w") as out:
        sys.stdout = out
        with open(f"events/{numbers[0]}/day{int(numbers[1]):02d}.py") as f:
            exec(f.read())
        sys.stdout = previous_stdout

    with open("res.txt") as f:
        text = f.read()
        results = re.findall(r"(\d+\.\d+.?s)", text)
        for id, v in enumerate(results):
            if v[-2:] == "us":
                results[id] = "0.000"
            elif v[-2:] == "ms":
                results[id] = f"{float(v[:-2])/1000:.3f}"
            else:
                results[id] = f"{float(v[:-1]):.3f}"

    os.remove("res.txt")

    with open("README.md") as f:
        lines = f.readlines()

        line_id = 0
        for id, line in enumerate(lines):
            if numbers[0] in line:
                line_id = id
                break

        splt = line.split("%2F")
        splt[0] = splt[0][:-2] + f"{int(numbers[1]):02d}"

        if splt[0][-2:] == splt[1][:2]:
            splt[1] = splt[1].replace("red", "green")

        lines[line_id] = '%2F'.join(splt)

        found = False
        for id, line in enumerate(lines):
            if f"## {numbers[0]}" in line:
                found = True
            
            if line.strip() == "" and found:
                if len(results) == 1:
                    lines.insert(id, f'| {numbers[1]} | [Solution](https://github.com/andrefpoliveira/AdventOfCode/blob/main/events/{numbers[0]}/day{f"{int(numbers[1]):02d}"}.py) | - | - | {results[0]} |\n')
                else:
                    lines.insert(id, f'| {numbers[1]} | [Solution](https://github.com/andrefpoliveira/AdventOfCode/blob/main/events/{numbers[0]}/day{f"{int(numbers[1]):02d}"}.py) | {results[0]} | {results[1]} | {results[2]} |\n')
                break

    with open("README.md", "w") as f:
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
