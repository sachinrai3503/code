# https://www.geeksforgeeks.org/find-maximum-sum-triplets-array-j-k-ai-aj-ak
"""
Given an array of positive integers of size n. Find the maximum sum of triplet
 ( ai + aj + ak ) such that 0 <= i < j < k < n and ai < aj < ak. 

Input: a[] = 2 5 3 1 4 9
Output: 16
Explanation:
All possible triplets are:-
2 3 4 => sum = 9
2 5 9 => sum = 16
2 3 9 => sum = 14
3 4 9 => sum = 16
1 4 9 => sum = 14
Maximum sum = 16
"""

from sys import maxsize

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def set_height(self):
        left = self.left.height if self.left else 0
        right = self.right.height if self.right else 0
        self.height = max(left, right) + 1
    
    def get_height(self):
        return self.height
    
    def get_balance_factor(self):
        left = self.left.height if self.left else 0
        right = self.right.height if self.right else 0
        return left-right

    def __str__(self):
        return ":".join([str(self.data)])

    def __repe__(self):
        return self.__str__()

class HeightBalancedBST:
    def __init__(self):
        self.root = None
    
    def pre(self, root):
        if root is None: return
        print(root, end = ' ')
        self.pre(root.left)
        self.pre(root.right)
    
    def print_tree(self):
        self.pre(self.root)
        print()
    
    def right_rotate(self, node):
        a = node
        b = node.left
        d = b.right
        b.right = a
        a.left = d
        a.set_height()
        b.set_height()
        return b

    def left_rotate(self, node):
        a = node
        c = a.right
        d = c.left
        a.right = d
        c.left = a
        a.set_height()
        c.set_height()
        return c
    
    def insert_node(self, root, data):
        if root is None: return data
        if root.data>data.data: root.left = self.insert_node(root.left, data)
        if root.data<data.data: root.right = self.insert_node(root.right, data)
        root.set_height()
        balance_factor = root.get_balance_factor()
        if balance_factor>1:
            if root.left.data>data.data:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor<-1:
            if root.right.data<data.data:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root
    
    def insert_in_BST(self, data):
        self.root = self.insert_node(self.root, BSTNode(data))

    def get_floor(self, root, data):
        _floor = None
        while root:
            if root.data<data:
                _floor = root.data
                root = root.right
            else:
                root = root.left
        return _floor

    def find_floor(self, data):
        return self.get_floor(self.root, data)

class Solution:
    def get_max_suffix(self, arr, length):
        max_arr = [None for i in range(length)]
        _max = -maxsize
        for i in range(length-1, -1, -1):
            _max = max(_max, arr[i])
            max_arr[i] = _max
        return max_arr

    def find_max_sum_triplet(self, arr:list[int]) -> int:
        max_sum = -maxsize
        length = len(arr)
        max_num_to_right = self.get_max_suffix(arr, length)
        bst = HeightBalancedBST()
        for i in range(length-1):
            max_to_right = max_num_to_right[i+1]
            floor_to_left = bst.find_floor(arr[i])
            if floor_to_left is not None and arr[i]<max_to_right:
                max_sum = max(max_sum, floor_to_left + arr[i] + max_to_right)
            bst.insert_in_BST(arr[i])
            # bst.print_tree()
        return max_sum
    
def main():
    arr = [2 ,5 ,3, 1, 4, 9]
    sol = Solution()
    print(sol.find_max_sum_triplet(arr))

if __name__ == '__main__' :
    main()