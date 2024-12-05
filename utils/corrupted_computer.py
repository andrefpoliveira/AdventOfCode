from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
import re

# INSTRUCTIONS
class Instruction(ABC):
    def __init__(self, _):
        pass

    @staticmethod
    @abstractmethod
    def get_pattern(self):
        pass

    @abstractmethod
    def apply_effect(self, computer: CorruptedComputer):
        pass


class Multiply(Instruction):
    def __init__(self, args):
        self.arg1 = int(args[0])
        self.arg2 = int(args[1])

    @staticmethod
    def get_pattern():
        return r"mul\((\d{1,3}),(\d{1,3})\)"

    def apply_effect(self, computer: CorruptedComputer):
        if computer.enabled:
            computer.value += self.arg1 * self.arg2


class Do(Instruction):
    @staticmethod
    def get_pattern():
        return r"do\(\)"
    
    def apply_effect(self, computer: CorruptedComputer):
        computer.enabled = True


class Dont(Instruction):
    @staticmethod
    def get_pattern():
        return r"don't\(\)"
    
    def apply_effect(self, computer: CorruptedComputer):
        computer.enabled = False


class InstructionsList(Enum):
    MULTIPLY = Multiply
    DO = Do
    DONT = Dont


# PROGRAM
class CorruptedComputer:
    def __init__(self, program, instruction_types = []):
        self.program = program

        self.enabled = True
        self.value = 0
        self.instruction_types = instruction_types if instruction_types else InstructionsList

    def find_instructions(self, program_line: str):
        instructions = []

        for inst in self.instruction_types:
            pattern = inst.value.get_pattern()

            it = re.finditer(pattern, program_line)
            for i in it:
                arguments = re.search(pattern, program_line[i.start():i.end()]).groups()

                instructions.append((i.start(), inst.value(arguments)))

        return [x[1] for x in sorted(instructions, key=lambda x: x[0])]

    def run(self):
        for l in self.program:
            instructions = self.find_instructions(l)
            for i in instructions:
                i.apply_effect(self)
        return self.value