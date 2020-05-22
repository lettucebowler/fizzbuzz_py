#!/usr/bin/env python3
from math import gcd

# Add entries here to check more numbers
mod_dict = {3: 'Fizz', 5: 'Buzz'}
less_dict = {10: 'Bazz'}

# Calculate lcm of numbers to check. Used to determine length of pattern.
keys = list(words.keys())
lcm = keys[0]
for i in keys[1:]:
    lcm = int(lcm*i/gcd(lcm, i))

for n in range(1, lcm + 1):
    output = []
    output.extend([less_dict[less] for less in less_dict if n < less])
    output.extend([mod_dict[word] for word in mod_dict if n % word == 0])
    print("".join(output) if len(output) > 0 else n)