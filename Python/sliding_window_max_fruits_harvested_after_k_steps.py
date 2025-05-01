# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps
"""
Fruits are available at some positions on an infinite x-axis. You are given 
 a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts 
 amounti fruits at the position positioni. fruits is already sorted by positioni
 in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at
 the position startPos. From any position, you can either walk to the 
 left or right. It takes one step to move one unit on the x-axis, and you can 
 walk at most k steps in total. For every position you reach, you harvest all 
 the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.

Example 1:
Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
Output: 9
Explanation: 
The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.

Example 2:
Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
Output: 14
Explanation: 
You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.

Example 3:
Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
Output: 0
Explanation:
You can move at most k = 2 steps and cannot reach any position with fruits.

Constraints:
1 <= fruits.length <= 105
fruits[i].length == 2
0 <= startPos, positioni <= 2 * 105
positioni-1 < positioni for any i > 0 (0-indexed)
1 <= amounti <= 104
0 <= k <= 2 * 105
"""

from typing import List

class Solution:

    def get_ceil_index(self, arr, arr_len, k):
        _ceil = arr_len
        s, e = 0, arr_len-1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid][0]>=k:
                _ceil = mid
                e = mid-1
            else:
                s = mid+1
        return _ceil
    
    def get_floor_index(self, arr, arr_len, k):
        _floor = -1
        s, e = 0, arr_len-1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid][0]<=k:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor

    def get_max_fruits_starting_from_left(self, arr, arr_len, left_end, start_pos, k):
        max_fruits = 0
        t_fruits = 0
        s, e = left_end, left_end-1
        while s<arr_len and arr[s][0]<=start_pos:
            left_step = start_pos-arr[s][0]
            right_step = k - 2*left_step
            max_reach = start_pos + (0 if right_step<0 else right_step)
            # print(f'LL {s=} {e=} {t_fruits=} {max_fruits=} {left_step=} {right_step=} {max_reach=}')
            while (e+1)<arr_len and arr[e+1][0]<=max_reach:
                t_fruits+=arr[e+1][1]
                e+=1
            max_fruits = max(max_fruits, t_fruits)
            t_fruits-=arr[s][1]
            s+=1
        # print(f'{max_fruits=}')
        return max_fruits

    def get_max_fruits_starting_from_right(self, arr, arr_len, right_end, start_pos, k):
        max_fruits = 0
        t_fruits = 0
        s, e = right_end, right_end+1
        while s>=0 and arr[s][0]>=start_pos: # will move from right to left
            right_step = arr[s][0] - start_pos
            left_step = k - 2*right_step
            max_reach = start_pos - (0 if left_step<0 else left_step)
            # print(f'RR {s=} {e=} {t_fruits=} {max_fruits=} {left_step=} {right_step=} {max_reach=}')
            while (e-1)>=0 and arr[e-1][0]>=max_reach:
                t_fruits+=arr[e-1][1]
                e-=1
            max_fruits = max(max_fruits, t_fruits)
            t_fruits-=arr[s][1]
            s-=1
        # print(f'{max_fruits=}')
        return max_fruits

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fruits_len = len(fruits)
        left_start = self.get_ceil_index(fruits, fruits_len, startPos-k)
        right_start = self.get_floor_index(fruits, fruits_len, startPos+k)
        # print(f'{left_start=} {right_start=}')
        return max(
            self.get_max_fruits_starting_from_left(fruits, fruits_len, left_start, startPos, k),
            self.get_max_fruits_starting_from_right(fruits, fruits_len, right_start, startPos, k)
        )