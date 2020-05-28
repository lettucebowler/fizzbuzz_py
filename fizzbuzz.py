#!/usr/bin/env python3
from math import gcd

# n: number to check
# states: dictionary of form number:word containing numbers to check against n
# output: list of conditions met, or [n] if none
def fizzbuzz(n, states):
    output = [str(n)]
    output.extend([text for divisor, text in states if n % divisor == 0])

    if len(output) > 1:
        output = output[1:]
    return output

# Add entries here to check more numbers
# conditions = {3: 'Fizz', 5: 'Buzz'}
conditions = [(3, 'Fizz'), (5, 'Buzz')]

# Calculate lcm of numbers to check. Used to determine length of pattern.
if len(conditions) > 0:
    divisors = [divisor for divisor, text in conditions]
    lcm = divisors[0]
    for i in divisors[1:]:
        lcm = int(lcm*i/gcd(lcm, i))

# Run program until all possible conditions have been met
for n in range(1, lcm + 1):
    print(''.join(fizzbuzz(n, conditions)))