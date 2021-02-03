# https://www.geeksforgeeks.org/find-k-closest-elements-given-value/
# https://leetcode.com/problems/find-k-closest-elements/
"""
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
Examples:

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
Note that if the element is present in array, then it should not be in output,
 only the other closest elements are required.
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr)-k
        while left<right:
            mid = left + (right-left)//2
            if x-arr[mid]>arr[mid+k]-x:
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]