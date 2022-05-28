import math
from math import *

from typing import List


def sequentialDigits(low: int, high: int) -> List[int]:

    # The integer part of log base 10 gives the number of digits of the number
    mn = int(math.log10(low))+1
    mx = int(math.log10(high))+1
    seq_digits = []
    for i in range(mn, mx+1):
        for j in range(1, 10-i+1):
            nb = 0
            dec = 10**(i-1)
            digit = j
            while dec > 0:
                nb += digit * dec
                dec = dec // 10
                digit += 1
            if  low<=nb<=high:
                seq_digits.append(nb)
    return seq_digits

low = 200
high = 2000000

print(sequentialDigits(low, high))