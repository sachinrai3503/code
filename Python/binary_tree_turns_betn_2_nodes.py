# https://www.geeksforgeeks.org/number-turns-reach-one-node-binary-tree/
"""
Given a binary tree and two nodes. The task is to count the number of turns needed 
 to reach from one node to another node of the Binary tree.

Examples:  
Input:   Below Binary Tree and two nodes
        5 & 6 
                   1
                /     \
               2        3
             /   \    /   \
            4     5   6     7
           /         / \
          8         9   10
Output: Number of Turns needed to reach 
from 5 to 6:  3
        
Input: For above tree if two nodes are 1 & 4
Output: Straight line : 0 turn  
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None
    
    def __repr__(self):
        return str(self.val)

class Tree:
    def __init__(self):
        self.root = None
    
    def _insert(self, root, val):
        if root is None: return TreeNode(val)
        if root.val>val: root.left = self._insert(root.left, val)
        elif root.val<val: root.right = self._insert(root.right, val)
        return root
    
    def add_nodes(self, ip:list):
        for val in ip:
            self.root = self._insert(self.root, val)
    
    def _print(self, root):
        if root:
            print(root.val, end = ' ')
            self._print(root.left)
            self._print(root.right)

    def print_pre_order(self):
        self._print(self.root)
        print()

class Solution:

    def __init__(self):
        self.s = 0
        self.other = None

    def count_turn_from(self, root, cur_child, dest):
        if root is None: return None
        if root.val == dest: return 0
        left = self.count_turn_from(root.left, 'L', dest)
        if left!=None:
            if cur_child=='R': return left+1
            return left
        right = self.count_turn_from(root.right, 'R', dest)
        if right!=None:
            if cur_child=='L': return right+1
            return right
        return None
    

    def count_turn_in_path(self, root, src, dest, cur_child):
        if root is None: return None
        if root.val==src or root.val==dest:
            self.s = 1
            self.other = dest if root.val==src else src
            t_turn = self.count_turn_from(root, 'N', self.other)
            if t_turn!=None:
                self.s = 2
                return t_turn
            return 0
        left = self.count_turn_in_path(root.left, src, dest, 'L')
        if self.s==2: return left
        if self.s==1:
            t_turn = self.count_turn_from(root.right, 'R', self.other)
            if t_turn!=None:
                self.s = 2
                return left + t_turn + 1
            return left + (1 if cur_child=='R' else 0)
        right = self.count_turn_in_path(root.right, src, dest, 'R')
        if self.s==2: return right
        if self.s==1: return right + (1 if cur_child=='L' else 0)
        return None

def main():
    ip = [700,300,200,100,50,150,140,110,115,114,120,400,430,450,500,475,465,460,480,477,478,485,482,486,1000,1500,1300,1250,1200,1275,1400,2000,2500,2200]
    src, dest = 1275, 115
    tree = Tree()
    tree.add_nodes(ip)
    tree.print_pre_order()
    sol = Solution()
    print('Turn = ', sol.count_turn_in_path(tree.root, src, dest, 'N'), sol.s, sol.other)

if __name__ == '__main__':
    main()