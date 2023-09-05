# https://leetcode.com/problems/can-place-flowers
"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
 However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1
 means not empty, and an integer n, return true if n new flowers can be planted in 
 the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        count = 0
        i = 0
        while i<flowerbed_len:
            if flowerbed[i]==1:
                i+=2
            else:
                if (i==0 or flowerbed[i]==0) and (i==(flowerbed_len-1) or flowerbed[i+1]==0):
                    count+=1
                    i+=2
                else:
                    i+=1
            if count>=n: return True
        return False