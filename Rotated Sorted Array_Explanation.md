## Search in a Rotated Sorted Array

Given a sorted array which is rotated at some random pivot point find a target value.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

- Given a target value to search, if found in the array return its index, otherwise return -1.
- One can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example:
- Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4


The idea of the algorithm its the find the index of what is called the “pivot” of the rotated sorted array. This “pivot” is the index of the minimal element.

Examples:
- Input: nums = [0,1,2,4,5,6,7] pivot = 0
- Input: nums = [1,2,4,5,6,7,0] pivot = 6
- Input: nums = [5,6,7,0,1,2,4] pivot = 3
- Input: nums = [4,5,6,7,0,1,2] pivot = 4

Once the pivot is found an ordinary binary search for the value in question is performed on the two sorted sub-arrays split at the pivot. 

For example: 
I- nput: nums = [4,5,6,7,0,1,2] pivot = 4

- => binary_search([4,5,6,7], value)
- => binary_search([0,1,2], value)

The pivot itself is found using a divide and conquer algorithm. That the pivot could be found using a divide and conquer strategy is somewhat surprising. Since finding the pivot and each of the two binary searches are all `O(log n)`, the overall performance of the algorithm is `O(log n)` as required. Since, the algorithm uses iteration, not recursion and therefore does not require extra storage space depending on the input list size, the space complexity is `O(1)`.


