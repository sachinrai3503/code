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


from collections import deque

def is_valid(ip):
    count = 0
    for c in ip:
        if c=='(':
            count+=1
        elif c==')':
            count-=1
        if count<0:
            return False
    if count==0: return True
    return False

class NullNode:
    def __init__(self):
        self.value = -1

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = 0
        op = set()
        already_visited = set()
        que = deque()
        null_node = NullNode()
        found_flag = False
        que.append(s)
        already_visited.add(s)
        que.append(null_node)
        while len(que)>0 and que[0]!=null_node:
            while len(que)>0 and que[0]!=null_node:
                temp = que.popleft()
                if is_valid(temp): 
                    found_flag = True
                    op.add(temp)
                if not found_flag:
                    t_len = len(temp)
                    for j in range(t_len):
                        if temp[j]==')' or temp[j]=='(':
                            next_str = temp[0:j] + temp[j+1:t_len]
                            if next_str not in already_visited:
                                que.append(next_str)
                                already_visited.add(next_str)
            que.popleft()
            if found_flag: break
            count+=1
            que.append(null_node)
        # print(count)
        return op