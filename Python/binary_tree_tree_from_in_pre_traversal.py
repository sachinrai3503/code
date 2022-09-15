# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal
"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a
 binary tree and inorder is the inorder traversal of the same tree, construct and return
 the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def create_tree(self, preorder, pre_index, inorder, s, e, inorder_index_map):
        if s>e: return None
        in_index = inorder_index_map.get(preorder[pre_index[0]])
        pre_index[0]+=1
        root = TreeNode(inorder[in_index])
        root.left = self.create_tree(preorder, pre_index, inorder, s, in_index-1, inorder_index_map)
        root.right = self.create_tree(preorder, pre_index, inorder, in_index+1, e, inorder_index_map)
        return root
    
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        n = len(inorder)
        inorder_index_map = {inorder[i]:i for i in range(n)}
        pre_index = [0]
        return self.create_tree(preorder, pre_index, inorder, 0, n-1, inorder_index_map)