# https://leetcode.com/problems/expression-add-operators
"""
Given a string num that contains only digits and an integer target, return all possibilities to 
 insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant
 expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

Constraints:
1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
"""

from typing import List

class Solution:

    def get_priority(self, op):
        if op=='*': return 2
        return 1

    def evaluate(self, a, b, op):
        if op=='+': return a+b
        if op=='-': return a-b
        if op=='*': return a*b
        return None

    def to_infix(self, arr, arr_len):
        stck = list()
        op = list()
        for i in range(arr_len):
            c = arr[i]
            if c not in self.operators:
                op.append(c)
            else:
                while stck and self.get_priority(stck[-1])>=self.get_priority(c):
                    op.append(stck.pop())
                stck.append(c)
        # print(f'{op=} {stck=} {arr=} {arr_len=}')
        while stck:
            op.append(stck.pop())
        return op
    
    def compute(self, arr, arr_len):
        # print(f'{arr=} {arr_len=}')
        in_fix = self.to_infix(arr, arr_len)
        in_fix_len = len(in_fix)
        # print(f'{in_fix=}')
        stck = list()
        op = 0
        for i in range(in_fix_len):
            c = in_fix[i]
            if c not in self.operators:
                stck.append(int(c))
            else:
                b = stck.pop()
                a = stck.pop()
                stck.append(self.evaluate(a, b, c))
        return stck[-1]

    def add_operators_in(self, arr, arr_len, i, cur_op):
        if i==arr_len:
            ans = self.compute(cur_op, len(cur_op))
            if ans==self.target:
                self.op.append(''.join(cur_op))
            return
        c = arr[i]
        for j in range(i, arr_len):
            cur_op.append(arr[i:j+1])
            if j==(arr_len-1):
                self.add_operators_in(arr, arr_len, j+1, cur_op)
            else:
                for oper in self.operators:
                    cur_op.append(oper)
                    self.add_operators_in(arr, arr_len, j+1, cur_op)
                    cur_op.pop()
            cur_op.pop()
            if c=='0': break

    # This one is very slow. Below tries to avoid the infix calculation
    def addOperators1(self, num: str, target: int) -> List[str]:
        num_len = len(num)
        cur_op = list()
        self.op = list()
        self.target = target
        self.operators = ['+', '-', '*']
        self.add_operators_in(num, num_len, 0, cur_op)
        return self.op

    def compute_once(self, a, op1, b, op2, c):
        if op1 is None or op2 is None or a is None or b is None or c is None: return a, op1, b, op2, c
        if self.get_priority(op1)>=self.get_priority(op2):
            return self.evaluate(a, b, op1), op2, c, None, None
        return a, op1, self.evaluate(b, c, op2), None, None

    def compute_full(self, a, op1, b, op2, c):
        if op1 is None:
            return a
        if op2 is None:
            return self.evaluate(a, b, op1)
        if self.get_priority(op1)>=self.get_priority(op2):
            return self.evaluate(self.evaluate(a, b, op1), c, op2)
        return self.evaluate(a, self.evaluate(b, c, op2), op1)

    def add_operators_in_exp(self, nums, nums_len, i, is_oper, cur_op, a, op1, b, op2, c):
        if i==nums_len:
            if self.compute_full(a, op1, b, op2, c)==self.target:
                self.op.append(''.join(cur_op))
            return
        a, op1, b, op2, c = self.compute_once(a, op1, b, op2, c)
        if is_oper:
            for oper in self.operator:
                cur_op.append(oper)
                if op1 is None:
                    self.add_operators_in_exp(nums, nums_len, i, False, cur_op, a, oper, b, op2, c)
                else:
                    self.add_operators_in_exp(nums, nums_len, i, False, cur_op, a, op1, b, oper, c)
                cur_op.pop()
        else:
            t_num = 0
            for j in range(i, nums_len):
                t_num = t_num*10 + (ord(nums[j])-48)
                cur_op.append(nums[i:j+1])
                if a is None:
                    self.add_operators_in_exp(nums, nums_len, j+1, True, cur_op, t_num, op1, b, op2, c)
                elif b is None:
                    self.add_operators_in_exp(nums, nums_len, j+1, True, cur_op, a, op1, t_num, op2, c)
                else:
                    self.add_operators_in_exp(nums, nums_len, j+1, True, cur_op, a, op1, b, op2, t_num)
                cur_op.pop()
                if t_num==0:
                    break
            
    def addOperators(self, num: str, target: int) -> List[str]:
        nums_len = len(num)
        # print(f'{nums=} {nums_len=}')
        self.target = target
        self.operator = ['+', '-', '*']
        self.op = list()
        cur_op = list()
        self.add_operators_in_exp(num, nums_len, 0, False, cur_op, None, None, None, None, None)
        return self.op