# https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
 represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to 
 any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from typing import List

class Solution:

    def __init__(self):
        self.map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.op = list()

    def combine(self, digits, digits_len, current_index, op):
        if current_index==digits_len:
            self.op.append(''.join(op))
            return
        for char in self.map.get(digits[current_index]):
            op.append(char)
            self.combine(digits, digits_len, current_index+1, op)
            op.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='': return []
        digits_len = len(digits)
        self.combine(digits, digits_len, 0, [])
        return self.op