# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string
"""
Given a parentheses string s containing only the characters '(' and ')'. A parentheses
 string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. 
 We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Constraints:
1 <= s.length <= 105
s consists of '(' and ')' only.
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        stck = list() # [ ['(', 0], ..]
        for char in s:
            if char=='(':
                if stck and stck[-1][1]!=0: # half closed (
                    count+=1
                    stck.pop()
                stck.append(['(', 0])
            else:
                if not stck:
                    count+=1
                    stck.append(['(', 0])
                stck[-1][1]+=1
                if stck[-1][1]==2:
                    stck.pop()
        while stck:
            count+=(2-stck.pop()[1])
        return count