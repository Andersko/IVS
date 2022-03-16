"""!
Module for standard deviation calculation

Script implements one function for standard deviation calculated from list of numbers.

Can be imported as module, or run as main script. If run as a script, calculates standard deviation of numbers from
standard input and prints result to standard output. Numbers are separated by whitespace characters. Amount of numbers
is 2 - 1000.

usage: profiling.py [-h] [INPUT_FILE]

@file profiling.py
@author Andrej Pavlovič
@date 16.3.2022
"""

# Internal program imports
import my_math as mm

# Python built-in libraries import
import sys

# Python external libraries import
import argparse


def std_dev(numbers: 'list of floats') -> float:
    """!
    Calculate standard deviation

    @param numbers list of numbers to calculate
    @return standard deviation
    @exception IndexError if numbers length < 2
    """
    if len(numbers) < 2:
        raise IndexError

    n = len(numbers)
    mean = mm.multiply(mm.divide(1, n), mm.sum(numbers))
    return mm.root(mm.multiply(mm.divide(1, mm.subtract(n, 1)), mm.subtract(mm.sum([mm.power(x, 2) for x in numbers]),
                                                                            mm.multiply(n, mm.power(mean, 2)))), 2)


if __name__ == '__main__':
    # Parse args
    parser = argparse.ArgumentParser(description='''Calculate standard deviation from stdin to stdout.
Input contains numbers separated by whitespace characters.''')
    parser.parse_args()

    numbers = []

    try:
        for line in sys.stdin:
            for word in line.split():
                numbers.append(float(word))
    except ValueError:
        exit('Invalid input.')

    try:
        print(std_dev(numbers))
    except IndexError:
        exit('Not enough numbers.')
