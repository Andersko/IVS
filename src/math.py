"""Math module for calculator

@file math.py
@author Filip Solich
@date 4.3.2022
"""

import math


def _is_int(x):
    """Check if x is integer even if x is float (5 -> True, 5.0 -> True, 5.1 -> False)

    @param x number to integer check
    @return True if x is integer
    """

    return isinstance(x, int) or (isinstance(x, float) and x.is_integer())


def power(x, n):
    """Calculate x^n

    @param x base value
    @param n exponent
    @return x raised to the power n
    @exception ValueError if exponent isn't natural number
    """

    if not _is_int(n) or n < 0.0:
        raise ValueError('Exponent isn\'t natural number')

    return x**n


def root(x, n):
    """Calculate nth root of x

    @param x positive number
    @param n number n in nth root
    @return x**(1/n)
    @exeption ValueError if n isn't integer
    @exeption ValueError if x is negative number
    """

    if not _is_int(n):
        raise ValueError('n isn\'t integer')

    if x < 0:
        raise ValueError('x is negative number')

    return x**(1/n)


def factorial(x):
    """Calculate x factorial

    @param x value for factorial calculation
    @return x factorial
    @exeption ValuesError if x isn't integer or x is negative number
    """

    if not _is_int(x):
        raise ValueError('x isn\'t integer')

    return math.factorial(int(x))


def modulo(x, n):
    """Calculate modulo from x and n

    @param x divident
    @param n divisor
    @return x % n
    @exeption ValueError if x or n isnt't integer
    """

    if not _is_int(x) or not _is_int(n):
        raise ValueError('x or n isn\'t integer')

    return int(x) % int(n)
