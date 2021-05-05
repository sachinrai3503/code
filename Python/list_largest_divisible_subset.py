# https://leetcode.com/problems/largest-divisible-subset/
"""
Given a set of distinct positive integers nums, return the largest subset answer
 such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""

from sys import maxsize

class Solution:
    
    def result_list(self, nums, index_list, start_index):
        op_list = list()
        while start_index!=-1:
            op_list.append(nums[start_index])
            start_index = index_list[start_index]
        return op_list
    
    def largestDivisibleSubset_DP(self, nums: list[int]) -> list[int]:
        start_index = -1
        max_len = 0
        length = len(nums)
        nums.sort()
        len_list = [0 for i in range(length)]
        index_list = [-1 for i in range(length)]
        for i in range(length-1, -1, -1):
            t_len = 0
            next_index = -1
            for j in range(i+1, length):
                if nums[j]%nums[i]==0 and len_list[j]>t_len:
                    t_len = len_list[j]
                    next_index = j
            len_list[i] = t_len + 1
            index_list[i] = next_index
            if len_list[i]>max_len:
                max_len = len_list[i]
                start_index = i
        return self.result_list(nums, index_list, start_index)
    
    def get_factor(self, n):
        factor_list = list()
        for i in range(1, int(n**.5)+1):
            if n%i==0:
                factor_list.append(i)
                factor_list.append(n//i)
        return factor_list
    
    def result_list2(self, nums, factor_len_dict, from_num):
        op_list = list()
        while from_num!=maxsize:
            op_list.append(from_num)
            from_num = factor_len_dict[from_num][1]
        return op_list
            
    
    # This is also DP, but instead of checking all the numbers just checks only
    # the factors
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        last_num_in_larget_subset = maxsize
        max_len = 0
        length = len(nums)
        nums.sort()
        # Key = factor, value = [len_of_factors, prev_factor]
        factor_len_dict = dict()
        for i in range(length):
            num = nums[i]
            factors = self.get_factor(num)
            t_len = 0
            prev_factor = maxsize
            for factor in factors:
                if factor in factor_len_dict:
                    value = factor_len_dict[factor]
                    if value[0]>t_len:
                        t_len = value[0]
                        prev_factor = factor
            factor_len_dict[num] = [t_len+1, prev_factor]
            if (t_len+1)>max_len:
                max_len = t_len+1
                last_num_in_larget_subset = num
        # print(factor_len_dict)
        return self.result_list2(nums, factor_len_dict, last_num_in_larget_subset)