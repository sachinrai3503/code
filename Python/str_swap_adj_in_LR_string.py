# https://leetcode.com/problems/swap-adjacent-in-lr-string
"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either 
 replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the 
 starting string start and the ending string result, return True if and only if there exists a sequence
 of moves to transform start to result.

Example 1:
Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
Output: true
Explanation: We can transform start to result following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:
Input: start = "X", result = "L"
Output: false

Constraints:
1 <= start.length <= 104
start.length == result.length
Both start and result will only consist of characters in 'L', 'R', and 'X'.
"""

# SAME AS - https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        s_len = len(start)
        r_len = len(result)
        i, j = 0, 0
        while i<s_len or j<r_len:
            while i<s_len and start[i]=='X':
                i+=1
            while j<r_len and result[j]=='X':
                j+=1
            if i<s_len and j<r_len and start[i]!=result[j]:
                return False
            elif i==s_len and j==r_len: return True
            elif i==s_len or j==r_len: return False
            elif (result[j]=='L' and i<j): return False
            elif (result[j]=='R' and i>j): return False
            else:
                i+=1
                j+=1
        return True