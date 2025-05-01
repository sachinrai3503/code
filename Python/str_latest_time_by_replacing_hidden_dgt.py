# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits
"""
You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).
The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

Example 2:
Input: time = "0?:3?"
Output: "09:39"

Example 3:
Input: time = "1?:22"
Output: "19:22"
 
Constraints:
time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
"""

class Solution:
    def maximumTime(self, time: str) -> str:
        s = list(time)
        if s[3]=='?':
            s[3] = '5'
        if s[4]=='?':
            s[4] = '9'
        if s[0]=='?' and s[1]=='?':
            s[0], s[1] = '2', '3'
        elif s[1]=='?':
            if s[0]=='2':
                s[1] = '3'
            else:
                s[1] = '9'
        elif s[0]=='?':
            if s[1] in '0123':
                s[0] = '2'
            else:
                s[0] = '1'
        return ''.join(s)