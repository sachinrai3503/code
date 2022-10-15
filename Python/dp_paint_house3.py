# https://leetcode.com/problems/paint-house-iii
"""
There is a row of m houses in a small city, each house must be painted with
 one of the n colors (labeled from 1 to n), some houses that have been painted
 last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with
 the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:
	houses[i]: is the color of the house i, and 0 if the house is not painted yet.
	cost[i][j]: is the cost of paint the house i with the color j + 1.

Return the minimum cost of painting all the remaining houses in such a way that
 there are exactly target neighborhoods. If it is not possible, return -1.

Example 1:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:
Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:
Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] 
 different of target = 3.
 
Constraints:
m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 104
"""

from sys import maxsize

class Solution:
    
    def print_mat(dp):
        row = len(dp)
        col = 0 if not row else len(dp[0])
        for i in range(row):
            for j in range(col):
                if dp[i][j]==maxsize: print('M', end = '\t')
                else: print(dp[i][j], end = '\t')
            print()
        print()
    
    def get_target_limit(self, houses, m):
        target_limit = list()
        island_count = 0
        prev = maxsize
        for i in range(m-1, -1, -1):
            if houses[i]!=0 and houses[i]!=prev:
                island_count+=1
                prev = houses[i]
            target_limit.insert(0, (island_count,m-i)) # (min, max)
        # print(f'{target_limit=}')
        return target_limit
    
    """
    m = houses, n = colour, t = (t-1)th target, 
    """
    def get_min_cost(self, dp, m, n, cur_house, ignore_colour, t):
        if t==0: return 0 if cur_house==m else maxsize
        if t>(m-cur_house): return maxsize
        min_cost = maxsize
        for i in range(n):
            if i==ignore_colour: continue
            min_cost = min(min_cost, dp[i][cur_house])
        return min_cost
    
    """
    m = houses, n = colour, t = (t-1)th target, 
    """
    def get_min_cost1(self, dp, m, n, cur_house, ignore_colour, t):
        if t==0: return 0 if cur_house==m else maxsize
        if t>(m-cur_house): return maxsize
        return dp[ignore_colour][cur_house]
    
    # O(Target*M*N*M)
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # return 0
        target_limit = self.get_target_limit(houses, m)
        dp = [[[0 for j in range(m)] for i in range(n)] for k in range(2)]
        for t in range(1, target+1):
            cur_mat = t%2
            prev_mat = 0 if cur_mat==1 else 1
            for t_m in range(m-t, -1, -1):
                min_cost = list() # min_cost[i] = min(min_cost[i], min_cost[i+1])
                prev = maxsize
                for t_n in range(n-1, -1, -1):
                    if not target_limit[t_m][0]<=t<=target_limit[t_m][1]: dp[cur_mat][t_n][t_m] = maxsize
                    elif houses[t_m]!=0:
                        if (t_n+1)!=houses[t_m]: dp[cur_mat][t_n][t_m] = maxsize
                        else:
                            t_cost = maxsize
                            t_sum = 0
                            i = t_m
                            while i<m and (houses[i]==(t_n+1) or houses[i]==0) and t<=(m-i):
                                t_sum+=(cost[i][t_n] if houses[i]==0 else 0)
                                t_cost = min(t_cost, t_sum + self.get_min_cost1(dp[prev_mat], m, n, i+1, t_n, t-1))
                                i+=1
                            dp[cur_mat][t_n][t_m] = t_cost
                    else:
                        t_cost = maxsize
                        t_sum = 0
                        i = t_m
                        while i<m and (houses[i]==0 or houses[i]==(t_n+1)) and t<=(m-i):
                            t_sum+=(cost[i][t_n] if houses[i]==0 else 0)
                            t_cost = min(t_cost, t_sum + self.get_min_cost1(dp[prev_mat], m, n, i+1, t_n, t-1))
                            i+=1
                        dp[cur_mat][t_n][t_m] = t_cost
                    min_cost.insert(0, min(prev, dp[cur_mat][t_n][t_m]))
                    prev = min_cost[0]
                # print(f'{t_m=} {t_n=} {min_cost=}')
                up = maxsize
                # updating the dp[cur_mat][i][t_m] with min cost to paint t_m house with colour!=i
                for t_n in range(n):
                    cur = dp[cur_mat][t_n][t_m]
                    down = min_cost[t_n+1] if t_n!=(n-1) else maxsize
                    dp[cur_mat][t_n][t_m] = min(up, down)
                    up = min(up, cur)
            # Solution.print_mat(dp[cur_mat])
        op = maxsize
        for i in range(n-1, -1, -1):
            op = min(op, dp[target%2][i][0])
        return op if op!=maxsize else -1