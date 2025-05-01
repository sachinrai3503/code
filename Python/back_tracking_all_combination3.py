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

    def combinationSum3_1(self, k: int, n: int) -> List[List[int]]:
        arr = [None for i in range(k)]
        self.get_all_combinations(arr, k, n, 0, 1)
        return self.op
    
    def get_all_combination2(self, n, start_from, arr, k, i):
        # print(f'-- {n=} {start_from=} {arr=} {k=} {i=}')
        if n==0:
            self.op.append(list(arr))
            return False # Means no futher combination possible
        if i==k:
            return True if n>0 else False
        remaining_k = k - i
        min_possible = (remaining_k*(start_from + (start_from + remaining_k - 1)))//2
        max_possible = (remaining_k*(9 + (9 - remaining_k + 1)))//2
        # print(f'== {n=} {start_from=} {arr=} {k=} {i=} {min_possible=} {max_possible=}')
        if n<min_possible: return False
        if n>max_possible: return True
        for j in range(start_from, 10):
            arr[i] = j
            if not self.get_all_combination2(n-j, j+1, arr, k, i+1):
                break
        return True

    def combinationSum3_2(self, k: int, n: int) -> List[List[int]]:
        arr = [None for i in range(k)]
        if not self.get_all_combination2(n, 1, arr, k, 0):
            return []
        return self.op

    def get_combinations(self, n, i, k, cur_op, prev_sum, start_from):
        if i==k:
            if prev_sum==n:
                self.op.append(list(cur_op))
            return
        if (prev_sum+start_from)>n: return
        for j in range(start_from, 10):
            if (prev_sum+j)<=n:
                cur_op.append(j)
                self.get_combinations(n, i+1, k, cur_op, prev_sum+j, j+1)
                cur_op.pop()
            else:
                break

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.get_combinations(n, 0, k, [], 0, 1)
        return self.op