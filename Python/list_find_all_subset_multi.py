# https://leetcode.com/problems/subsets/
"""
Given an integer array nums of unique elements, return all possible subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any
 order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
class Solution1:

    def get_subsets(self, nums, s, length, t_list, op_list):
        if s>=length: return
        for i in range(s,length):
            t_list.append(nums[i])
            op_list.append(list(t_list))
            self.get_subsets(nums, i+1, length, t_list, op_list)
            t_list.pop()

    # Time and space complexity - O(N*(2^N))
    # 2^N subset and N for copying it
    def subsets_rec(self, nums: list[int]) -> list[list[int]]:
        op_list = [[]]
        self.get_subsets(nums, 0, len(nums), list(), op_list)
        return op_list
    
    # Time and space complexity - O(N*(2^N))
    # 2^N subset and N for copying it
    def subsets(self, nums: list[int]) -> list[list[int]]:
        op_list = list()
        length = len(nums)
        count = 1<<length
        for i in range(count):
            t_list = list()
            for j in range(length):
                if i&(1<<j)!=0:
                    t_list.append(nums[j])
            op_list.append(t_list)
        return op_list

# https://leetcode.com/problems/subsets-ii/
"""
Given an integer array nums that may contain duplicates, return all possible
 subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution
 in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
class Solution:
    def subsetsWithDup_1(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        op_set = set()
        length = len(nums)
        count = 1<<length
        for i in range(count):
            t_list = list()
            for j in range(length):
                if i&(1<<j)!=0:
                    t_list.append(nums[j])
            t_tuple = tuple(t_list)
            if t_tuple not in op_set:
                op_set.add(t_tuple)
        return op_set

    def get_subset_dp(self, nums, s, length, t_list, op_list):
        if s>=length: return
        seen = set()
        for i in range(s, length):
            if nums[i] not in seen:
                seen.add(nums[i])
                t_list.append(nums[i])
                op_list.append(list(t_list))
                self.get_subset_dp(nums, i+1, length, t_list, op_list)
                t_list.pop()
    
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        length = len(nums)
        op_list = [[]]
        self.get_subset_dp(nums, 0, length, [], op_list)
        return op_list