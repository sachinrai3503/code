# https://leetcode.com/problems/max-points-on-a-line
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
 return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""

from sys import maxsize
from collections import Counter
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        line_count = 0
        points_len = len(points)
        for i in range(points_len):
            x1, y1 = points[i][0], points[i][1]
            slope_count = Counter() # {m1:count_of_points, ...}
            for j in range(i+1, points_len):
                x2_x1 = points[j][0]-x1
                if x2_x1!=0:
                    ij_slope = (points[j][1]-y1)/x2_x1
                else:
                    ij_slope = maxsize
                slope_count[ij_slope]+=1
                if line_count<slope_count[ij_slope]:
                    line_count = max(line_count, slope_count[ij_slope])
            # print(f'{slope_count=}')
        return line_count+1