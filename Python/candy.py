# https://leetcode.com/problems/candy
"""
There are n children standing in a line. Each child is assigned a rating value
 given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""

from sys import maxsize
from typing import List

class Solution:

    def get_smaller_count_to_right(self, ratings, ratings_len):
        count = list()
        prev = maxsize
        prev_count = 0
        for i in range(ratings_len-1, -1, -1):
            if ratings[i]>prev:
                count.insert(0, prev_count+1)
            else: count.insert(0, 0)
            prev = ratings[i]
            prev_count = count[0]
        # print(f'{count=}')
        return count

    def candy(self, ratings: List[int]) -> int:
        count = 0
        ratings_len = len(ratings)
        smaller_count = self.get_smaller_count_to_right(ratings, ratings_len)
        prev = -maxsize
        prev_count = 0
        for i in range(ratings_len):
            left = 1 if ratings[i]<=prev else prev_count+1
            right = smaller_count[i]+1
            t_count = max(left, right)
            count+=t_count
            prev = ratings[i]
            prev_count = t_count
        return count