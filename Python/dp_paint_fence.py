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

from collections import deque

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
	# m = no of adjacent fence having same colour
	# f(1) = k
	# f(i) = k*f(i-1) :: for 2<=i<=m
	# f(i) = k*f(i-1) - k :: for i==(m+1)
	# f(i) = k*f(i-1) - k(f(i-3) - f(i-3)/k) => k*f(i-1) - (k-1)f(i-3) :: for i>(m+1)
    def num_ways(self, n: int, k: int) -> int:
        que = deque()
        m = 2
        for i in range(1, n+1):
            if i<=m:
                val = k if i==1 else k*que[-1]
                que.append(val)
            elif i==m+1:
                val = k*que[-1] - k
                que.append(val)
            else:
                val = k*que[-1] - (k-1)*que.popleft()
                que.append(val)
            # print(que)
        return que[-1]