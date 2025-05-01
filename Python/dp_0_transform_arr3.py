# https://leetcode.com/problems/zero-array-transformation-iii
"""
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
 - The amount by which the value is decremented can be chosen independently for each index.
 - A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be
 converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

Example 1:
Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
Output: 1
Explanation:
After removing queries[2], nums can still be converted to a zero array.
Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.

Example 2:
Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]
Output: 2
Explanation:
We can remove queries[2] and queries[3].

Example 3:
Input: nums = [1,2,3,4], queries = [[0,3]]
Output: -1
Explanation:
nums cannot be converted to a zero array even after using all the queries.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length
"""

from typing import List
import heapq

class Solution:

    # This is wrong. TC - nums = [0,0,1,1,0], queries = [[3,4],[0,2],[2,3]]
    def maxRemoval1(self, nums: List[int], queries: List[List[int]]) -> int:
        nums_len = len(nums)
        queries_len = len(queries)
        count = [0 for i in range(nums_len+1)]
        queries.sort(key = lambda x : (x[0], -x[1]))
        print(f'{queries=}')
        taken_queries = 0
        t_count = 0
        j = 0
        for i in range(nums_len):
            while (t_count+count[i])<nums[i] and j<queries_len:
                s, e = queries[j]
                if i>e: j+=1
                elif i<s: break
                else:
                    count[i]+=1
                    count[e+1]-=1
                    j+=1
                    taken_queries+=1
            t_count+=count[i]
            print(f'{count=}')
            if t_count<nums[i]: return -1
        return queries_len-taken_queries
    
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        nums_len = len(nums)
        queries_len = len(queries)
        count = [0 for i in range(nums_len+1)]
        heap = list() # to store the queries applicable
        queries.sort()
        # print(f'{queries=}')
        taken_queries = 0
        t_count = 0
        j = 0
        for i in range(nums_len):
            while j<queries_len:
                s, e = queries[j]
                if i>e: j+=1
                elif i<s: break
                else:
                    heapq.heappush(heap, -e) # this query is valid for index i
                    j+=1
            while heap and (t_count+count[i])<nums[i]:
                e = -heapq.heappop(heap)
                if e<i: continue
                count[i]+=1
                count[e+1]-=1
                taken_queries+=1
            t_count+=count[i]
            # print(f'{count=}')
            if t_count<nums[i]: return -1
        return queries_len-taken_queries