# https://leetcode.com/problems/maximum-width-of-binary-tree/
"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes 
 (the leftmost and rightmost non-null nodes), where the null nodes between the
 end-nodes are also counted into the length calculation.
It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:
Input: root = [1,3,2,5,null,null,9,6,null,null,7]
Output: 8
Explanation: The maximum width existing in the fourth level with the length 8
 (6,null,null,null,null,null,null,7).
 
Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""
from collections import deque

class NULLNODE:
    def __init__(self):
        self.is_null_node = True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # This will give timeout for large tree
    def widthOfBinaryTree2(self, root) -> int:
        max_width = 0
        que = deque()
        null_node = NULLNODE()
        que.append(root)
        que.append(null_node)
        while len(que)>0 and que[0]!=null_node:
            s, e = 0, -1
            i = 0
            after_first_non_null_node = False
            while len(que)>0 and que[0]!=null_node:
                temp = que.popleft()
                if temp is None and not after_first_non_null_node: continue
                if temp is not None:
                    if not after_first_non_null_node:
                        s = i
                        after_first_non_null_node = True
                    e = i
                    que.append(temp.left)
                    que.append(temp.right)
                else:
                    que.append(None)
                    que.append(None)
                i+=1
            que.popleft()
            max_width = max(max_width, e-s+1)
            # if not after_first_non_null_node: break
            que.append(null_node)
        return max_width
    
    # Sol. based on concept of complete binary tree
    def get_max_width(self, root, level, order, leftmost_node_order):
        if root is None: return 0
        if leftmost_node_order[level] is None:
            leftmost_node_order[level] = order
        cur_width = order - leftmost_node_order[level] + 1
        child_width = max(self.get_max_width(root.left, level+1, order*2+1, leftmost_node_order), self.get_max_width(root.right, level+1, order*2+2, leftmost_node_order))
        return max(cur_width, child_width)

    def widthOfBinaryTree(self, root) -> int:
        leftmost_node_order = [None for i in range(3000)]
        return self.get_max_width(root, 0, 0, leftmost_node_order)