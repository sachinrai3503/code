# https://leetcode.com/problems/combination-sum-iii
"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
 Only numbers 1 through 9 are used.
 Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the 
 combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1,
 there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

from typing import List

class Solution:

    def __init__(self):
        self.op = list()

    def get_all_combinations(self, arr, k, n, current_index, start_from):
        if current_index==k:
            if n==0:
                self.op.append(list(arr))
            return
        remaining_numbers = k-current_index
        end_at = n
        if remaining_numbers != 1:
            end_at = (n//remaining_numbers) - (1 if (n%remaining_numbers)==0 else 0)
        end_at = min(end_at, 9)
        # print(f'{arr=} {k=} {n=} {current_index=} {start_from=} {end_at=}')
        for num in range(start_from, end_at+1):
            # print(f'{current_index=}')
            arr[current_index] = num
            self.get_all_combinations(arr, k, n-num, current_index+1, num+1)
            arr[current_index] = None
        return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [None for i in range(k)]
        self.get_all_combinations(arr, k, n, 0, 1)
        return self.op