import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10
import day11, day12, day13, day14, day15, day16, day17, day18, day19
import day20, day21

def run_all():
    for day in range(1, 22):
        day = globals()[f"day{day}"]
        run = getattr(day, "run")
        yield run()