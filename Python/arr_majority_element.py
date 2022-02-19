# https://leetcode.com/problems/majority-element-ii
# https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times
# https://www.geeksforgeeks.org/print-all-array-elements-appearing-more-than-n-k-times
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

Follow up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:
    
    def process_num(self, num_info, length, num):
        empty_index = -1
        for i in range(length):
            if num_info[i] is None: 
                empty_index = i
            elif num_info[i][0]==num:
                num_info[i][1]+=1
                return
        if empty_index!=-1:
            num_info[empty_index] = [num, 1]
        else:
            for i in range(length):
                num_info[i][1]-=1
                if num_info[i][1]==0:
                    num_info[i] = None
        return None
    
    def get_count(self, nums, x):
        count = 0
        for num in nums:
            if num==x:
                count+=1
        return count
    
    def majorityElement(self, nums: list[int]) -> list[int]:
        op = list()
        k = 3
        length = len(nums)
        req_freq = length//k
        num_info = [None for i in range(k-1)]
        for num in nums:
            self.process_num(num_info, k-1, num)
            # print(num_info)
        for info in num_info:
            if info is not None:
                count = self.get_count(nums, info[0])
                if count>req_freq:
                    op.append(info[0])
        return op