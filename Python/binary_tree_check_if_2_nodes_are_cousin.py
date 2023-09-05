# https://leetcode.com/problems/cousins-in-binary-tree
"""
Given the root of a binary tree with unique values and the values of two different
 nodes of the tree x and y, return true if the nodes corresponding to the values x 
 and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each
 depth k node are at the depth k + 1.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:
The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def search_child(self, que, child_val):
        if not que: return False
        while que[0]:
            temp = que.popleft()
            if temp.left and temp.left.val==child_val: return True
            if temp.right and temp.right.val==child_val: return True
        return False

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return False
        if root.val in [x, y]: return False
        que = deque()
        que.append(root)
        que.append(None)
        while que[0]:
            while que[0]:
                temp = que.popleft()
                if temp.left:
                    if temp.left.val==x:
                        return self.search_child(que, y)
                    if temp.left.val==y:
                        return self.search_child(que, x)
                    que.append(temp.left)
                if temp.right:
                    if temp.right.val==x:
                        return self.search_child(que, y)
                    if temp.right.val==y:
                        return self.search_child(que, x)
                    que.append(temp.right)
            que.popleft()
            que.append(None)
        return False