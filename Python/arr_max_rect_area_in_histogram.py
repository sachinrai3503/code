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
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights_len = len(heights)
        max_area = 0
        stck = list() # has indexs
        area = list()
        for i in range(heights_len):
            area.append(0)
            cur_height = heights[i]
            while stck and heights[stck[-1]]>cur_height:
                temp = stck.pop()
                prev_smaller = -1 if not stck else stck[-1]
                area[temp] =(heights[temp]*(i-prev_smaller-1))
                max_area = max(max_area, area[temp])
            stck.append(i)
        #     print(stck)
        # print(area)
        while stck:
            temp = stck.pop()
            prev_smaller = -1 if not stck else stck[-1]
            area[temp]+=(heights[temp]*(heights_len-prev_smaller-1))
            max_area = max(max_area, area[temp])
        return max_area