# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time
"""
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is 
 between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. 
You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.

Example 1:
Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer
 than 3 operations.

Example 2:
Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of
 operations needed is 1.

Constraints:
current and correct are in the format "HH:MM"
current <= correct
"""
class Solution:
    
    def get_minutes(self, time):
        time = time.split(':')
        minutes = 60*int(time[0]) + int(time[1])
        return minutes
    
    def convertTime(self, current: str, correct: str) -> int:
        minutes_cur = self.get_minutes(current)
        minutes_cor = self.get_minutes(correct)
        diff = minutes_cor - minutes_cur
        op = 0
        op+=(diff//60)
        diff%=60
        op+=(diff//15)
        diff%=15
        op+=(diff//5)
        diff%=5
        op+=diff
        return op