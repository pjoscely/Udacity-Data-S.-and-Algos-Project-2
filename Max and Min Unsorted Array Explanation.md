## Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in `O(n)` time. Do not use Python's inbuilt functions to find min and max.

There were not many design issues with this problem. The straight forward algorithm starts off by initializing min and max variables to the the first list entry. It then makes a single pass through the list updating the initial min and max values depending on the current list entry. The the end of the list traversal both min and max value are then returned. The time complexity is `O(n)`. And, since the same number variables are used, independent of the input array, the space complexity is `O(1)`.
