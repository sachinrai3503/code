# https://leetcode.com/problems/unique-number-of-occurrences
"""
Given an array of integers arr, return true if the number of occurrences of each
 value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
 have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        counter = Counter(arr)
        count_map = [0 for i in range(arr_len+1)]
        # print(f'{counter=} {type(counter)=}')
        for count in counter.values():
            if count_map[count]!=0: return False
            count_map[count] = count
        return True