#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:44:31 2019

@author: joscelynec
"""

def Dutch_Flag(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
       
   Adapted from https://en.wikipedia.org/wiki/Dutch_national_flag_problem 

    """
#Null input
    if input_list == None:
        return None
#Empty List input
    if input_list == []:
        return []
    i = 0
    j = 0
    mid = 1
    n = len(input_list) - 1
    while j <= n:
        if input_list[j] < mid:
            #swap 
            temp = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = temp
            i = i + 1
            j = j + 1
        elif input_list[j] > mid:
            #swap
            temp = input_list[j]
            input_list[j] = input_list[n]
            input_list[n] = temp
            n = n - 1
        else:
            j = j + 1
    return input_list
    
    
def test_function(test_case):
    
    sorted_array = Dutch_Flag(test_case)
    if sorted_array == None:
        print(sorted_array)
        print("Pass")
        return
    if sorted_array == []:
        print(sorted_array)
        print("Pass")
        return
    
    if sorted_array == sorted(test_case):
        print(sorted_array)
        print("Pass")
    else:
        print("Fail")
#*******  Test Code ******************8

#None Input 
test_function(None)  

#Empty Input     
test_function([])       

#Singelton Lists
test_function([0])  
test_function([1]) 
test_function([2]) 

#Lists with 2 elements
test_function([1,0])  
test_function([2,1]) 
test_function([2,0])
test_function([0,0])  
test_function([1,1]) 
test_function([2,2])


#Longer length lists 
test_function([2,1,0])
test_function([2,2,0,0,1,1,1,0,0])
test_function([2,2,2,2,2,2,2,2,0])  
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2])

"""
None
Pass
[]
Pass
[0]
Pass
[1]
Pass
[2]
Pass
[0, 1]
Pass
[1, 2]
Pass
[0, 2]
Pass
[0, 0]
Pass
[1, 1]
Pass
[2, 2]
Pass
[0, 1, 2]
Pass
[0, 0, 0, 0, 1, 1, 1, 2, 2]
Pass
[0, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2]
Pass
"""





