# https://leetcode.com/problems/valid-number/
"""
A valid number can be split up into these components (in order):
    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
    - (Optional) A sign character (either '+' or '-').
    - One of the following formats:
        - One or more digits, followed by a dot '.'.
        - One or more digits, followed by a dot '.', followed by one or more digits.
        - A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
    - (Optional) A sign character (either '+' or '-').
    - One or more digits.

For example, all the following are valid numbers: 
 ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
 "53.5e93", "-123.456e789"], while the following are not 
 valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
 
Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false
 
Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""

class Solution:
    
    # Below uses Finite automata
    def isNumber(self, s: str) -> bool:
        # No. of state = [0-8], no. of col = 5 [+-,.,eE,0-9,Aa-Zz]
        # Pass state = 2,4,7 : Fail state = 8 : rest all also fail
        TA = [[1,3,8,2,8],
              [8,3,8,2,8],
              [8,4,5,2,8],
              [8,8,8,4,8],
              [8,8,5,4,8],
              [6,8,8,7,8],
              [8,8,8,7,8],
              [8,8,8,7,8]]
        PASS_STATE = [2,4,7]
        FAIL_STATE = 8 # Any other in betn state is also fail. 
        state = 0
        s_len = len(s)
        for i in range(s_len):
            char = s[i]
            col = None
            if char in '+-': col = 0
            elif char == '.': col = 1
            elif char in 'eE': col = 2
            elif '0'<=char<='9': col = 3
            else: col = 4
            state = TA[state][col]
            if state==FAIL_STATE: return False
        return True if state in PASS_STATE else False