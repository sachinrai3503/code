# https://www.lintcode.com/problem/basic-calculator-iii/
"""
Description
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + 
 or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators ,
 open ( and closing parentheses ) and empty spaces . The integer division should
 truncate toward zero.

You may assume that the given expression is always valid. All intermediate results
 will be in the range of [-2147483648, 2147483647]

Example

Example 1:
Input："1 + 1"
Output：2
Explanation：1 + 1 = 2

Example 2:
Input：" 6-4 / 2 "
Output：4
Explanation：4/2=2，6-2=4
"""

class Solution:

    def get_priority(self, c):
        if c is None: return -1
        if c=='*' or c=='/': return 2
        elif c=='+' or c=='-': return 1
        return 0
    
    def is_digit(self, c):
        return 48<=ord(c)<=57
    
    def is_operator(self, c):
        try:
            if c in '+-/*': return True
        except TypeError as e: return False

    def evaluate_operator(self, a, b, oper):
        if oper == '+': return a+b
        if oper == '-': return a-b
        if oper == '*': return a*b
        if oper == '/': return a//b

    def to_post_fix(self, s):
        stck = list()
        post_fix = list()
        num = 0
        is_prev_num = False
        for c in s:
            if self.is_digit(c):
                num = num*10 + (ord(c)-48)
                is_prev_num = True
            else:
                if is_prev_num: post_fix.append(num)
                num = 0
                is_prev_num = False
                if c == ' ': continue
                elif c=='(': stck.append(c)
                elif c==')':
                    while stck[-1]!='(':
                        post_fix.append(stck.pop())
                    stck.pop()
                else:
                    prio = self.get_priority(c)
                    while len(stck)>0 and self.get_priority(stck[-1])>=prio:
                        post_fix.append(stck.pop())
                    stck.append(c)
        if is_prev_num: post_fix.append(num)
        while len(stck)>0:
            post_fix.append(stck.pop())
        return post_fix

    def eval_post_fix(self, post_fix):
        stck = list()
        for item in post_fix:
            if self.is_operator(item):
                b = stck.pop()
                a = stck.pop()
                stck.append(self.evaluate_operator(a, b, item))
            else:
                stck.append(item)
        return stck[0]

    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        post_fix = self.to_post_fix(s)
        # print(post_fix)
        return self.eval_post_fix(post_fix)