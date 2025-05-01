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

from typing import List

class Solution:

    def can_swap(self, nums1, nums2, i):
        if i==0: return True
        j = i-1
        if nums1[j]<nums2[i] and nums2[j]<nums1[i]: return True
        return False
    
    def can_swap_at_i(self, nums1, nums2, nums_len, i):
        j = i+1
        if j==nums_len: return True
        if nums1[i]<nums2[j] and nums2[i]<nums1[j]: return True
        return False

    def is_swap_needed(self, nums1, nums2, nums_len, i):
        if i==(nums_len-1): return False
        j = i+1
        if nums1[i]>=nums1[j] or nums2[i]>=nums2[j]: return True
        return False

    # will not give the min swaps for below TC
    # [0,7,8,10,10,11,12,13,19,18] & [4,4,5,7,11,14,15,16,17,20]
    def minSwap1(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        nums_len = len(nums1)
        for i in range(nums_len):
            if self.is_swap_needed(nums1, nums2, nums_len, i):
                count+=1
                can_swap_i = self.can_swap(nums1, nums2, i)
                can_swap_i_1 = self.can_swap(nums1, nums2, i+1)
                if can_swap_i and can_swap_i_1:
                    print(f'swapping {i=}')
                    nums1[i], nums2[i] = nums2[i], nums1[i]
                elif not can_swap_i and can_swap_i_1:
                    print(f'swapping {i+1=}')
                    nums1[i+1], nums2[i+1] = nums2[i+1], nums1[i+1]
        print(f'{nums1=}')
        print(f'{nums2=}')
        return count
    
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        nums_len = len(nums1)
        w, wo = 0, 0 # w == With swapping, wo == without swapping
        for i in range(nums_len-1, -1, -1):
            if self.is_swap_needed(nums1, nums2, nums_len, i):
                temp = w
                w = 1 + wo
                wo = temp
            elif self.can_swap_at_i(nums1, nums2, nums_len, i):
                temp = w
                w = 1 + min(w, wo)
                wo = min(temp, wo)
            else:
                w = 1 + w
                wo = wo
        return min(w, wo)