# https://leetcode.com/problems/minimum-time-difference
"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between 
 any two time-points in the list.
 

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""

from sys import maxsize
from typing import List

class Solution:

    def __init__(self):
        self.mid_day = 720

    def to_minutes(self, time):
        hrs, _min = time.split(':')
        return int(hrs)*60 + int(_min)
    
    def compute_diff_in_minute(self, time1_min, time2_min):
        if (time1_min<=self.mid_day and time2_min<=self.mid_day) or \
            (time1_min>self.mid_day and time2_min>self.mid_day):
            return abs(time1_min - time2_min)
        else:
            clock_wise_diff = abs(time1_min - time2_min)
            if time1_min<time2_min : # am<pm
                anti_clock_wise_diff = (1440 - time2_min) + time1_min
            else:
                anti_clock_wise_diff = (1440 - time1_min) + time2_min
            return min(clock_wise_diff, anti_clock_wise_diff)

    def get_min_diff(self, time_list):
        min_diff = maxsize
        time_list_len = len(time_list)
        if not time_list or time_list_len<=1: return maxsize
        prev = time_list[0]
        for i in range(1, time_list_len):
            min_diff = min(min_diff, self.compute_diff_in_minute(prev, time_list[i]))
            prev = time_list[i]
        return min_diff

    # Will take more time
    def findMinDifference1(self, timePoints: List[str]) -> int:
        min_diff = maxsize
        timePoints = [self.to_minutes(_) for _ in timePoints]
        timePoints.sort()
        # print(f'{timePoints=}')
        min_diff = min(self.get_min_diff(timePoints), \
                            self.compute_diff_in_minute(timePoints[0], timePoints[-1]))
        return min_diff
    
    # Uses bucket sort as per editorial but looks more like counting sort
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_diff = maxsize
        buckets = [False for i in range(60*24)]
        first_time, last_time = maxsize, -maxsize
        for time in timePoints:
            time_min = self.to_minutes(time)
            first_time = min(first_time, time_min)
            last_time = max(last_time, time_min)
            if buckets[time_min]: return 0
            buckets[time_min] = True
        min_diff = self.compute_diff_in_minute(first_time, last_time)
        # print(f'{first_time=} {last_time=} {min_diff=}\n{buckets=}')
        prev = None
        for i in range(24*60):
            if buckets[i]:
                if prev:
                    min_diff = min(min_diff, self.compute_diff_in_minute(prev, i))
                prev = i
        return min_diff