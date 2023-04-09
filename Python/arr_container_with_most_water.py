# https://leetcode.com/problems/container-with-most-water
# https://www.geeksforgeeks.org/maximum-water-that-can-be-stored-between-two-buildings
"""
You are given an integer array height of length n. There are n vertical lines drawn such
 that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
 contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
 In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 
Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from sys import maxsize
from typing import List

class Solution:

    def get_increasing_height_from_right(self, arr, arr_len):
        op = []
        cur_max = -1*maxsize
        for i in range(arr_len-1, -1, -1):
            cur_max = max(arr[i], cur_max)
            op.insert(0, cur_max)
        return op

    def binary_search_incresing_arr(self, arr, s, e, k):
        _floor = None
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]>=k:
                _floor = mid
                e = mid-1
            else:
                s = mid+1
        return _floor
    
    def binary_search_decreasing_arr(self, arr, s, e, k):
        _ceil = None
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]>=k:
                _ceil = mid
                s = mid+1
            else:
                e = mid-1
        return _ceil

    # o(nlogn) - times out
    def maxArea_binary_search(self, height: List[int]) -> int:
        height_len = len(height)
        max_water = 0
        increasing_height_from_right = self.get_increasing_height_from_right(height, height_len)
        increasing_height_from_left = []
        prev = -maxsize
        for i in range(height_len):
            prev = max(prev, height[i])
            increasing_height_from_left.append(prev)
            left = self.binary_search_incresing_arr(increasing_height_from_left, 0, i-1, height[i])
            right = self.binary_search_decreasing_arr(increasing_height_from_right, i+1, height_len-1, height[i])
            water_stored = 0 if left is None else min(height[left], height[i])*(i-left)
            if right is not None:
               water_stored+=min(height[right], height[i])*(right-i)
            max_water = max(max_water, water_stored)
        #     print(f'{i=} {left=} {right=}')
        # print(f'{increasing_height_from_left=}')
        # print(f'{increasing_height_from_right=}')
        return max_water
    
    # O(nlogn) - but fast enough to pass
    def maxArea_sort(self, height: List[int]) -> int:
        height_len = len(height)
        indexs = [i for i in range(height_len)]
        indexs.sort(key = lambda x : height[x])
        # print(f'{indexs=}')
        max_water = 0
        min_index, max_index = maxsize, -maxsize
        for i in range(height_len-1, -1, -1):
            t_i = indexs[i]
            min_index = min(min_index, t_i)
            max_index = max(max_index, t_i)
            if t_i<=min_index:
                max_water = max(max_water, height[t_i]*(max_index-t_i))
            elif t_i>=max_index:
                max_water = max(max_water, height[t_i]*(t_i-min_index))
            else:
                max_water = max(max_water, height[t_i]*(max_index-min_index))
        return max_water

    def maxArea(self, height: List[int]) -> int:
        height_len = len(height)
        max_area = 0
        i, j = 0, height_len-1
        while i<j:
            if height[i]<height[j]:
                max_area = max(max_area, height[i]*(j-i))
                i+=1
            elif height[i]>height[j]:
                max_area = max(max_area, height[j]*(j-i))
                j-=1
            else:
                max_area = max(max_area, height[j]*(j-i))
                j-=1
                i+=1
        return max_area