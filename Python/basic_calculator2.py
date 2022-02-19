# https://leetcode.com/problems/basic-calculator-ii/
"""
Given a string s which represents an expression, evaluate this expression and
 return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
 results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
 as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    
    def get_priority(self, c):
        if c is None: return -1
        if c=='*' or c=='/': return 2
        return 1
    
    def is_digit(self, c):
        return 48<=ord(c)<=57
    
    def evaluate_operator(self, a, b, oper):
        if oper == '+': return a+b
        if oper == '-': return a-b
        if oper == '*': return a*b
        if oper == '/': return a//b
    
    def evaluate_till(self, num_list, oper_stck, prio):
        while len(oper_stck)>0 and self.get_priority(oper_stck[-1])>=prio:
            oper = oper_stck.pop()
            b = num_list.pop()
            a = num_list.pop()
            num_list.append(self.evaluate_operator(a, b, oper))
    
    def calculate_stck(self, s: str) -> int:
        stck = list()
        num_list = list()
        num = 0
        is_prev_digit = False
        for c in s:
            if self.is_digit(c):
                num = num*10 + (ord(c)-48)
                is_prev_digit = True
            elif c == ' ': continue
            else:
                num_list.append(num)
                is_prev_digit = False
                num = 0
                self.evaluate_till(num_list, stck, self.get_priority(c))
                stck.append(c)
        if is_prev_digit:
            num_list.append(num)
            is_prev_digit = False
        self.evaluate_till(num_list, stck, -1)
        return num_list[0]
    
    def calculate(self, s: str) -> int:
        a, b, c = None, None, None
        oper1, oper2 = None, None
        num = 0
        for char in s:
            if self.is_digit(char):
                num = num*10 + (ord(char)-48)
            elif char == ' ': continue
            else:
                if oper1 is None:
                    a = num
                    oper1 = char
                elif oper2 is None:
                    b = num
                    oper2 = char
                else:
                    c = num
                    if self.get_priority(oper1)>=self.get_priority(oper2):
                        a = self.evaluate_operator(a, b, oper1)
                        oper1 = oper2
                        b = c
                    else:
                        b = self.evaluate_operator(b, c, oper2)
                    oper2 = char
                    c = None
                num = 0
        if oper1 is None:
            a = num
            return a
        elif oper2 is None:
            b = num
            return self.evaluate_operator(a, b, oper1)
        else:
            c = num
            if self.get_priority(oper1)>=self.get_priority(oper2):
                temp = self.evaluate_operator(a, b, oper1)
                return self.evaluate_operator(temp, c, oper2)
            else:
                temp = self.evaluate_operator(b, c, oper2)
                return self.evaluate_operator(a, temp, oper1)