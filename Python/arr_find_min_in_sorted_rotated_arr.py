# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
 For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
 array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of
 this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

class Solution:
    # For unique arr ele
    def findMin(self, nums: list[int]) -> int:
        s, e = 0, len(nums)-1
        while s<=e:
            if s==e: return nums[s]
            mid = s + (e-s)//2
            if s==mid or nums[s]<nums[mid]: # 1st half of array sorted or 2 element arr
                if nums[mid]<nums[e]: return nums[s] # full array sorted
                s = mid+1 # full array not sorted
            else: e = mid # 1st half not sorted. Note -> e != (mid-1) as mid could be the min
        return None
    
    # For duplicate arr ele
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
    def findMin_dup(self, nums: list[int]) -> int:
        s, e = 0, len(nums)-1
        while s<=e:
            if s==e: return nums[s]
            mid = s + (e-s)//2
            if nums[s]==nums[mid] and nums[mid]==nums[e]:
                if s==mid: return nums[s]
                s+=1
                e-=1
            elif s!=mid and nums[s]==nums[mid]: s = mid # Note - s!=(mid+1) eg = [1,1,2]
            elif nums[mid]==nums[e]: e = mid # e!=(mid-1) eg = [2,1,1]
            else:
                if s==mid or nums[s]<nums[mid]: # 2 ele case or 1st half is sorted
                    if nums[mid]<nums[e]: return nums[s] # full arr sorted
                    s = mid+1
                else: e = mid # 1st half not sorted. Note -> e!=(mid-1)
        return None
                    