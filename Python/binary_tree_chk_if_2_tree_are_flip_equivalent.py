# https://leetcode.com/problems/flip-equivalent-binary-trees/
"""
For a binary tree T, we can define a flip operation as follows: choose any node,
 and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make
 X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees
 are flip equivelent or false otherwise.

Example 1:
Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Example 4:
Input: root1 = [0,null,1], root2 = []
Output: false

Example 5:
Input: root1 = [0,null,1], root2 = [0,1]
Output: true

Constraints:
The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
"""
from sys import maxsize

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_val(node):
    if node is None:
        return maxsize
    return node.val


class Solution:
    def flipEquiv_iter(self, root1: TreeNode, root2: TreeNode) -> bool:
        stck1, stck2 = list(), list()
        if root1 is not None:
            stck1.append(root1)
        if root2 is not None:
            stck2.append(root2)
        while len(stck1) > 0 and len(stck2) > 0:
            temp1 = stck1.pop()
            temp2 = stck2.pop()
            if temp1.val != temp2.val:
                return False
            val_left1, val_right1 = get_val(temp1.left), get_val(temp1.right)
            val_left2, val_right2 = get_val(temp2.left), get_val(temp2.right)
            if val_left1 == val_left2 and val_right1 == val_right2:
                if val_right1 != maxsize:
                    stck1.append(temp1.right)
                if val_left1 != maxsize:
                    stck1.append(temp1.left)
                if val_right2 != maxsize:
                    stck2.append(temp2.right)
                if val_left2 != maxsize:
                    stck2.append(temp2.left)
            elif val_left1 == val_right2 and val_right1 == val_left2:
                if val_right1 != maxsize:
                    stck1.append(temp1.right)
                if val_left1 != maxsize:
                    stck1.append(temp1.left)
                if val_left2 != maxsize:
                    stck2.append(temp2.left)
                if val_right2 != maxsize:
                    stck2.append(temp2.right)
            else:
                return False
        if len(stck1)+len(stck2) > 0:
            return False
        return True

    def flipEquiv(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        if root1.val != root2.val:
            return False
        if self.flipEquiv(root1.left, root2.left) and \
           self.flipEquiv(root1.right, root2.right):
            return True
        if self.flipEquiv(root1.left, root2.right) and \
           self.flipEquiv(root1.right, root2.left):
            return True
        else:
            return False
