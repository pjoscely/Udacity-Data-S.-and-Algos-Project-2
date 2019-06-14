#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:59:10 2019

@author: joscelynec
"""

#Udacity Merge Sort
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum. 
    Return these two numbers. You can assume that all array elements 
    are in the range [0, 9]. The number of digits in both the numbers cannot differ 
    by more than 1

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
#********************************************************************************  
    if input_list == None or len(input_list) == 0:#degenerate cases return -1,-1
        return -1, -1
    
    if len(input_list) == 1 :#degenerate case of a one item list
        return input_list[0], 0
    
    input_list = mergesort(input_list)
    input_list.reverse()#Python method
    num1 = ""
    num2 = ""
    for i in range(len(input_list)):
        if i %2 ==0:
            num1 +=str(input_list[i])
        if i %2 ==1:
            num2 +=str(input_list[i])
    return int(num1), int(num2)
            
#*******************************************************************************     
       

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
"""
Test Code
"""

#Null input 
test_function([None, [-1, -1]])

#Empty input    
test_function([[], [-1, -1]])    

#Single value input
test_function([[1], [1, 0]]) 

"""
Various inputs
"""
      
test_function([[1, 2], [2, 1]])
test_function([[1, 2,3], [32, 1]])
test_function ([[9,9], [9, 9]])
test_function([[1,2,3,4], [42, 31]]) 
test_function([[2,2,2,2,2], [222, 22]]) 
"""
Udacity supplied test cases
"""
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 2,5,6,0,4], [952, 640]])
"""
Larger Inputs
"""
test_function([[9,8,7,6,5,4,3,2,1,0,0], [975310, 86420]])
test_function([[2,3,1,4,2,3,1,3,3,4,8,6,9,9,1,0,0], [984332110, 96433210]])
"""
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