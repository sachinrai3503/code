# https://leetcode.com/problems/valid-parenthesis-string
"""
Given a string s containing only three types of characters: '(', ')' and '*', 
 return true if s is valid.

The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.

'*' could be treated as a single right parenthesis ')' or a single left parenthesis
  '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true 

Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        s_len = len(s)
        ast_count, open_count, close_count = 0, 0, 0
        for char in s:
            if char == '*':
                ast_count+=1
            elif char == '(':
                open_count+=1
            else:
                if open_count>0:
                    open_count-=1
                elif ast_count>0:
                    ast_count-=1
                else: return False
        # print(f'{ast_count=} {open_count=} {close_count=}')
        if open_count>0 and ast_count<open_count: return False
        ast_count, open_count, close_count = 0, 0, 0
        for i in range(s_len-1, -1, -1):
            char = s[i]
            if char == '*':
                ast_count+=1
            elif char == ')':
                close_count+=1
            else:
                if close_count>0:
                    close_count-=1
                elif ast_count>0:
                    ast_count-=1
                else: return False
        # print(f'-{ast_count=} {open_count=} {close_count=}')
        return True