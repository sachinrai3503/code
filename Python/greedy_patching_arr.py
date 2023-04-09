# https://leetcode.com/problems/patching-array
"""
Given a sorted integer array nums and an integer n, add/patch elements to the
 array such that any number in the range [1, n] inclusive can be formed by the sum
 of some elements in the array.

Return the minimum number of patches required.

Example 1:
Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].

Example 3:
Input: nums = [1,2,2], n = 5
Output: 0
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
"""

from typing import List

class Solution:

    def count_marked(self, arr, arr_len, n):
        count = 0
        for i in range(arr_len-1, n-1, -1):
            if arr[i] is None and arr[i-n] is not None:
                arr[i] = 1
                count+=1
        return count

    # This timesout
    def minPatches_1(self, nums: List[int], n: int) -> int:
        op = [None for i in range(n+1)]
        op[0] = 1
        patch_count = 0
        count = 0
        for num in nums:
            count+=self.count_marked(op, n+1, num)
        # print(f'{op=} {count=} {patch_count=}')
        for i in range(n+1):
            if count==n: break
            if op[i] is not None: continue
            patch_count+=1
            count+=self.count_marked(op, n+1, i)
        return patch_count
    
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        nums_len = len(nums)
        i, cur_reach = 0, 0
        while cur_reach<n:
            while i<nums_len and nums[i]<=(cur_reach+1):
                cur_reach+=nums[i]
                i+=1
                if cur_reach>=n: return patches
            cur_reach+=(cur_reach+1)
            patches+=1
        return patches