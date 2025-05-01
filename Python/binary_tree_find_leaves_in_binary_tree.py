# https://leetcode.com/problems/find-leaves-of-binary-tree
# https://www.lintcode.com/problem/650
"""
Description
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and
 remove all leaves, repeat until the tree is empty.

Example
Example1
Input: {1,2,3,4,5}
Output: [[4, 5, 3], [2], [1]].
Explanation:

    1
   / \
  2   3
 / \     
4   5    

Example2
Input: {1,2,3,4}
Output: [[4, 3], [2], [1]].
Explanation:

    1
   / \
  2   3
 /
4 
"""

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:

    def __init__(self):
        self.nodes = dict()

    def get_leaves(self, root : TreeNode) -> int:
        if not root: return 0
        left = self.get_leaves(root.left)
        right = self.get_leaves(root.right)
        depth = max(left, right) + 1
        nodes_at_depth = self.nodes.get(depth, [])
        nodes_at_depth.append(root.val)
        self.nodes[depth] = nodes_at_depth
        return depth

    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        self.get_leaves(root)
        return [v for _, v in self.nodes.items()]