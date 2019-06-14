#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:31:24 2019

@author: joscelynec
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or len(ints) == 0:
        return None
    if len(ints) == 1:
        return (ints[0],ints[0])
    
    max = ints[0]
    min = ints[0]
    for i in range(1, len(ints)):
        if ints[i] > max:
            max = ints[i]
        if ints[i] < min:
            min = ints[i]
    return (min,max)
            


"""
Tests below
"""
import random
"""
Null Input
"""
l = None
print ("Pass" if (None == get_min_max(l)) else "Fail")

"""
 empty list
"""
l = [i for i in range(0, 0)] 
random.shuffle(l)
print ("Pass" if (None == get_min_max(l)) else "Fail")

"""
Udacity Example Test Case of Ten Integers
"""
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


"""
Example Test Case of 100,000 Integers
"""
l = [i for i in range(0, 100000)]  # a list containing 0 - 99999
random.shuffle(l)

print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")


"""
Example Test Case of 1,000,000 Integers
"""
l = [i for i in range(0, 1000000)]  # a list containing 0 - 999999
random.shuffle(l)

print ("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")

"""
Pass
Pass
Pass
Pass
Pass
"""