#!/usr/bin/env python3
from math import gcd

words = {3: 'fizz', 5: 'buzz'}

for n in range(1, 100):
    output = ""
    for word in words:
        if n % word == 0:
            output += words[word]
    if output == "":
        print(str(n))
    else:
        print(str(output))