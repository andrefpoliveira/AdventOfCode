def I(s):
    return s.strip()
def intI(s):
    return int(s.strip())

#
# Input Parsing - Space/Comma/Line separared values/integers
#

def ssv(s):
    return [v.strip() for v in s.strip().split(" ")]
def ssi(s):
    return [int(v.strip()) for v in s.strip().split(" ")]

def csv(s):
    return [v.strip() for v in s.strip().split(",")]
def csi(s):
    return [int(v.strip()) for v in s.strip().split(",")]

def lsv(s):
    return [v.strip() for v in s.strip().split("\n")]
def lsi(s):
    return [int(v.strip()) for v in s.strip().split("\n")]

#
# Grid
#
def grid(s):
    return [list(l) for l in s.strip().split("\n")]

def int_grid(s):
    return [[int(i) for i in row.split()] for row in s.strip().split("\n")]

#
# Character / Digits string
#
def chars(s):
    return list(s.strip())
def digits(s):
    return [int(d) for d in list(s.strip())]