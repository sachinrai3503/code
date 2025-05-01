# https://www.lintcode.com/problem/919
# https://leetcode.com/problems/meeting-rooms-ii
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
 find the minimum number of conference rooms required.

Constraint -
- (0,8),(8,10) is not conflict at 8

Example
Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""

import heapq

from typing import (
    List,
)

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        count = 0
        l1 = []
        for interval in intervals:
            s, e = interval.start, interval.end
            heapq.heappush(l1, [s, 1])
            heapq.heappush(l1, [e, -1])
        # print(f'{l1=}')
        cur_count = 0
        while l1:
            _, room_count = heapq.heappop(l1)
            cur_count+=room_count
            count = max(count, cur_count)
        return count