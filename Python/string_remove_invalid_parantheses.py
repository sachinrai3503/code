# https://leetcode.com/problems/remove-invalid-parentheses/
# https://www.geeksforgeeks.org/remove-invalid-parentheses/
"""
Remove the minimum number of invalid parentheses in order to make the input 
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

# Added a better readable code around same logic

from collections import deque

class Solution:
    
    def is_balanced(self, s):
        if s is None: return False
        count = 0
        for char in s:
            if char==')': count-=1
            elif char=='(': count+=1
            if count<0: return False
        if count!=0: return False
        return True
    
    def removeInvalidParentheses(self, s: str) -> list[str]:
        op_list = list()
        visited = set()
        que = deque()
        que.append(s)
        que.append(None)
        visited.add(s)
        while len(que)>0 and que[0]!=None:
            while len(que)>0 and que[0]!=None:
                temp = que.popleft()
                if self.is_balanced(temp):
                    op_list.append(temp)
                len_temp = len(temp)
                for i in range(len_temp):
                    if temp[i] not in '()': continue
                    t_s = temp[0:i] + temp[i+1:len_temp]
                    if t_s not in visited:
                        visited.add(t_s)
                        que.append(t_s)
            que.popleft()
            if len(op_list)>0: return op_list
            que.append(None)
        return None