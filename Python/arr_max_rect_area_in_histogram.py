# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/
# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""
Given an array of integers heights representing the histogram's bar height where
 the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution:

    def get_prev_smaller_index(self, heights, length):
        smaller_indexs = [-1 for i in range(length)]
        stck = list()
        for i in range(length-1, -1, -1):
            while len(stck)>0 and heights[stck[-1]]>heights[i]:
                smaller_indexs[stck.pop()] = i
            stck.append(i)
        while len(stck)>0:
            smaller_indexs[stck.pop()] = -1
        return smaller_indexs
    
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        length = len(heights)
        smaller_indexs = self.get_prev_smaller_index(heights, length)
        # print(smaller_indexs)
        stck = list()
        for i in range(length):
            while len(stck)>0 and heights[stck[-1]]>heights[i]:
                cur_index = stck.pop()
                t_area =  (i-smaller_indexs[cur_index]-1)*heights[cur_index]
                max_area = max(t_area, max_area)
            stck.append(i)
        while len(stck)>0:
            cur_index = stck.pop()
            t_area =  (length-smaller_indexs[cur_index]-1)*heights[cur_index]
            max_area = max(t_area, max_area)
        return max_area