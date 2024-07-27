# https://leetcode.com/problems/koko-eating-bananas
"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has 
 piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
 some pile of bananas and eats k bananas from that pile. If the pile has less
 than k bananas, she eats all of them instead and will not eat any more bananas
 during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas
 before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

from sys import maxsize
from typing import List

class Solution:

    def can_eat_all_banana(self, piles, piles_count, h, k):
        hrs_taken = 0
        for i in range(piles_count):
            hrs_taken+=((piles[i]//k) + (1 if piles[i]%k!=0 else 0))
            if hrs_taken>h: return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = maxsize
        piles_len = len(piles)
        s, e = 1, max(piles)
        while s<=e:
            mid = s + (e-s)//2
            # print(f'{s=} {e=} {mid=}')
            if self.can_eat_all_banana(piles, piles_len, h, mid):
                min_speed = mid
                e = mid-1
            else:
                s = mid+1
        return min_speed