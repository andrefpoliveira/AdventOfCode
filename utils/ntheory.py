import math

def _gcd(a, b):
    """Finds the Greatest Common Divisor of two integers a and b"""
    return math.gcd(a, b)

def _lcm(a, b):
    """Finds the Lowest Common Multiple of two integers a and b"""
    return math.lcm(a, b)

def gcd(ns):
    """Finds the Greatest Common Divisor of a list of integers ns"""
    while len(ns) > 1:
        a, b = ns.pop(), ns.pop()
        while b:
            a, b = b, a%b
        ns.append(a)
    return ns[0]

def lcm(ns):
    """Finds the Lowest Common Mulitple of a list of integers ns"""
    while len(ns) > 1:
        a, b = ns.pop(), ns.pop()
        ns.append(_lcm(a, b))
    return ns[0]

def triangular_number(n):
    return (n * (n + 1)) // 2

#####

def is_square(n):
    return int(math.sqrt(n) ** 2) == n

def is_prime(n):
    return n not in [0,1] and all(n % i > 0 for i in range(2, n-1))