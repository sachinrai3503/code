# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node;
        otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.
    
Zigzag length is defined as the number of nodes visited - 1. 
(A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.max_path_len = 0
    
    def get_path_len(self, root):
        if root is None: return [0, 0] # [left_subtree_path_len, right_subtree_path_len]
        left = self.get_path_len(root.left)
        right = self.get_path_len(root.right)
        path_len_via_root = [1 + left[1], 1 + right[0]]
        self.max_path_len = max(self.max_path_len, max(path_len_via_root))
        return path_len_via_root
    
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None : return -1
        self.get_path_len(root)
        return self.max_path_len - 1