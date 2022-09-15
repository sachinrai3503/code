# https://leetcode.com/problems/create-binary-tree-from-descriptions/
"""
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti]
 indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
    If isLefti == 1, then childi is the left child of parenti.
    If isLefti == 0, then childi is the right child of parenti.
    Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

Example 1:
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

Example 2:
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 
Constraints:
1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        key_node_map = dict() # node.val -> [node, is_child]
        for description in descriptions:
            parent, child, is_left = description
            parent_node, child_node = key_node_map.get(parent, [TreeNode(parent), False]), key_node_map.get(child, [TreeNode(child), True])
            if is_left:
                parent_node[0].left = child_node[0]
            else:
                parent_node[0].right = child_node[0]
            child_node[1] = True
            key_node_map[parent] = parent_node
            key_node_map[child] = child_node
        # print(key_node_map)
        for key in key_node_map:
            if not key_node_map[key][1]: return key_node_map[key][0]
        return None