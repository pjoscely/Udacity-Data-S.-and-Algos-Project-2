## Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. NO use OF any sorting function that Python provides is allowed.

Note: `O(n)` does not necessarily mean single-traversal. For example: if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

According to Wikipedia:

“The Dutch national flag problem (DNF) is a computer science programming problem proposed by Edsger Dijkstra.The flag of the Netherlands consists of three colors: red, white and blue. Given balls of these three colors arranged randomly in a line (the actual number of balls does not matter), the task is to arrange them such that all balls of the same color are together and their collective color groups are in the correct order.”

To solve this problem, Dijkstra algorithm in pseudo-algorithm form is used:

procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    n ← size of A - 1

    while j ≤ n:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[n]
            n ← n - 1
        else:
            j ← j + 1

 The sorting is accomplished in a single pass and has therefore time complexity `O(n)`. Since the same number variables are used, independent of the input array, the space complexity is `O(1)`.
