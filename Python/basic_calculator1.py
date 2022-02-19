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
    
    def evaluate(self, a, b, oper):
        if oper=='+': return a+b
        else: return a-b
    
    def is_digit(self, c):
        if 48<=ord(c)<=57: return True
        return False
    
    def operator(self, num_list, oper_stck):
        oper = oper_stck.pop()
        b = num_list.pop()
        a = num_list.pop()
        num_list.append(self.evaluate(a,b,oper))
    
    def calculate(self, s: str) -> int:
        stck = list()
        num_list = list()
        num = 0
        is_prev_digit = False
        is_operand_missing = True
        for c in s:
            # print(num_list, stck, num, c)
            if self.is_digit(c):
                num = num*10 + ord(c)-48
                is_prev_digit = True
                is_operand_missing = False
            else:
                if is_prev_digit: num_list.append(num)
                num = 0
                is_prev_digit = False
                if c==' ': continue
                elif c=='+' or c=='-':
                    if len(stck)>0 and stck[-1]!='(':
                        self.operator(num_list, stck)
                    if is_operand_missing: num_list.append(0)
                    is_operand_missing = False
                    stck.append(c)
                elif c=='(': 
                    stck.append(c)
                    is_operand_missing = True
                elif c==')':
                    if stck[-1]!='(':
                        self.operator(num_list, stck)
                    stck.pop()
                    is_operand_missing = False
        # print(num_list, stck, num)
        if is_prev_digit: num_list.append(num)
        num = 0
        # print(num_list, stck, num)
        if len(stck)>0:
            self.operator(num_list, stck)
        return num_list[0]