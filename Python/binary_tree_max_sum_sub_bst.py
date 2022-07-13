# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
# https://www.geeksforgeeks.org/maximum-sub-tree-sum-in-a-binary-tree-such-that-the-sub-tree-is-also-a-bst/
"""
Given a binary tree root, return the maximum sum of all keys of any sub-tree which
 is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    
Example 1:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node 
             with key equal to 3.

Example 2:
Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with
             key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 
Constraints:
The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104
"""

from sys import maxsize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def get_max_sub_bst(self, root):
        if root is None:
            print('Empty')
            return [0,0,0] # [min,sum,max]
        left, right = [None, 0, maxsize*-1], [maxsize, 0, None]
        if root.left is not None:
            left = self.get_max_sub_bst(root.left)
        if root.right is not None:
            right = self.get_max_sub_bst(root.right)
        if left is None or right is None: return None
        if left[-1]<root.val<right[0]:
            t_sum = root.val + left[1] + right[1]
            self.max_sum = max(self.max_sum, t_sum)
            return [left[0] if left[0] else root.val, t_sum, right[-1] if right[-1] else root.val]
        return None
        
    
    def maxSumBST(self, root: TreeNode) -> int:
        self.max_sum = 0
        self.get_max_sub_bst(root)
        return self.max_sum