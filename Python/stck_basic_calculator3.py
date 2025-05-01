# https://leetcode.com/problems/basic-calculator-iii
# https://www.lintcode.com/problem/849
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , 
 open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results 
 will be in the range of [-2147483648, 2147483647]

Do not use the eval built-in library function.

Example
Example 1:
Input: "1 + 1"
Output: 2
Explanation: 1 + 1 = 2

Example 2:
Input: " 6-4 / 2 "
Output 4
Explanation 4/2=2, 6-2=4
"""

class Solution:

    def get_priority(self, oper):
        if oper in '+-': return 1
        if oper in "*/": return 2
        if oper in '()': return 0
        return None

    def compute(self, a, opr, b):
        if opr=='+': return a + b
        if opr=='-': return a-b
        if opr=='*': return a*b
        if opr=='/': return a//b
        return None

    # a + (b*c) - d = abc*+d-
    def to_postfix(self, s, s_len):
        stck = list()
        op = list()
        i = 0
        while i<s_len:
            char = s[i]
            if char==' ':
                pass
            elif '0'<=char<='9':
                num = 0
                while i<s_len and '0'<=s[i]<='9':
                    num = num*10 + (ord(s[i])-48)
                    i+=1
                op.append(num)
                i-=1
            elif char in '+-/*':
                char_prio = self.get_priority(char)
                while stck and self.get_priority(stck[-1])>=char_prio:
                    op.append(stck.pop())
                stck.append(char)
            elif char=='(':
                stck.append(char)
            else:
                while stck and stck[-1]!='(':
                    op.append(stck.pop())
                stck.pop()
            i+=1
            # print(f'{stck=}')
        while stck:
            op.append(stck.pop())
        return op

    def evaluate_post_fix(self, post_fix):
        op = 0
        post_fix_len = len(post_fix)
        stck = list()
        i = 0
        while i<post_fix_len:
            item = post_fix[i]
            if type(item)==str and item in '+-/*':
                b = stck.pop()
                a = stck.pop()
                stck.append(self.compute(a, item, b))
            else:
                stck.append(item)
            i+=1
            # print(f'{stck=}')
        return stck[-1]

    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s: str) -> int:
        s_len = len(s)
        op = 0
        post_fix = self.to_postfix(s, s_len)
        # print(f'{post_fix=}')
        return self.evaluate_post_fix(post_fix)