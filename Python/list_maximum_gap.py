# https://leetcode.com/problems/maximum-gap/
# https://www.geeksforgeeks.org/maximum-adjacent-difference-array-sorted-form/
"""
Given an unsorted array, find the maximum difference between the successive
 elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Note:
You may assume all elements in the array are non-negative integers and fit
 in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""

from sys import maxsize

class Solution:
    def maximumGap1(self, nums: list[int]) -> int:
        if len(nums)<2: return 0
        min_num = maxsize
        max_num = -maxsize
        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
        map_len = max_num-min_num+1
        list_map = [False for i in range(map_len)]
        for num in nums:    list_map[num-min_num] = True
        max_diff = -maxsize
        prev = 0
        i = 0
        while i<map_len:
            if list_map[i]:
                if (i-prev)>max_diff: max_diff = i-prev
                prev = i
            i+=1
        return max_diff
        
    def maximumGap2(self, nums: list[int]) -> int:
        length = len(nums)
        if length<2: return 0
        nums.sort()
        print(nums)
        max_diff = -maxsize
        i = 1
        while i<length:
            if nums[i]-nums[i-1]>max_diff:
                max_diff = nums[i]-nums[i-1]
            i+=1
        return max_diff
    
    def get_max_min(self, nums):
        max_num, min_num = -maxsize, maxsize
        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        return min_num, max_num
    
    def maximumGap(self, nums):
        length = len(nums)
        if length<2: return 0
        min_num, max_num = self.get_max_min(nums)
        bucket_size = max(1, (max_num-min_num)//(length-1))
        bucket_count = (max_num-min_num)//bucket_size + 1
        buckets = [[maxsize, -maxsize] for i in range(bucket_count)]
        # print(bucket_size, bucket_count)
        for num in nums:
            num_index = (num-min_num)//bucket_size
            # print(num_index)
            buckets[num_index][0] = min(buckets[num_index][0], num)
            buckets[num_index][1] = max(buckets[num_index][1], num)
        max_gap = 0
        # print(buckets)
        prev_bucket = None
        for i in range(bucket_count):
            if buckets[i][0]!=maxsize:
                if prev_bucket==None: prev_bucket = buckets[0]
                else:
                    max_gap = max(max_gap, buckets[i][0]-prev_bucket[1])
                    prev_bucket = buckets[i]
        return max_gap