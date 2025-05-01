# https://leetcode.com/problems/allocate-mailboxes
"""
Given the array houses where houses[i] is the location of the ith house along a street and an
 integer k, allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 

Example 2:
Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

Constraints:
1 <= k <= houses.length <= 100
1 <= houses[i] <= 104
All the integers of houses are unique.
"""

from sys import maxsize
from typing import List

class MailboxPosInfo:
    def __init__(self, cur_pos, cur_dist, houses_on_left, houses_on_right):
        self.cur_pos = cur_pos
        self.cur_dist = cur_dist
        self.houses_on_left = houses_on_left
        self.houses_on_right = houses_on_right
    
class Solution:

    def get_best_position_for_mailbox(self, arr, s, e, cur_pos_info : MailboxPosInfo) -> MailboxPosInfo:
        count = e-s+1
        mid = s + (e-s)//2
        house_on_left = (mid-s+1)
        house_on_right = count - house_on_left
        next_pos = arr[mid]
        if (count&1)==0:
            next_pos = (arr[mid] + arr[mid+1])//2
        diff = next_pos - cur_pos_info.cur_pos
        next_dist = (cur_pos_info.cur_dist + diff*cur_pos_info.houses_on_left - diff*cur_pos_info.houses_on_right) + \
                        (arr[e] - next_pos)
        return MailboxPosInfo(next_pos, next_dist, house_on_left, house_on_right)

    def minDistance(self, houses: List[int], k: int) -> int:
        houses_count = len(houses)
        houses.sort()
        dp = [[maxsize for j in range(houses_count)] for i in range(2)]
        for tk in range(1, k+1):
            cur_row = tk%2
            prev_row = 0 if cur_row==1 else 1
            for i in range(houses_count-1, -1, -1):
                min_dist = maxsize
                cur_best_pos = MailboxPosInfo(0, 0, 0, 0)
                for j in range(i, houses_count):
                    next_best_pos = self.get_best_position_for_mailbox(houses, i, j, cur_best_pos)
                    min_dist_to_right = 0 if j==(houses_count-1) else dp[prev_row][j+1]
                    t_dist = maxsize if min_dist_to_right==maxsize else (next_best_pos.cur_dist + min_dist_to_right)
                    if t_dist<min_dist:
                        min_dist = t_dist
                    cur_best_pos = next_best_pos
                dp[cur_row][i] = min_dist
                print(f'{dp[cur_row]=}')
        return dp[k%2][0]