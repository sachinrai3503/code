# https://leetcode.com/problems/find-in-mountain-array
# https://leetcode.com/problems/peak-index-in-a-mountain-array
# https://www.geeksforgeeks.org/find-element-bitonic-array
# https://www.geeksforgeeks.org/minimum-in-an-array-which-is-first-decreasing-then-increasing
# https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/
"""
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that 
 mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using
 a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index,
 which is 2.

Example 2:
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:
3 <= mountain_arr.length() <= 104
0 <= target <= 109
0 <= mountain_arr.get(index) <= 109
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def is_peak(self, arr, s, e, index):
        ele_index = arr.get(index)
        if index!=s and arr.get(index-1)>ele_index:
            return -1
        if index!=e and ele_index<arr.get(index+1):
            return 1
        return 0

    def binary_search_incr(self, arr, s, e, x):
        while s<=e:
            mid = s + (e-s)//2
            ele_mid = arr.get(mid)
            if ele_mid==x: return mid
            elif ele_mid>x: e = mid-1
            else: s = mid+1
        return -1

    def binary_search_decr(self, arr, s, e, x):
        while s<=e:
            mid = s + (e-s)//2
            ele_mid = arr.get(mid)
            if ele_mid==x: return mid
            elif ele_mid<x: e = mid-1
            else: s = mid+1
        return -1

    def find_peak_index(self, arr, length):
        s, e = 0, length-1
        while s<=e:
            mid = s + (e-s)//2
            peak = self.is_peak(arr, s, e, mid)
            if peak==0: return mid
            elif peak==-1: e = mid-1
            elif peak==1: s = mid+1
        return -1
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        peak_index = self.find_peak_index(mountain_arr, length)
        # print(peak_index)
        if target>=mountain_arr.get(0) and target<=mountain_arr.get(peak_index): 
            ele_at = self.binary_search_incr(mountain_arr, 0, peak_index, target)
            if ele_at!=-1: return ele_at
        return self.binary_search_decr(mountain_arr, peak_index+1, length-1, target)