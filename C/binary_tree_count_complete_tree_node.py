# https://leetcode.com/problems/count-complete-tree-nodes/
# https://www.geeksforgeeks.org/find-value-k-in-given-complete-binary-tree-with-values-indexed-from-1-to-n
"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled
 in a complete binary tree, and all nodes in the last level are as far left as possible.
 It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def get_max_level(self, root):
        level = 0
        while root:
            level+=1
            root = root.left
        return level-1
    
    def search_node_at_index(self, root, cur_index, s, e, k):
        while root:
            if cur_index==k: return True
            mid = s + (e-s)//2
            if k>mid:
                root = root.right
                cur_index = cur_index*2+2
                s = mid+1
            else:
                root = root.left
                cur_index = cur_index*2+1
                e = mid
        return False
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        last_node_index = -1
        max_level = self.get_max_level(root)
        s = l_index = (2**max_level - 1) # index of 1st node on last level
        e = r_index = l_index*2 # index of last node on last level
        # print(f'{max_level=} {l_index=} {r_index=}')
        while s<=e:
            # print(f'{s=} {e=}')
            mid = s + (e-s)//2
            if self.search_node_at_index(root, 0, l_index, r_index, mid):
                last_node_index = mid
                s = mid+1
            else:
                e = mid-1
        return last_node_index+1