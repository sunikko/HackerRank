#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    need_to_be_cap = True
    return_str = ""
    for chr in s:
        if need_to_be_cap and chr != " ":
            return_str += chr.upper()
            need_to_be_cap = False
        else:
            return_str += chr
            if chr == " ":
                need_to_be_cap = True
    return return_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
