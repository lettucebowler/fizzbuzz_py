#!/usr/bin/env python3
from math import gcd

# Global behavior variables
MOD = True
LESS = False


# Add entries here to check more numbers
mod_dict = {3: 'Fizz', 5: 'Buzz'}
less_dict = {10: 'Bazz'}
range_list = []

# Calculate lcm of numbers to check. Used to determine length of pattern.
if MOD and len(mod_dict) > 0:
    keys = list(mod_dict.keys())
    lcm = keys[0]
    for i in keys[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    range_list.append(lcm)

#find largest value checked for less_dict
if LESS and len(less_dict) > 0:
    range_list.append(max(list(less_dict.keys())))

# Determine largest checked value and set range of iteration to it.
if len(range_list) > 0:
    final_num = max(range_list)
else:
    print("No Functions Enabled.")
    exit()

for n in range(1, final_num + 1):
    output = []
    if MOD:
        output.extend([mod_dict[word] for word in mod_dict if n % word == 0])
    if LESS:
        output.extend([less_dict[less] for less in less_dict if n < less])
    print("".join(output) if len(output) > 0 else n)