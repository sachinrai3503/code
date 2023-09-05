# https://leetcode.com/problems/russian-doll-envelopes
"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
 represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one
 envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
"""

from typing import List

class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        max_len = 0
        envelopes_len = len(envelopes)
        dp = [0 for i in range(envelopes_len)]
        envelopes.sort()
        # print(f'{envelopes=}')
        for i in range(envelopes_len-1, -1, -1):
            wi, hi = envelopes[i]
            t_len = 0
            for j in range(i+1, envelopes_len):
                if wi<envelopes[j][0] and hi<envelopes[j][1]:
                    t_len = max(t_len, dp[j])
            dp[i] = t_len+1
            max_len = max(max_len, dp[i])
        return max_len