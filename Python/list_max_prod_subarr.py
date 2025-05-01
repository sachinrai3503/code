# https://www.geeksforgeeks.org/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/
"""
Given an integer array nums, find a subarray that has the largest product, 
 and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

from sys import maxsize
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -maxsize
        p1, p2 = 1, None
        for num in nums:
            p1*=num
            if p2 is not None:
                p2*=num
                max_prod = max(max_prod, p2)
            max_prod = max(max_prod, p1)
            if p1<0 and p2 is None:
                p2 = 1
            elif p1==0:
                p1, p2 = 1, None
            # print(f'{num=} {p1=} {p2=} {max_prod=}')
        return max_prod