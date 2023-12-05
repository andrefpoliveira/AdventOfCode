class Intcode:
  def __init__(self, program):
    self.program = program
    self.id = 0

  def replace_noun_verb(self, noun, verb):
    self.program[1] = noun
    self.program[2] = verb

  def get_pos(self, prog, id):
    return prog[id]

  def get_value(self, prog, id):
    return prog[self.get_pos(prog, id)]

  def run(self):
    prog = [x for x in self.program]
    id = 0
    while id < len(prog):
      
      opcode = prog[id]

      if opcode == 99:
        return self.get_pos(prog, 0)
      else:
        opcode_func = getattr(self, f"opcode_{opcode}")
        prog, id = opcode_func(prog, id)

  ########################################
  # OPCODES
  ########################################
  def opcode_1(self, prog, id):
    res = self.get_value(prog, id+1) + self.get_value(prog, id+2)
    prog[self.get_pos(prog, id+3)] = res
    return prog, id + 4

  def opcode_2(self, prog, id):
    res = self.get_value(prog, id+1) * self.get_value(prog, id+2)
    prog[self.get_pos(prog, id+3)] = res
    return prog, id + 4