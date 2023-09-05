# https://www.geeksforgeeks.org/tile-stacking-problem
"""
A stable tower of height n is a tower consisting of exactly n tiles of unit height
 stacked vertically in such a way, that no bigger tile is placed on a smaller tile.

We have an infinite number of tiles of sizes 1, 2, …, m. The task is to calculate 
 the number of the different stable towers of height n that can be built from these
 tiles, with a restriction that you can use at most k tiles of each size in the tower.

 Note: Two towers of height n are different if and only if there exists a 
       height h (1 <= h <= n), such that the towers have tiles of different sizes at height h.

Examples: 
Input : n = 3, m = 3, k = 1.
Output : 1
Possible sequences: { 1, 2, 3}. 
Hence answer is 1.

Input : n = 3, m = 3, k = 2.
Output : 7
{1, 1, 2}, {1, 1, 3}, {1, 2, 2},
{1, 2, 3}, {1, 3, 3}, {2, 2, 3}, 
{2, 3, 3}.
"""

def count_ways(n, m, k):
    dp = [[0 for j in range(2)] for i in range(n+1)]
    dp[0][0], dp[0][1] = 1, 1 # ways to make 0 height
    for i in range(m, 0, -1):
        cur_col = i%2
        prev_col = 0 if cur_col==1 else 1
        t_sum = dp[0][prev_col]
        for j in range(1, n+1):
            dp[j][cur_col]= dp[j][prev_col] + t_sum
            t_sum+=dp[j][prev_col]
            if (j-k)>=0:
                t_sum-=dp[j-k][prev_col]
        print(dp)
    return dp[n][1]

def main():
    n, m, k = 8, 5, 5
    print(count_ways(n, m, k))

if __name__ == '__main__':
    main()