# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
"""
You are given two integer arrays of the same length nums1 and nums2. 
In one operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element
 at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly
 increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only
 if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

Example 1:
Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation: Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4] which are both strictly increasing.

Example 2:
Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
Output: 1

Constraints:
2 <= nums1.length <= 105
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 2 * 105
"""

from sys import maxsize

class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        with_swap, without_swap = 1, 0
        prev_a, prev_b = nums1[-1], nums2[-1]
        for i in range(len(nums1)-2, -1, -1):
            t_with, t_without = maxsize, maxsize
            prev_a, prev_b = nums1[i+1], nums2[i+1]
            if nums1[i]<prev_a and nums2[i]<prev_b:
                t_without = without_swap
                t_with = 1 + with_swap
            if nums1[i]<prev_b and nums2[i]<prev_a:
                t_without = min(t_without, with_swap)
                t_with = min(t_with, 1 + without_swap)
            with_swap = t_with
            without_swap = t_without
            # print(without_swap, with_swap)
            # print('*'*20)
        return min(with_swap, without_swap)