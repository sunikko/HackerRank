#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = s.split()
    return_str = ""
    for name in names:
        return_str = (return_str + " ") if return_str != "" else return_str
        cap_name = name[0].upper() + name[1:]
        return_str += cap_name
    return return_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
