# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
"""
You are given two strings s1 and s2 of equal length consisting of letters 
 "x" and "y" only. Your task is to make these two strings equal to each other.

You can swap any two characters that belong to different strings,
 which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal,
 or return -1 if it is impossible to do so.

Example 1:
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2: 
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we 
 can only swap chars in different strings.

Example 3:
Input: s1 = "xx", s2 = "xy"
Output: -1

Example 4:
Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4

Constraints:
1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Keeping count of corresponding diff. in s1 and s2.
        # Here x_count means s1[i]==x and s2[i]==y
        # Here y_count means s1[i]==y and s2[i]==x
        x_count, y_count = 0, 0
        i = len(s1) -1
        while i>=0:
            if s1[i]!=s2[i]:
                if s1[i]=='x': x_count+=1
                elif s1[i]=='y': y_count+=1
            i-=1
        count = (x_count//2) + (y_count//2)
        rem1, rem2 = (x_count%2), (y_count%2)
        if rem1==0 and rem2==0: return count
        elif rem1==1 and rem2==1: return count+2
        else: return -1