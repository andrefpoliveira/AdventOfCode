import sys
sys.path.append("year2015")
import year2015.run_all

with open("README.md", "w") as f:
    f.write("# AdventOfCode\n")
    f.write("My solutions for the Advent Of Code\n\n")

    f.write("## 2015\n")
    f.write("| Day | Link | Part 1 Solve Time (s) | Part 2 Solve Time (s) | Total Solve Time (s) |\n")
    f.write("|:---:|:----:|:---------------------:|:---------------------:|:--------------------:|\n")

    for day, res in enumerate(year2015.run_all.run_all()):
        day += 1
        first_value = "{:.3f}".format(res[0]) if res[0] != "-" else res[0]
        second_value = "{:.3f}".format(res[1]) if res[1] != "-" else res[1]
        third_value = "{:.3f}".format(res[2]) if res[2] != "-" else res[2]
        f.write(f"| {day} | [Solution](https://github.com/andrefpoliveira/AdventOfCode/blob/main/2015/day{day}.py) | {first_value} | {second_value} | {third_value} |\n")