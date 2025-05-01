# https://leetcode.com/problems/partition-equal-subset-sum/
"""
Given a non-empty array nums containing only positive integers, find if the array
 can be partitioned into two subsets such that the sum of elements in both subsets
 is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from typing import List

class Solution:
    
    def get_all_possible_sum_combinations(self, nums, nums_len):
        op = list()
        op_len = 0
        for num in nums:
            new_sum_added = 0
            for i in range(op_len):
                op.append(op[i] + num)
                new_sum_added+=1
            op.append(num)
            new_sum_added+=1
            op_len+=new_sum_added
        op.append(0)
        return op

    # This is same approach as in https://leetcode.com/problems/closest-subsequence-sum/ & 
    # https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
    # But as contraint n==200 this will time out 
    def canPartition_1(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        mid_len = nums_len//2
        total_sum = sum(nums)
        if total_sum%2: return False
        goal = total_sum//2
        left_nums_sum_comb_list = self.get_all_possible_sum_combinations(nums[:mid_len], mid_len)
        right_nums_sum_comb_list = self.get_all_possible_sum_combinations(nums[mid_len:], mid_len)
        left_nums_sum_comb_list.sort()
        right_nums_sum_comb_list.sort()
        # print(f'{left_nums_sum_comb_list=}')
        # print(f'{right_nums_sum_comb_list=}')
        left_len, right_len = len(left_nums_sum_comb_list), len(right_nums_sum_comb_list)
        i, j = 0, right_len-1
        while i<left_len and j>=0:
            s1, s2 = left_nums_sum_comb_list[i], right_nums_sum_comb_list[j]
            t_sum = s1+s2
            if t_sum==goal: return True
            if t_sum<goal:
                i+=1
            else:
                j-=1
        return False
    
    # given the constraint creating a dp[] of len==sum(nums)//2 is efficient approach here
    def canPartition(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        total_sum = sum(nums)
        if total_sum%2: return False
        goal = total_sum//2
        dp = [False for i in range(goal+1)]
        dp[0] = True
        for num in nums:
            if num>goal: return False
            for j in range(goal, num-1, -1):
                dp[j] = dp[j-num] if not dp[j] else dp[j]
            # print(f'{dp=}')
        return dp[-1]