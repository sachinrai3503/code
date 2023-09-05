# https://leetcode.com/problems/find-duplicate-subtrees
"""
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:
The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.op = list()
        self.tree_map = dict() # tree:False/True

    def find_duplicate_subtrees(self, root):
        if root is None: return 'N'
        left = self.find_duplicate_subtrees(root.left)
        right = self.find_duplicate_subtrees(root.right)
        sub_tree = '*'.join([str(root.val),left,right])
        # print(f'{sub_tree=}')
        is_included = self.tree_map.get(sub_tree, None)
        if is_included is None:
            self.tree_map[sub_tree] = False
        elif not is_included:
            self.op.append(root)
            self.tree_map[sub_tree] = True
        return sub_tree

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.find_duplicate_subtrees(root)
        return self.op