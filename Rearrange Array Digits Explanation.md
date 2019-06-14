## Rearrange Array Digits

Rearrange Array Elements so as to form two integers such that their sum is a maximum and return these two numbers. One can assume that all array elements are in the range `[0, 9]`. The number of digits in both the numbers cannot differ by more than 1. One can not use any sorting function that Python provides and the expected time complexity must be `O(nlog(n))`.

Example: [1, 2, 3, 4, 5]

One expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

The algorithm firsts sorts the list elements using a Merge Sort. The  Merge Sort was chosen as it always has `O(nlogn)` complexity. The expected time complexity is then  `O(nlogn)`. Instead of crafting a special reverse function, Python’s reverse method, `O(n)` complexity, is then used to produce produce a descending list. The Rearrange method then uses a greedy approach to build the two lists by alternatively placing elements into the two lists. 

For example:
- [4,3,2,1] => [4] [ ] => [4] [3] => [42] [3] => [42] [31] => return [42] [31]

- This process is also `O(n)`, so the overall complexity is `O(nlogn)`. The space complexity of the Merge Sort is `O(n)` as are the reverse and Rearrange methods, the overall space complexity is `O(n)`.



