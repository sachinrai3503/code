# https://www.interviewbit.com/problems/burn-a-tree/
# https://www.geeksforgeeks.org/minimum-time-to-burn-a-tree-starting-from-a-leaf-node/
"""
Given a binary tree and a leaf node from this tree. It is known that in 1s all
 nodes connected to a given node (left child, right child and parent) get burned
 in 1 second. Then all the nodes which are connected through one intermediate get
 burned in 2 seconds, and so on. The task is to find the minimum time required to
 burn the complete binary tree.

Examples: 
Input : 
            1
       /       \
      2          3
    /  \          \
   4    5          6
      /   \         \
     7     8         9
                      \
                       10
Leaf = 8
Output : 7
"""

import sys
sys.setrecursionlimit(150000)
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def __init__(self):
        self.is_found = False
        self.min_time = -1

    def get_height(self, root):
        if root is None: return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def get_min_time_to_burn(self, root, leaf_node):
        if root is None: return 0
        if root.val == leaf_node:
            self.is_found = True
            self.min_time = 0
            return 1
        left = self.get_min_time_to_burn(root.left, leaf_node)
        if self.is_found:
            right_height = self.get_height(root.right)
            self.min_time = max(self.min_time, left+right_height)
            return left+1
        right = self.get_min_time_to_burn(root.right, leaf_node)
        if self.is_found:
            self.min_time = max(self.min_time, left + right)
            return right+1
        return max(left, right) + 1

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        self.get_min_time_to_burn(A, B)
        return self.min_time