# https://leetcode.com/problems/zero-array-transformation-iv
"""
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Select a subset of indices in the range [li, ri] from nums.
 - Decrement the value at each selected index by exactly vali.
 - A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in 
 sequence, nums becomes a Zero Array. If no such k exists, return -1.

Example 1:
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
Output: 2
Explanation:
For query 0 (l = 0, r = 2, val = 1):
Decrement the values at indices [0, 2] by 1.
The array will become [1, 0, 1].
For query 1 (l = 0, r = 2, val = 1):
Decrement the values at indices [0, 2] by 1.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
Output: -1
Explanation:
It is impossible to make nums a Zero Array even after all the queries.

Example 3:
Input: nums = [1,2,3,2,1], queries = [[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]]
Output: 4
Explanation:
For query 0 (l = 0, r = 1, val = 1):
Decrement the values at indices [0, 1] by 1.
The array will become [0, 1, 3, 2, 1].
For query 1 (l = 1, r = 2, val = 1):
Decrement the values at indices [1, 2] by 1.
The array will become [0, 0, 2, 2, 1].
For query 2 (l = 2, r = 3, val = 2):
Decrement the values at indices [2, 3] by 2.
The array will become [0, 0, 0, 0, 1].
For query 3 (l = 3, r = 4, val = 1):
Decrement the value at index 4 by 1.
The array will become [0, 0, 0, 0, 0]. Therefore, the minimum value of k is 4.

Example 4:
Input: nums = [1,2,3,2,6], queries = [[0,1,1],[0,2,1],[1,4,2],[4,4,4],[3,4,1],[4,4,5]]
Output: 4 

Constraints:
1 <= nums.length <= 10
0 <= nums[i] <= 1000
1 <= queries.length <= 1000
queries[i] = [li, ri, vali]
0 <= li <= ri < nums.length
1 <= vali <= 10
"""

from typing import List

class Solution:

    def compute_all_sum_by_add_k(self, arr, max_sum, k):
        i = max_sum
        while i>=k:
            if arr[i-k]>0:
                arr[i]+=arr[i-k]
            i-=1
    
    def compute_all_sum_by_sub_k(self, arr, max_sum, k):
        i = 0
        while (i+k)<=max_sum:
            if arr[i]>0:
                arr[i+k]-=arr[i]
            i+=1

    def compute_all_sum_by_add(self, arr, arr_len, nums_list):
        for num in nums_list:
            self.compute_all_sum_by_add_k(arr, arr_len, num)
    
    def compute_all_sum_by_sub(self, arr, arr_len, nums_list):
        for num in nums_list:
            self.compute_all_sum_by_sub_k(arr, arr_len, num)

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        nums_len = len(nums)
        queries_len = len(queries)
        count = [[list(), list()] for i in range(nums_len+1)] # [[nums_list_to_add, nums_list_to_sub], [], ..]
        sums_arr = [0 for i in range(max(nums)+1)]
        sums_arr_len = len(sums_arr)-1
        sums_arr[0] = 1
        j = 0
        for i in range(nums_len):
            self.compute_all_sum_by_sub(sums_arr, sums_arr_len, count[i][1])
            self.compute_all_sum_by_add(sums_arr, sums_arr_len, count[i][0])
            # print(f'{i=} {j=} {sums_arr=} {count=}')
            while sums_arr[nums[i]]==0 and j<queries_len:
                s, e, val = queries[j]
                if e<i: j+=1
                else:
                    if s>i: count[s][0].append(val)
                    else: self.compute_all_sum_by_add_k(sums_arr, sums_arr_len, val)
                    count[e+1][1].append(val)
                    j+=1
            # print(f'{i=} {j=} {sums_arr=} {count=}')
            if sums_arr[nums[i]]==0: return -1
        return j