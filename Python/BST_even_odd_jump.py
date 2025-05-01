# https://leetcode.com/problems/odd-even-jump
"""
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) 
 jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called 
 even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is
 the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is
 the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by
 jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

Example 1:
Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3],
 arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.

Example 2:
Input: arr = [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], 
 arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2],
 arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index,
 so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], 
 arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.

Example 3:
Input: arr = [5,1,3,4,2]
Output: 3
Explanation: We can reach the end from starting indices 1, 2, and 4.

Constraints:
1 <= arr.length <= 2 * 104
0 <= arr[i] < 105
"""

from typing import List

class BSTNode:
    def __init__(self, num, index):
        self.data = [num, index]
        self.right = None
        self.left = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None
    
    def insert_in_bst(self, num, index):
        BST.is_new_node = True
        BST.old_node = None
        self.root = BST._add_node(self.root, BSTNode(num, index))
        return (BST.is_new_node, BST.old_node)

    def get_balance(root):
        left = 0 if not root.left else root.left.height
        right = 0 if not root.right else root.right.height
        return left-right

    def get_height(root):
        left = 0 if not root.left else root.left.height
        right = 0 if not root.right else root.right.height
        return max(left, right) + 1

    def rotate_right(root):
        left = root.left
        left_right = left.right
        root.left = left_right
        left.right = root
        root.height = BST.get_height(root)
        left.height = BST.get_height(left)
        return left

    def rotate_left(root):
        right = root.right
        right_left = right.left
        root.right = right_left
        right.left = root
        root.height = BST.get_height(root)
        right.height = BST.get_height(right)
        return right

    def _add_node(root, node):
        if not root:
            return node
        elif root.data[0]<node.data[0]:
            root.right = BST._add_node(root.right, node)
        elif root.data[0]>node.data[0]:
            root.left = BST._add_node(root.left, node)
        else:
            BST.is_new_node = False
            BST.old_node = BSTNode(*root.data)
            root.data[1] = node.data[1]
            return root
        root.height = BST.get_height(root)
        balance = BST.get_balance(root)
        if balance>1 and root.left.data[0]>node.data[0]:
            root = BST.rotate_right(root)
        elif balance>1 and root.left.data[0]<node.data[0]:
            root.left = BST.rotate_left(root.left)
            root = BST.rotate_right(root)
        elif balance<-1 and root.right.data[0]<node.data[0]:
            root = BST.rotate_left(root)
        elif balance<-1 and root.right.data[0]>node.data[0]:
            root.right = BST.rotate_right(root.right)
            root = BST.rotate_left(root)
        return root
    
    def get_inorder_successor(root):
        right = root.right
        while right and right.left:
            right = right.left
        return right
    
    def get_inorder_predecessor(root):
        left = root.left
        while left and left.right:
            left = left.right
        return left

    def _get_next_small_big_node(root, num, small, big):
        # if root:
        #     print(f'{root.data=} {num=} {small=} {big=}')
        # else:
        #     print(f'{root=} {num=} {small=} {big=}')
        if not root: return (None, None)
        if root.data[0]>num:
           return BST._get_next_small_big_node(root.left, num, small, root)
        if root.data[0]<num:
            return BST._get_next_small_big_node(root.right, num, root, big)
        if root.data[0]==num:
            inorder_succ = BST.get_inorder_successor(root)
            inorder_pred = BST.get_inorder_predecessor(root)
            small = small if not inorder_pred else inorder_pred
            big = big if not inorder_succ else inorder_succ
            # print(f'{inorder_succ=} {inorder_pred=} {small=} {big=}')
            return (small, big)

    def get_next_small_big_node(self, num):
        return BST._get_next_small_big_node(self.root, num, None, None)

    def pre_order(root):
        if root:
            print(root.data, end='::')
            BST.pre_order(root.left)
            BST.pre_order(root.right)

    def print_pre(self):
        BST.pre_order(self.root)
        print()

    def in_order(root):
        if root:
            BST.in_order(root.left)
            print(root.data, end='::')
            BST.in_order(root.right)

    def print_in(self):
        BST.in_order(self.root)
        print()


class Solution:

    # Will timeout
    def oddEvenJumps1(self, arr: List[int]) -> int:
        count = 0
        arr_len = len(arr)
        greater_eql_stack = list()
        smaller_eql_stack = list()
        op_map = dict() # {index : (odd_step_bool, even_step_bool)}
        for i in range(arr_len-1, -1, -1):
            num = arr[i]
            if greater_eql_stack and arr[greater_eql_stack[-1]]<num:
                while greater_eql_stack and arr[greater_eql_stack[-1]]<num:
                    smaller_eql_stack.append(greater_eql_stack.pop())
            else:
                while smaller_eql_stack and arr[smaller_eql_stack[-1]]>num:
                    greater_eql_stack.append(smaller_eql_stack.pop())
            odd_jump_index = greater_eql_stack[-1] if greater_eql_stack else None
            even_jump_index = smaller_eql_stack[-1] if smaller_eql_stack else None
            # print(f'{i=} {arr[i]=} {greater_eql_stack=} {smaller_eql_stack=}')
            if not odd_jump_index and not even_jump_index: # Last index case
                op_map[i] = (True, True)
            else:
                odd_jump_index = even_jump_index if (even_jump_index and arr[even_jump_index]==num) else odd_jump_index
                even_jump_index = odd_jump_index if (odd_jump_index and arr[odd_jump_index]==num) else even_jump_index
                odd_result = False if not odd_jump_index else op_map[odd_jump_index][1]
                even_result = False if not even_jump_index else op_map[even_jump_index][0]
                op_map[i] = (odd_result, even_result)
            count+=(1 if op_map[i][0] else 0)
            if smaller_eql_stack and arr[smaller_eql_stack[-1]]==num:
                smaller_eql_stack[-1] = i # same num case
            elif greater_eql_stack and arr[greater_eql_stack[-1]]==num:
                greater_eql_stack[-1] = i
            else:
                greater_eql_stack.append(i)
            # print(f'{odd_jump_index=} {even_jump_index=}')
            # print(f'--{greater_eql_stack=} {smaller_eql_stack=}')
            # print(f'{op_map=}')
        return count
    
    def oddEvenJumps(self, arr: List[int]) -> int:
        count = 0
        arr_len = len(arr)
        op_map = dict() # {index : (odd_step_bool, even_step_bool)}
        bst = BST()
        for i in range(arr_len-1, -1, -1):
            num = arr[i]
            is_new_node, old_node = bst.insert_in_bst(num, i)
            if not is_new_node:
                small_node, big_node = old_node, old_node
            else:
                small_node, big_node = bst.get_next_small_big_node(num)
            # print(f'{num=} {small_node=} {big_node=}')
            if not small_node and not big_node:
                op_map[i] = (True, True)
            else:
                odd_jump_index = small_node.data[1] if (small_node and small_node.data[0]==num) else (big_node.data[1] if big_node else None)
                even_jump_index = big_node.data[1] if (big_node and big_node.data[0]==num) else (small_node.data[1] if small_node else None)
                odd_result = False if not odd_jump_index else op_map[odd_jump_index][1]
                even_result = False if not even_jump_index else op_map[even_jump_index][0]
                op_map[i] = (odd_result, even_result)
            count+=(1 if op_map[i][0] else 0)
            # bst.print_pre()
            # bst.print_in()
        return count