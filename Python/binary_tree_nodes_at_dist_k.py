# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
Given the root of a binary tree, the value of a target node target, and an integer k,
 return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) 
 have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
 
Constraints:
The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def get_nodes_at_dist_k(self, root, k, cur_k):
        if root is None: return
        if cur_k>k: return
        if cur_k==k:
            self.op.append(root.val)
            return
        self.get_nodes_at_dist_k(root.left, k, cur_k+1)
        self.get_nodes_at_dist_k(root.right, k, cur_k+1)
    
    def find_nodes_at_k_from_target(self, root, target, k):
        if root is None: return 0
        if root.val==target.val:
            self.get_nodes_at_dist_k(root, k, 0)
            return 1
        left = self.find_nodes_at_k_from_target(root.left, target, k)
        if left!=0:
            if left==k: self.op.append(root.val)
            elif left<k: self.get_nodes_at_dist_k(root.right, k, left+1)
            return left+1
        right = self.find_nodes_at_k_from_target(root.right, target, k)
        if right!=0:
            if right==k: self.op.append(root.val)
            elif right<k: self.get_nodes_at_dist_k(root.left, k, right+1)
            return right+1
        return 0
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        self.op = list()
        self.find_nodes_at_k_from_target(root, target, k)
        return self.op
