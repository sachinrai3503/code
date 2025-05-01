# https://leetcode.com/problems/largest-time-for-given-digits
"""
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest
 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

Example 1:
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43",
 "23:14", and "23:41". Of these times, "23:41" is the latest.

Example 2:
Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
 
Constraints:
arr.length == 4
0 <= arr[i] <= 9
"""

from typing import List

class Solution:

    def get_max_hr(self, counts):
        hr = [None, None]
        if counts[2]:
            hr[0] = '2'
            counts[2]-=1
            i=3
            while i>=0:
                if counts[i]:
                    hr[1] = chr(i+48)
                    counts[i]-=1
                    return hr
                i-=1
        elif counts[1] or counts[0]:
            hr[0] = '1' if counts[1] else '0'
            counts[ord(hr[0])-48]-=1
            i = 9
            while i>=0:
                if counts[i]:
                    hr[1] = chr(i+48)
                    counts[i]-=1
                    return hr
                i-=1
        return None, None

    def get_max_min(self, counts):
        min = [None, None]
        i=5
        while i>=0:
            if counts[i]:
                min[0] = chr(i+48)
                counts[i]-=1
                break
            i-=1
        i = 9
        while i>=0:
            if counts[i]:
                min[1] = chr(i+48)
                counts[i]-=1
                break
            i-=1
        return min

    # This will fail for [9,9,2,1]
    def largestTimeFromDigits1(self, arr: List[int]) -> str:
        counts = [0 for i in range(10)]
        for num in arr:
            counts[num]+=1
        print(f'{counts=}')
        time = [None, None, ':', None, None]
        time[0], time[1] = self.get_max_hr(counts)
        print(f'{time=}')
        if time[0] is None or time[1] is None: return '' 
        time[3], time[4] = self.get_max_min(counts)
        print(f'{time=}')
        if time[3] is None or time[4] is None: return '' 
        return ''.join(time)
    
    def generate_largest_time(self, op, i, counts, start_from):
        if i==2: return self.generate_largest_time(op, i+1, counts, start_from)
        if i==5: return True
        j = start_from[i]
        if i==1 and op[0]=='2':
            j = 3
        while j>=0:
            if counts[j]>0:
                op[i] = chr(j+48)
                counts[j]-=1
                if self.generate_largest_time(op, i+1, counts, start_from):
                    return True
                counts[j]+=1
            j-=1
        return False

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        counts = [0 for i in range(10)]
        for num in arr:
            counts[num]+=1
        # print(f'{counts=}')
        start_from = [2, 9, -1, 5, 9]
        op = [None, None, ':', None, None]
        if self.generate_largest_time(op, 0, counts, start_from):
            return ''.join(op)
        return ''