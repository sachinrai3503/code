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

class Solution:
    def maxArea_sort(self, height: list[int]) -> int:
        max_area = 0
        height_len = len(height)
        indexs = [i for i in range(height_len)]
        indexs.sort(key = lambda x : height[x])
        # print(indexs)
        most_right_greater, most_left_greater = indexs[-1], indexs[-1]
        for i in range(height_len-2, -1, -1):
            t_area = 0
            if most_left_greater<indexs[i]<most_right_greater:
                t_area = height[indexs[i]]*(most_right_greater-most_left_greater)
            elif indexs[i]<most_left_greater:
                t_area = height[indexs[i]]*(most_right_greater-indexs[i])
            else:
                t_area = height[indexs[i]]*(indexs[i]-most_left_greater)
            max_area = max(max_area, t_area)
            # print(f'{i=} {t_area=} {most_right_greater=} {most_left_greater=}')
            most_right_greater = max(most_right_greater, indexs[i])
            most_left_greater = min(most_left_greater, indexs[i])
        return max_area
    
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        height_len = len(height)
        i, j = 0, height_len-1
        while i<j:
            t_area = 0
            if height[i]<height[j]:
                t_area = height[i]*(j-i)
                i+=1
            elif height[i]>height[j]:
                t_area = height[j]*(j-i)
                j-=1
            else:
                t_area =  height[j]*(j-i)
                i+=1
                j-=1
            max_area = max(max_area, t_area)
        return max_area