# https://leetcode.com/problems/longest-valid-parentheses
# https://www.geeksforgeeks.org/length-of-the-longest-valid-substring
"""
Given a string containing just the characters '(' and ')', return the length of 
 the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 
Constraints:
0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""

class Solution:

    def find_pairs(self, s:str, s_len:int) -> list:
        op = list()
        stack = list()
        for i in range(s_len):
            if s[i] == '(':
                stack.append(i)
            elif not stack:
                continue
            else:
                op.append((stack.pop(), i))
        # print(f'{op=}')
        return op

    """
    This is O(nlogn) time complexity, O(n) space
    """
    def longestValidParentheses_sort(self, s: str) -> int:
        s_len = len(s)
        pairs = self.find_pairs(s, s_len)
        pairs.sort(key = lambda x:x[0])
        # print(f'{pairs=}')
        max_len = 0
        start, end = 0, -1
        for i, j in pairs:
            if i<end: continue
            elif end==(i-1):
                end = j
            else:
                max_len = max(max_len, end-start+1)
                start, end = i, j
        max_len = max(max_len, end-start+1)
        return max_len

    """
    This is O(n) time complexity and O(n) space
    """
    def longestValidParentheses_dp(self, s: str) -> int:
        s_len = len(s)
        dp = [0]
        stack = list()
        for j in range(s_len):
            t_len = 0
            if s[j]=='(':
                stack.append(j)
            elif stack:
                i = stack.pop()
                t_len = dp[i] + (j-i+1)
            dp.append(t_len)
        return max(dp)

    def scan_from_left(self, s, s_len):
        max_len = 0
        left, right = 0, 0
        for char in s:
            if char=='(': left+=1
            else: right+=1
            if left==right: max_len = max(max_len, left+right)
            elif right>left: left, right = 0, 0
        return max_len
    
    def scan_from_right(self, s, s_len):
        max_len = 0
        left, right = 0, 0
        for i in range(s_len-1, -1, -1):
            char = s[i]
            if char == ')': right+=1
            else: left+=1
            if left==right: max_len = max(max_len, left+right)
            elif left>right: left, right = 0, 0
        return max_len

    """
    O(n) time and O(1) space
    """
    def longestValidParentheses(self, s: str) -> int:
        s_len = len(s)
        return max(self.scan_from_left(s, s_len), self.scan_from_right(s, s_len))