# https://leetcode.com/problems/last-stone-weight-ii
"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones
 have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 100
"""

from sys import maxsize
from typing import List

class Solution:

    def find_last_stone_weight(self, stones, stones_len, remaining_stones, stones_sum):
        # print(f'{stones=} {remaining_stones=} {stones_sum=}')
        if remaining_stones<=1: return stones_sum
        min_weight = maxsize
        for i in range(stones_len):
            x = stones[i]
            if x!=None:
                stones[i] = None
                for j in range(i+1, stones_len):
                    y = stones[j]
                    if y!=None:
                        stones[j] = None
                        lost = 2
                        z = abs(y-x)
                        if z:
                            stones[j] = z
                            lost = 1
                        t_stones_sum = stones_sum - x - y + z
                        min_weight = min(min_weight, self.find_last_stone_weight(stones, stones_len, remaining_stones-lost, t_stones_sum))
                        stones[j] = y
                stones[i] = x
        return min_weight

    # This will time out
    def lastStoneWeightII_rec(self, stones: List[int]) -> int:
        stones_len = len(stones)
        stones_sum = sum(stones)
        return self.find_last_stone_weight(stones, stones_len, stones_len, stones_sum)

    # This will not work for [31,26,33,21,40]. Exp op = 5, actual op = 9
    # sequence = (26 - (33-21)) - (40-31) = 5
    def lastStoneWeightII_2(self, stones: List[int]) -> int:
        stones_len = len(stones)
        dp_len = 1<<stones_len
        dp = [maxsize for i in range(dp_len)]
        dp[0] = 0
        for i in range(dp_len):
            print(f'{i=} {dp=}')
            if dp[i] is maxsize: continue
            x = dp[i]
            for j in range(stones_len):
                if i&(1<<j)==0:
                    y = stones[j]
                    z = y
                    if x!=0:
                        z = abs(x-y)
                    dp[i|(1<<j)] = min(dp[i|(1<<j)], z)
        return dp[-1]

    # stones = [a,b,c].
    # Possible sequences = (a-b)-c = a - (b+c)
    #                    = a-(b-c) = (a+c) - b
    #                    = (a-c)-b = a - (b+c) same as 1st
    # So, it can be seen that question is to divide the arr in 2 sets
    # such that their sum is near/equal to each other.
    # Eg. For 2nd testcase = (26 - (33-21)) - (40-31) = (26+31+21) - (40+33) = 5
    def lastStoneWeightII_BitWiseDP(self, stones, stones_len, stones_sum) -> int:
        op = maxsize
        dp_len = 1<<stones_len
        dp = [maxsize for i in range(dp_len)]
        dp[0] = 0
        for i in range(dp_len):
            # print(f'{i=} {dp=}')
            if dp[i] is maxsize: continue
            for j in range(stones_len):
                if i&(1<<j)==0:
                    t_sum = dp[i] + stones[j]
                    dp[i|(1<<j)] = t_sum
                    op = min(op, abs(stones_sum-(2*t_sum)))
        return op

    # stones = [a,b,c].
    # Possible sequences = (a-b)-c = a - (b+c)
    #                    = a-(b-c) = (a+c) - b
    #                    = (a-c)-b = a - (b+c) same as 1st
    # So, it can be seen that question is to divide the arr in 2 sets
    # such that their sum is near/equal to each other.
    # Eg. For 2nd testcase = (26 - (33-21)) - (40-31) = (26+31+21) - (40+33) = 5
    def lastStoneWeightII_DP(self, stones, stones_len, stones_sum) -> int:
        mid = (stones_sum//2)+1
        dp = [False for i in range(mid)]
        max_subset_sum = -1
        for i in range(stones_len):
            stone_i = stones[i]
            # print(f'{i=} {stone_i=} {dp=}')
            for j in range(mid-1, stone_i-1, -1):
                if j==stone_i:
                    dp[j] = True
                    max_subset_sum = max(max_subset_sum, j)
                elif dp[j-stone_i]:
                    dp[j] = True
                    max_subset_sum = max(max_subset_sum, j)
        return stones_sum-(2*max_subset_sum)
    
    def lastStoneWeightII_3(self, stones: List[int]) -> int:
        stones_len = len(stones)
        stones_sum = sum(stones)
        if ((stones_sum//2)+1)<(1<<stones_len):
            return self.lastStoneWeightII_DP(stones, stones_len, stones_sum)
        else:
            return self.lastStoneWeightII_BitWiseDP(stones, stones_len, stones_sum)
    
    # this is slower than lastStoneWeightII_3
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_len = len(stones)
        half_len = stones_len//2
        stones_sum = sum(stones)
        op = stones_sum
        dp = [set() for i in range(half_len+1)]
        dp[0].add(0)
        for stone in stones:
            for i in range(half_len, 0, -1):
                for t_sum in dp[i-1]:
                    subset1_sum = t_sum+stone
                    dp[i].add(subset1_sum)
                    op = min(op, abs(stones_sum-(2*subset1_sum)))
        # print(f'{dp=}')
        return op