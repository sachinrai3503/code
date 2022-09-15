# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of 
a binary tree and postorder is the postorder traversal of the same tree, construct and
return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def create_tree(self, postorder, post_index, inorder, s, e, inorder_index_map):
        if s>e: return None
        in_index = inorder_index_map.get(postorder[post_index[0]])
        post_index[0]-=1
        root = TreeNode(inorder[in_index])
        root.right = self.create_tree(postorder, post_index, inorder, in_index+1, e, inorder_index_map)
        root.left = self.create_tree(postorder, post_index, inorder, s, in_index-1, inorder_index_map)
        return root
    
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        n = len(inorder)
        inorder_index_map = {inorder[i]:i for i in range(n)}
        post_index = [n-1]
        return self.create_tree(postorder, post_index, inorder, 0, n-1, inorder_index_map)