"""!
Math module for calculator

@file math.py
@author Filip Solich
@author Andrej Pavlovič
@author Adam Kostolányi
@date 16.3.2022
"""


import math


def _is_number(x):
    """!
    Check if x is number

    @param x number to check
    @return True if x is number
    """

    if type(x) is int or type(x) is float:
        return True

    return False


def _is_int(x):
    """!
    Check if x is integer even if x is float (5 -> True, 5.0 -> True, 5.1 -> False)

    @param x number to integer check
    @return True if x is integer
    """

    return isinstance(x, int) or (isinstance(x, float) and x.is_integer())


def add(a, b):
    """!
    Addition of two numbers
    
    @param a addend
    @param b addend
    @return sum of a and b
    @exception TypeError if a or b is not a number
    """

    if not _is_number(a) or not _is_number(b):
        raise TypeError

    return a + b


def subtract(a, b):
    """!
    Subtraction of two numbers
    
    @param a minuend
    @param b subtrahend
    @return difference of a and b
    @exception TypeError if a or b is not a number
    """

    if not _is_number(a) or not _is_number(b):
        raise TypeError

    return a - b


def multiply(a, b):
    """!
    Multiplication of two numbers
    
    @param a multiplier
    @param b multiplicand
    @return product of a and b
    @exception TypeError if a or b is not a number
    """

    if not _is_number(a) or not _is_number(b):
        raise TypeError

    return a * b


def divide(a, b):
    """!
    Division of two numbers

    Note that function does not take care of zero division.
    
    @param a dividend
    @param b divisor
    @return quotient of a and b
    @exception TypeError if a or b is not a number
    """

    if not _is_number(a) or not _is_number(b):
        raise TypeError

    result = a / float(b)

    if int(result) == result:
        return int(result)

    return result


def power(x, n):
    """!
    Calculate x^n

    @param x base value
    @param n exponent
    @return x raised to the power n
    @exception TypeError if `x` or `n` isnt't number
    @exception ValueError if exponent isn't natural number
    """

    if not _is_number(x) or not _is_number(n):
        raise TypeError('`x` or `n` isn\'t number')

    if not _is_int(n) or n < 0.0:
        raise ValueError('Exponent isn\'t natural number')

    return x ** n


def root(x, n):
    """!
    Calculate nth root of `x`

    @param x positive number
    @param n number n in nth root
    @return x**(1/n)
    @exception TypeError if `x` or `n` isnt't number
    @exception ValueError if `n` isn't integer
    @exception ValueError if `n` is zero 
    @exception ValueError if `x` is negative number
    """

    if not _is_number(x) or not _is_number(n):
        raise TypeError('`x` or `n` isn\'t number')

    if not _is_int(n):
        raise ValueError('`n` isn\'t integer')

    if x < 0:
        raise ValueError('`x` is negative number')

    if n == 0:
        raise ValueError('`n` can\'t be 0')

    return x**(1/n)


def factorial(x):
    """!
    Calculate `x` factorial

    @param x value for factorial calculation
    @return x factorial
    @exception TypeError if `x` isn't number
    @exception ValusError if `x` isn't integer or `x` is negative number
    """

    if not _is_number(x):
        raise TypeError('`x` isn\'t number')

    if not _is_int(x):
        raise ValueError('`x` isn\'t integer')

    return math.factorial(int(x))


def modulo(x, n):
    """!
    Calculate modulo from `x` and `n`

    @param x divident
    @param n divisor
    @return x % n
    @exception TypeError if `x` or `n` isnt't number
    @exception ValueError if `x` or `n` isnt't integer
    """

    if not _is_number(x) or not _is_number(n):
        raise TypeError('`x` or `n` isn\'t number')

    if not _is_int(x) or not _is_int(n):
        raise ValueError('`x` or `n` isn\'t integer')

    return int(x) % int(n)


def sum(li: list):
    """!
    Sum up list

    @param li list with numbers
    @return sum
    """

    sum = 0

    for number in li:
        sum = add(sum, number)

    return sum
