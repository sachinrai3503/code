# https://leetcode.com/problems/target-sum
"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' 
 before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and 
 concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        nums_sum = sum(nums)
        if nums_sum<abs(target): return 0
        base = nums_sum
        dp_len = nums_sum*2+1
        dp = [[0 for j in range(dp_len)] for i in range(2)]
        dp[nums_len%2][base] = 1 # assuming 0 can be made by even 0 element
        for i in range(nums_len-1, -1, -1):
            cur_row = i%2
            prev_row = 0 if cur_row==1 else 1
            for j in range(dp_len):
                t_target = j - base
                b1, b2 = t_target - nums[i], t_target + nums[i]
                b1_index, b2_index = b1 + base, b2 + base
                op1, op2 = 0, 0
                if b1>=-base:
                    op1 = dp[prev_row][b1_index]
                if b2<=base:
                    op2 = dp[prev_row][b2_index]
                dp[cur_row][j] = op1 + op2
            # print(dp[cur_row])
        return dp[0][target+base]