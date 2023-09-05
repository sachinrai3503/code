# https://leetcode.com/problems/maximum-height-by-stacking-cuboids
# https://www.geeksforgeeks.org/box-stacking-problem-dp-22
"""
Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] 
 (0-indexed). Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj 
 and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating 
 it to put it on another cuboid.

Return the maximum height of the stacked cuboids.

Example 1:
Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190
Explanation:
Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.

Example 2:
Input: cuboids = [[38,25,45],[76,35,3]]
Output: 76
Explanation:
You can't place any of the cuboids on the other.
We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.

Example 3:
Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
Output: 102
Explanation:
After rearranging the cuboids, you can see that all cuboids have the same dimension.
You can place the 11x7 side down on all cuboids so their heights are 17.
The maximum height of stacked cuboids is 6 * 17 = 102.
 
Constraints:
n == cuboids.length
1 <= n <= 100
1 <= widthi, lengthi, heighti <= 100
"""

from typing import List

class Solution:
    
    def is_small(self, dim1, dim2):
        if dim1[0]<=dim2[0] and dim1[1]<=dim2[1] and dim1[2]<=dim2[2]: return True
        return False
    
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        max_len = 0
        cuboids_len = len(cuboids)
        dimensions = list()
        for i in range(cuboids_len):
            w, l, h = cuboids[i]
            dimensions.append(((min(w,l), max(w,l), h), i))
            dimensions.append(((min(w,h), max(w,h), l), i))
            dimensions.append(((min(l,h), max(l,h), w), i))
        dimensions.sort()
        dimensions_len = len(dimensions)
        dp = [0 for i in range(dimensions_len)]
        for i in range(dimensions_len-1, -1, -1):
            t_height = 0
            dimension_i, dimension_i_index = dimensions[i]
            for j in range(i+1, dimensions_len):
                if dimensions[j][1]!=dimension_i_index and self.is_small(dimension_i, dimensions[j][0]):
                    t_height = max(t_height, dp[j])
            dp[i] = dimension_i[2] + t_height
            max_len = max(max_len, dp[i])
        return max_len