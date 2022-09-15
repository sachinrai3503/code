# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining
 elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. 
 The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. 
 herefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

Constraints:
1 <= arr.length <= 105
0 <= arr[i] <= 109
"""

from sys import maxsize

class Solution:
    
    def get_floor(self, arr, s, e, k):
        _floor = -1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]<=k:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor

    def get_ceil(self, arr, s, e, k):
        _ceil = e+1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]<k:
                s = mid+1
            else:
                _ceil = mid
                e = mid-1
        return _ceil
    
    # [1,2,2,2,2,2,3,1,7,5,1,2,2,2,2,2,2,5,6]
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        arr_len = len(arr)
        i, j = 0, arr_len-1
        while i<(arr_len-1):
            if arr[i]>arr[i+1]:
                break
            i+=1
        if i==(arr_len-1): return 0
        while j>0:
            if arr[j]<arr[j-1]:
                break
            j-=1
        # print(f'{i=}, {j=}')
        ti, tj = 0, arr_len-1
        min_size = maxsize
        while ti<=i and j<=tj:
            if arr[i]<=arr[j]: min_size = min(min_size, j-i-1)
            while ti<=i:
                if arr[ti]>arr[j]: break
                ti+=1
            while tj>=j:
                if arr[tj]<arr[i]: break
                tj-=1
            min_size = min(min_size, min(j-ti, tj-i))
            i-=1
            j+=1
        return min_size