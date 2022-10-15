# https://www.lintcode.com/problem/1817
# https://leetcode.com/problems/divide-chocolate

"""
You have one chocolate bar that consists of some chunks. Each chunk has its
 own sweetness given by the array sweetness.

You're going to share this chocolate with K friends, so you need to cut K 
 times to get K + 1 pieces, each of which is made up of a series of small pieces.

Being generous, you will eat the piece with the minimum total sweetness and
 give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]

Constraints:
0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
"""

from typing import (
    List,
)

from sys import maxsize

class Solution:

    def get_info(self, sweetness, sweetness_len):
        _min, total_sum = maxsize, 0
        for num in sweetness:
            _min = min(_min, num)
            total_sum+=num
        return _min, total_sum
    
    """
    Checks if the arr can be split into m subarrs such that sum for all subarr >=k
    t_m==m returns True
    t_m>m  returns True
    t_m<m  returns False
    """
    def is_min_k_sweetness_possible(self, sweetness, sweetness_len, m, k):
        t_m = 0
        i, t_sum = 0, 0
        while i<sweetness_len:
            t_sum+=sweetness[i]
            if t_sum>=k:
                t_m+=1
                if t_m==m: return True
                t_sum = 0
            i+=1
        return False # arr can't be split into m subarr with min_sum >= k
    
    """
    @param sweetness: an integer array
    @param k: an integer
    @return:  return the maximum total sweetness of the piece
    """
    def maximize_sweetness(self, sweetness: List[int], k: int) -> int:
        sweetness_len = len(sweetness)
        m = k+1
        s, e = self.get_info(sweetness, sweetness_len)
        while s<=e:
            mid = s + (e-s)//2
            is_possible = self.is_min_k_sweetness_possible(sweetness, sweetness_len, m, mid)
            if is_possible:
                s = mid+1
            else:
                e = mid-1
        return e