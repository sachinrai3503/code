# https://www.geeksforgeeks.org/count-paths-whose-sum-is-not-divisible-by-k-in-given-matrix
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k
"""
You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently
 at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k.
 Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
Output: 2
Explanation: There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.

Example 2:
Input: grid = [[0,0]], k = 5
Output: 1
Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.

Example 3:
Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
Output: 10
Explanation: Every integer is divisible by 1 so the sum of the elements on every possible
 path is divisible by k.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 5 * 104
1 <= m * n <= 5 * 104
0 <= grid[i][j] <= 100
1 <= k <= 50
"""

from typing import List

class Solution:
    
    def gcd(self, a, b):
        if b==0: return a
        return self.gcd(b, a%b)
    
    def rotate_right_by_k(self, arr, arr_len, k):
        _gcd = self.gcd(arr_len, k)
        for i in range(_gcd):
            temp = arr[i]
            next_i = (i+k)%arr_len
            while next_i!=i:
                temp2 = arr[next_i]
                arr[next_i] = temp
                temp = temp2
                next_i = (next_i+k)%arr_len
            arr[next_i] = temp
    
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = 0 if m==0 else len(grid[0])
        dp = [[0 for i in range(k)] for j in range(n)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                rem = grid[i][j]%k
                self.rotate_right_by_k(dp[j], k, rem)
                if (j+1)<n:
                    for t_k in range(k):
                        dp[j][(rem+t_k)%k] = (dp[j][(rem+t_k)%k] + dp[j+1][t_k])%1000000007
                if i==m-1 and j==n-1:
                    dp[j][rem]=1
            # print(dp)
        return dp[0][0]