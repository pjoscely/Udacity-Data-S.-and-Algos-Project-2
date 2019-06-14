#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:23:49 2019

@author: joscelynec
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    Use method of bisection while keeping track of computations
    using Python's integer division yields O(log n)//
    """
    if number == None:#input is None
        return None
    if number < 0:# return -1  if number is negative
        return -1
   
    #Main body of code
    low = 1
    high = number
    guess_old = low
    guess_new = high
    #Binary bisection method
    while guess_old != guess_new:
      guess_old = guess_new 
      square = guess_old**2;
      if square < number:
        low = guess_old
      elif square > number:
        high = guess_old
      guess_new = (low + high)//2#integer division
        
    return guess_new
"""
Test Code
"""
print ("Pass" if  (None == sqrt(None)) else "Fail")#Null input

print ("Pass" if  (-1 == sqrt(-27)) else "Fail")#Negative input test

print ("Pass" if  (0 == sqrt(0)) else "Fail")#Zero input
print ("Pass" if  (1 == sqrt(1)) else "Fail")#1 input
print ("Pass" if  (1 == sqrt(2)) else "Fail")#2 input
print ("Pass" if  (1 == sqrt(3)) else "Fail")#3 input
print ("Pass" if  (2 == sqrt(4)) else "Fail")#Negative input

print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (3 == sqrt(15)) else "Fail")

print ("Pass" if  (3 == sqrt(9)) else "Fail")

print ("Pass" if  (4 == sqrt(16)) else "Fail")

print ("Pass" if  (24 == sqrt(624)) else "Fail")
print ("Pass" if  (31 == sqrt(1000)) else "Fail")

#Large Number input
print ("Pass" if  (166564950== sqrt(27743882883774747)) else "Fail")
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
Pass
"""