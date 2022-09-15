# https://leetcode.com/problems/multiply-strings
# https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists
"""
Given two non-negative integers num1 and num2 represented as strings, return the product
 of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer
 directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    
    def int_mult(self, a, b):
        return (ord(a)-48)*(ord(b)-48)
    
    def multiply_by(self, num1, digit, op, index):
        carry = 0
        num1_len = len(num1)
        for i in range(num1_len):
            t_prod = self.int_mult(num1[i], digit) + carry
            if index>=len(op):
                op.append(0)
            t_sum = (op[index] + t_prod)
            op[index] = t_sum%10
            carry = t_sum//10
            index+=1
        if carry!=0:
            op.append(carry)
        return op
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0': return '0'
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        op = list()
        len_num2 = len(num2_rev)
        for i in range(len_num2):
            self.multiply_by(num1_rev, num2_rev[i], op, i)
        return ''.join([str(num) for num in op[::-1]])