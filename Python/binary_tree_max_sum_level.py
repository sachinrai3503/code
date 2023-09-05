# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
"""
Given the root of a binary tree, the level of its root is 1, the level of its children is
 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:
The number of nodes in the tree is in the range [1, 104].
-10^5 <= Node.val <= 10^5
"""

from collections import deque
from sys import maxsize
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -maxsize
        op_level = -1
        que = deque()
        que.append(root)
        que.append(None)
        level = 1
        while que and que[0]:
            level_sum = 0
            while que and que[0]:
                temp = que.popleft()
                level_sum+=temp.val
                if temp.left: que.append(temp.left)
                if temp.right: que.append(temp.right)
            que.popleft()
            if level_sum>max_sum:
                max_sum = level_sum
                op_level = level
            level+=1
            que.append(None)
        return op_level