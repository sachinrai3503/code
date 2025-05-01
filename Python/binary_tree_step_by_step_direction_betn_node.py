# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a
 value from 1 to n. You are also given an integer startValue representing the value of
 the start node s, and a different integer destValue representing the value of the
 destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step
 directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'.
 Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def find_in_child(self, root, target, op1, op2, child_type):
        if root is None: return False
        op1.append(child_type)
        op2.append('U')
        if root.val == target: return True
        if self.find_in_child(root.left, target, op1, op2, 'L'):
            return True
        if self.find_in_child(root.right, target, op1, op2, 'R'):
            return True
        op1.pop()
        op2.pop()
        return False

    def find_directions(self, root, start, dest, op1, op2, child_type):
        if root is None: return
        if root.val==start or root.val==dest:
            self.s = 1
            self.other = dest if root.val==start else start
            if self.find_in_child(root.left, self.other, op1, op2, 'L') or \
                self.find_in_child(root.right, self.other, op1, op2, 'R'):
                self.s = 2
                return
            op1.append('U')
            op2.append(child_type)
            return
        self.find_directions(root.left, start, dest, op1, op2, 'L')
        if self.s==1:
            if self.find_in_child(root.right, self.other, op1, op2, 'R'):
                self.s = 2
                return
            op1.append('U')
            op2.append(child_type)
            return
        self.find_directions(root.right, start, dest, op1, op2, 'R')
        if self.s==1:
            op1.append('U')
            op2.append(child_type)
        return

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        op1 = list()
        op2 = list()
        self.s = 0
        self.other = None
        self.find_directions(root, startValue, destValue, op1, op2, None)
        # print(f'{self.s=} {self.other=} {op1=} {op2=}')
        if self.s!=2:
            return None
        return ''.join(op1) if self.other==destValue else ''.join(op2[::-1])