#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:01:56 2019

@author: joscelynec
"""
"""
Iterative Binary Search of a Sorted Array
Adapted from:
https://codereview.stackexchange.com/questions/117180/python-2-binary-search
"""
def binary_search(array, value):
    start, stop = 0, len(array)
    while start < stop:
        offset = start + stop >> 1
        sample = array[offset]
        if sample < value:
            start = offset + 1
        elif sample > value:
            stop = offset
        else:
            return offset
    return -1


"""
Finds pivot index in sorted rotated list
for example, for [6, 7, 8, 9, 10, 1, 2, 3, 4]
pivot = 5
"""
def find_pivot(input_list):
    start = 0
    end = len(input_list) - 1
    while start <= end:
        mid = (start + end)//2
        if input_list[start] <= input_list[end]: #check if list is not rotated
            return start
        elif input_list[start] <= input_list[mid]: #first to mid is sorted, pivot is in other half of list
            start = mid +1
        else: #pivot is in first half of list
            end = mid 
    return start
     
   

"""
Modify/adapt binary search to search a rotated sorted input_list
in O(nlog n) time
Uses find_pivot(input_list) and then binary search on two sub lists
Find the index by searching in a rotated sorted input_list
Args:
  input_list(input_list), number(int): Input input_list to search and the target
Returns:
  int: Index or -1
"""
def rotated_input_list_search(input_list, number):
    #Null input
    if input_list == None or number == None:
        return -1
    #Empty List
    if input_list == [] or number == None:
        return -1
   
    pivot_index = find_pivot(input_list)
    #perform binary search on each list divided into at the pivot
    temp = binary_search(input_list[0: pivot_index], number)
    if temp != -1:
        return temp
    temp = binary_search(input_list[pivot_index: len(input_list)], number)
    if temp != -1:
        return temp + pivot_index
    #number not found
    return -1
#print(rotated_input_list_search([6, 7, 8, 1, 2, 3, 4], 6))



def linear_search(input_list, number):
    #Null input
    if input_list == None or number == None:
        return -1
    #Empty List
    if input_list == [] or number == None:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
#Udacity test function modified for None or Empty inputs
def test_function(test_case):
    if test_case == None:
         print("None")
         return
        
    input_list = test_case[0]
    if input_list == [None]:
        print("None")
        return
    
    number = test_case[1]
    if number == None:
        print("None")
        return
    
    
    if linear_search(input_list, number) == rotated_input_list_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
 

test_function(None)#Null Inputs
test_function([[None], None])#Null Input_lists
test_function([[None], 6])#Null Input_lists
test_function([[], None])#Empty List, None for number
test_function([[], 6])#Empty List
test_function([[8], 8])#Singleton List with value
test_function([[8], 7])#Singleton List without value
#More tests two element lists
test_function([[7,8], 8])
test_function([[8,5], 8])
test_function([[7,8], 9])
test_function([[8,5], 4])
#Full cycle of a sorted list, value present and not present
test_function([[1, 2, 3, 4, 5], 3])
test_function([[1, 2, 3, 4, 5], 6])
test_function([[2, 3, 4, 5, 1], 3])
test_function([[2, 3, 4, 5, 1], 6])
test_function([[3, 4, 5, 1, 2], 3])
test_function([[3, 4, 5, 1, 2], 6])
test_function([[4, 5, 1, 2, 3], 3])
test_function([[4, 5, 1, 2, 3], 6])
test_function([[5, 1, 2, 3, 4], 3])
test_function([[5, 1, 2, 3, 4], 6])
#Udacity supplied tests
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
"""
None
None
None
None
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
"""






