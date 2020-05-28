#!/usr/bin/env python3
from math import gcd

# n: number to check
# states: dictionary of form number:word containing numbers to check against n
# output: list of conditions met, or [n] if none
def fizzbuzz(n, states):
    output = [str(n)]
    output.extend([condition(n) for condition in states if condition(n) != None])
    if len(output) > 1:
        output = output[1:]
    return output

# List of lambda functions to test conditions
triggers = [lambda x: 'Fizz' if x % 3 == 0 else None,
            lambda x: 'Buzz' if x % 5 == 0 else None,
            lambda x: 'Bazz' if x < 10 else None]

for n in range(1, 100 + 1):
    print(''.join(fizzbuzz(n, triggers)))