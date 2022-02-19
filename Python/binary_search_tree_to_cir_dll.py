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

    def toCDLL(self, root):
        if root is None: return None
        left = self.toCDLL(root.left)
        right = self.toCDLL(root.right)
        head = None
        if left is not None:
            head = left
            left.left.right = root
            root.left = left.left
            if right is not None:
                left.left = right.left
            else:
                left.left = root
        else:
            head = root
            if right is not None:
                root.left = right.left
            else:
                root.left = root
        if right is not None:
            if left is not None:
                right.left.right = left
            else:
                right.left.right = root
            right.left = root
            root.right = right
        else:
            if left is not None:
                root.right = left
            else:
                root.right = root
        return head

    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        return self.toCDLL(root)