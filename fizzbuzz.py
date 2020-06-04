#!/usr/bin/env python3
from math import gcd

# n: number to check
# states: dictionary of form number:word containing numbers to check against n
# output: list of conditions met, or [n] if none
def fizzbuzz(n, states):
    output = [str(n)]
    output.extend([text for text, condition in states if condition(n)])
    if len(output) > 1:
        output = output[1:]
    return output

# Array of outputs and their associated conditions
triggers = [['Fizz', lambda x: x % 3 == 0],
            ['Buzz', lambda x: x % 5 == 0]]

# Driver program
for n in range(1, 100 + 1):
    output_buffer = ['{}: '.format(n)]
    output_buffer.extend(fizzbuzz(n, triggers))
    print(''.join(output_buffer))