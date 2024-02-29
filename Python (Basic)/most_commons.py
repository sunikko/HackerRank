#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    # count the occurrence count
    # a dict to add chr:num for in s
    chr_dict = {}
    for chr in s:
        chr_dict[chr] = chr_dict[chr] + 1 if chr in chr_dict.keys() else 1
        # chr_dict[i] = chr_dict.get(i, 0) + 1
        
    # order by the occurence count
    # if it's same, sort them in alphabetical order
    # Python can sort by two things by returning a tuple for the key in the sorted method
    #  the negative sign is required on the numeric type to reverse its sorted order.
    # chr_dict = sorted(chr_dict.items(), key=lambda item: (item[-1], item[0])) ?? 
    # == 1 ==
    # chr_list = sorted(chr_dict.items(), key=lambda item: item[0])
    # chr_list = sorted(chr_list, key=lambda item: item[1], reverse=True)
    # == 2 ==
    chr_list = sorted(chr_dict.items(), key=lambda item: (-item[1], item[0]))

    # == 1 ==
    # for item in chr_list[:3]:
    #     print("{} {}".format(item[0], item[1]))
    # == 2 ==
    # for chr, count in chr_list[:3]:
    #         print(chr, count)
    # == 3 ==
    # * symbol is used to print the list elements in a single line with space
    for i in chr_list[:3]:
        print(*i)

    
    
