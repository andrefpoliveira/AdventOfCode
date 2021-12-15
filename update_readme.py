from datetime import date

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
            splt[1] = f"{int(d):02d}" + splt[1][2:]
            lines[end_of_p-1] = '%2F'.join(splt)
        else:
            lines.insert(end_of_p, f'    <a href="https://github.com/andrefpoliveira/AdventOfCode#{y}" alt="Year{y}"><img src="https://img.shields.io/badge/{y}-00%2F01-red" /></a>\n')

    with open("README.md", "w") as f:
        for line in lines:
            f.write(line)

        