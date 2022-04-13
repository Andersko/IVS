"""!
Script to generate random input numbers for testing (profiling) of profiler.py.

Creates (overrides) 3 new files in current directory - test_{10|100|1000}.txt

@file profiling_test_generator.py
@author Andrej Pavlovič
@date 29.3.2022
"""

import random

with open('../profiling/test_10.txt', 'w', newline='\n') as f:
    for i in range(-2, 3):
        print(random.randint(-10, 10) * i, file=f)

    for i in range(-2, 3):
        print(random.randint(-10, 10) * i * random.random(), file=f)

with open('../profiling/test_100.txt', 'w', newline='\n') as f:
    for i in range(-17, 43):
        print(random.randint(-3, 1) * i, file=f)

    for i in range(-12, 28):
        print(random.randint(-1, 2) * i * random.random(), file=f)

with open('../profiling/test_1000.txt', 'w', newline='\n') as f:
    for i in range(333):
        print(random.randint(-10, 15) * random.random(), file=f)

    for i in range(333):
        print(random.randint(-3, 1) * 8.5, file=f)

    for i in range(334):
        print(random.randint(-8, 85), file=f)
