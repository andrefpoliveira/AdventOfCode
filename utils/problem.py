import os
import re
import time
from aocd.models import Puzzle

class Problem:
    """ class Problem

    Represents and provides methods relating to a single Advent of Code
    problem.
    """

    def __init__(self, *args, **kwargs):
        """ __init__()

        Pass the year, month, and problem name to the constructor to
        instantiate a new Problem.

            Problem("2015/01: Not Quite Lisp")
            Problem(year=2015, day=1, name="Not Quite Lisp")
        """

        match = re.fullmatch(
            re.compile(
                r"(?P<year>[0-9]{4})\/"
                + r"(?P<day>0?[1-9]|1[0-9]|2[0-5])\: "
                + r"(?P<name>.+)"
            ),
            "".join(args),
        )

        if (match):
            self.year = int(match.group("year"))
            self.day = int(match.group("day"))
            self.name = str(match.group("name"))
        elif all(field in kwargs.keys() for field in ["year", "day", "name"]):
            self.year = int(kwargs.get("year", 0))
            self.day = int(kwargs.get("day", 0))
            self.name = str(kwargs.get("name", "???"))
        else:
            raise ValueError(
                "Could not parse arguments to Problem constructor."
            )

        # The solver functions, and the input preprocessor, are stored as class
        # fields.
        self.fns = {}
        self.preprocessor = lambda x: x

        # All tests are user-defined.
        self.tests = {}
        self.total_time = 0

    def solver(self, part="both"):
        """ solver()

        A decorator for a function to mark it as a solver function to run.
        Optionally specify the part being solved using the `part` keyword
        argument.
        """

        def register(fn):
            # Register the solver function in the instance dictionary variable
            # `self.fns`.
            self.fns[part] = fn
            return fn

        return register

    def solve(self):
        """ solve()

        Run the solver functions and pretty-print the output.
        """

        print("--- Day {}: {} ---".format(self.day, self.name))

        # Setup the path to the local cache.
        fp = "./events/{:04}/inputs/day{:02}.txt".format(self.year, self.day)

        if os.path.exists(fp):
            # Read input from cache.
            with open(fp, "r") as fh:
                inp_s = fh.read()
        else:
            inp_s = Puzzle(year=int(self.year), day=int(self.day)).input_data

        # Run each solver.
        for part, fn in self.fns.items():
            # Apply the preprocessor.
            inp = self.preprocessor(inp_s)

            # Run the solver on the input and time the runtime.
            start = time.perf_counter()
            out = fn(inp)
            stop = time.perf_counter()

            self.total_time += (stop - start)

            # Compute runtime and appropriate time unit.
            delta, unit = (stop - start), 0
            while delta < 1 and unit <= 3:
                delta, unit = 1000 * delta, unit + 1
            delta, unit = round(delta, 5), ["s", "ms", "us", "ns"][unit]

            # Print answers
            if (part in ["both"]) and (type(out) is tuple) and (len(out) >= 2):
                print("Part 1: {}".format(out[0]))
                print("Part 2: {} (runtime: {}{})".format(
                    out[1], delta, unit
                ))
            else:
                print("Part {}: {} (runtime: {}{})".format(
                    part, out, delta, unit
                ))

        if len(self.fns.items()) > 1:
            delta, unit = self.total_time, 0
            while delta < 1 and unit <= 3:
                delta, unit = 1000 * delta, unit + 1
            delta, unit = round(delta, 5), ["s", "ms", "us", "ns"][unit]

            print("Total time: {}{}".format(delta, unit))
