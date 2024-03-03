#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_times = t1.split()
    t2_times = t2.split()
    
    # # Parse the timestamps into datetime objects
    # t1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S")
    # t2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S")
    # duration = abs(t1 - t2)                         # For build-in functions
    # duration_in_s = duration.total_seconds()
    
    timezone = str(abs(int(t2_times[-1]) - int(t1_times[-1])) * 36)

    return str(timezone)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
