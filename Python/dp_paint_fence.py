# https://www.geeksforgeeks.org/painting-fence-algorithm
# https://leetcode.com/problems/paint-fence
# https://www.lintcode.com/problem/514
"""
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts
  have the same color. Return the total number of ways you can paint the fence.

n and k are non-negative integers.

Example 1:
Input: n=3, k=2  
Output: 6

Example 2:
Input: n=2, k=2  
Output: 4
"""

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        if n==0 or k==0: return 0
        total, same, diff = 0, 0, 0
        for i in range(1, n+1):
            if i==1:
                same, diff, total = 0, k, k
            else:
                same = diff
                diff = total*(k-1)
                total = same+diff
        return total