#!/usr/bin/env python3
from math import gcd

# Add entries here to check more numbers
words = {3: 'fizz', 5: 'buzz'}

# Calculate lcm of numbers to check. Used to determine length of pattern.
keys = list(words.keys())
lcm = keys[0]
for i in keys[1:]:
    lcm = int(lcm*i/gcd(lcm, i))

for n in range(1, lcm + 1):
    output = [words[word] for word in words if n % word == 0]
    print("".join(output) if len(output) > 0 else n)