# Finding the Square Root of an Integer

## Problem Description
- Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
- For example if the given number is 16, then the answer would be 4.
- If the given number is 27, the answer would be 5 because `sqrt(5) = 5.196` whose floor value is 5.

## Algorithm Efficiency
- The expected time complexity is `O(log(n))`
- The space complexity is `O(1)`.

### Explanation
The idea here is to use the method a of bisection. 
Given a positive integer `n`, a mid value is computed and squared. 
Based on the squared result being less than or greater than `n` a new mid value is produced. 
To obtain a floor value the Python integer division `//` operator is used. 
Just as a binary search has time complexity `O(log(n))`, so does this bisection method.
Since the program uses the same small set of variables the space complexity is `O(1)`.
