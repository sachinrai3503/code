# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
# https://www.geeksforgeeks.org/connect-nodes-at-same-level-with-o1-extra-space
# https://www.geeksforgeeks.org/connect-nodes-at-same-level/


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:

    # https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    # This is for a perfect binary tree
    def connect_perfect_binary_tree(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        que = deque()
        que.append(root)
        que.append(None)
        while que[0]!=None:
            prev = None
            while que[0]!=None:
                temp = que.popleft()
                left, right = temp.left, temp.right
                if left is None: return root
                if prev: prev.next = left
                left.next = right
                prev = right
                que.append(left)
                que.append(right)
            que.popleft()
            que.append(None)
        return root

    # https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
    # This is for any binary tree
    def connect_binary_tree(self, root: 'Node') -> 'Node':
        if not root: return root
        que = deque()
        que.append(root)
        que.append(None)
        while que[0]!=None:
            prev = None
            while que[0]!=None:
                temp = que.popleft()
                left, right = temp.left, temp.right
                if left is not None:
                    if prev: prev.next = left
                    prev = left
                    que.append(left)
                if right is not None:
                    if prev: prev.next = right
                    prev = right
                    que.append(right)
            que.popleft()
            que.append(None)
        return root

    # This is without que. O(1) space
    def connect_binary_tree2(self, root: 'Node') -> 'Node':
        t_root = root
        while root:
            next_root = None
            prev = None
            while root:
                left, right = root.left, root.right
                if left is not None:
                    if prev: prev.next = left
                    prev = left
                    if next_root is None: next_root = left
                if right is not None:
                    if prev: prev.next = right
                    prev = right
                    if next_root is None: next_root = right
                root = root.next
            root = next_root
        return t_root