# https://www.lintcode.com/problem/1534/
"""
Description
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left 
 and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

We want to transform this BST into a circular doubly linked list. Each node in a 
 doubly linked list has a predecessor and successor. For a circular doubly linked list, 
 the predecessor of the first element is the last element, and the successor of the
 last element is the first element.

Example
Example 1:
Input: {4,2,5,1,3}
        4
       /  \
      2   5
     / \
    1   3
Output: "left:1->5->4->3->2  right:1->2->3->4->5"
Explanation:
Left: reverse output
Right: positive sequence output

Example 2:
Input: {2,1,3}
        2
       /  \
      1   3
Output: "left:1->3->2  right:1->2->3"
"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:

    def _connect_circular_dll(self, list1_head, list2_head):
        list1_tail, list2_tail = list1_head.left, list2_head.left
        list1_head.left = list2_tail
        list2_tail.right = list1_head
        list1_tail.right = list2_head
        list2_head.left = list1_tail

    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if root is None: return None
        left_dll_head = self.treeToDoublyList(root.left)
        right_dll_head = self.treeToDoublyList(root.right)
        root.left = root.right = root
        if left_dll_head:
            self._connect_circular_dll(left_dll_head, root)
        else:
            left_dll_head = root
        if right_dll_head:
            self._connect_circular_dll(left_dll_head, right_dll_head)
        return left_dll_head