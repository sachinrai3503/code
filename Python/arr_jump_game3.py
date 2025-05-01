# https://leetcode.com/problems/jump-game-iii
"""
Given an array of non-negative integers arr, you are initially positioned at 
 start index of the array. When you are at index i, you can jump to i + arr[i] 
 or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

Constraints:
1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
"""

from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        arr_len = len(arr)
        que = deque()
        visited = set()
        que.append(start)
        visited.add(start)
        while que:
            t = que.popleft()
            if arr[t]==0: return True
            l, r = t-arr[t], t+arr[t]
            if l>=0 and l not in visited:
                que.append(l)
                visited.add(l)
            if r<arr_len and r not in visited:
                que.append(r)
                visited.add(r)
        return False