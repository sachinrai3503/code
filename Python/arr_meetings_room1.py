# https://leetcode.com/problems/meeting-rooms
# https://www.lintcode.com/problem/920
"""
Given an array of meeting time intervals consisting of start and end times [(s1,e1),(s2,e2),...] (si < ei), determine
 if a person could attend all meetings.

- 0≤intervals.length≤10^4
- intervals[i].length==2
- 0≤start_i<end_i≤10^6
- [(0,8), (8,10)] is not conflict at 8
 
Example
Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict
"""

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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        s, e = -1, -1
        for interval in intervals:
            ts, te = interval.start, interval.end
            if ts>=e:
                s, e = ts, te
            else:
                return False
        return True