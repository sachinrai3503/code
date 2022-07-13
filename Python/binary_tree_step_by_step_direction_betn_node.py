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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def __init__(self):
        self.s = 0
    
    def get_path_from(self, root, dest, cur_child, path:list):
        if root is None: return False
        path.append(cur_child)
        if root.val==dest: return True
        left = self.get_path_from(root.left, dest, 'L', path)
        if left: return left
        right = self.get_path_from(root.right, dest, 'R', path)
        if right: return True
        path.pop()
        return False

    def get_path_between(self, root, src, dest):
        if root == None: return None
        if root.val==src:
            self.s = 1
            t_path = list()
            is_path = self.get_path_from(root, dest, '', t_path)
            if is_path:
                self.s = 2
                return t_path
            return ['U']
        left = self.get_path_between(root.left, src, dest)
        if self.s==2:
            return left
        if self.s==1:
            if root.val==dest:
                self.s = 2
            else:
                t_path = list()
                is_path = self.get_path_from(root.right, dest, 'R', t_path)
                if is_path:
                    self.s = 2
                    return left + t_path
                left.append('U')
            return left
        right = self.get_path_between(root.right, src, dest)
        if self.s==2: return right
        if self.s==1:
            if root.val==dest:
                self.s = 2
            else:
                t_path = list()
                is_path = self.get_path_from(root.left, dest, 'L', t_path)
                if is_path:
                    self.s = 2
                    return right + t_path
                right.append('U')
            return right
        return None
            
    
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        path = self.get_path_between(root, startValue, destValue)
        # print(path)
        return ''.join(path)