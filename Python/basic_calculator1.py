# https://leetcode.com/problems/basic-calculator/
"""
Given a string s representing a valid expression, implement a basic calculator
 to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings
 as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

class Solution:

    def net_sign(self, a, b):
        if a is None: a = '+'
        if b is None: b = '+'
        if a=='+': return b
        if a=='-': return '+' if b=='-' else '-'

    def compute(self, a, opr, b):
        if opr=='+': return a + b
        if opr=='-': return a-b
        return None

    def calculate(self, s: str) -> int:
        op = 0
        s_len = len(s)
        stck = list()
        sign = None
        i = 0
        while i<s_len:
            char = s[i]
            if char==' ':
                pass
            elif char=='+': sign = '+'
            elif char=='-': sign = '-'
            elif char=='(':
                bracket_sign = '+' if not stck else stck[-1]
                sign = '+' if sign is None else sign
                stck.append(self.net_sign(bracket_sign, sign))
                sign = None
            elif char==')':
                stck.pop()
            else:
                num = 0
                while i<s_len and '0'<=s[i]<='9':
                    num = num*10 + (ord(s[i])-48)
                    i+=1
                bracket_sign = '+' if not stck else stck[-1]
                sign = '+' if sign is None else sign
                op = self.compute(op, self.net_sign(bracket_sign, sign), num)
                sign = None
                i-=1
            i+=1
        return op