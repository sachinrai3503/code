# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
 where 0 <= i <= j < n.

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 
Constraints:
1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
"""

from math import log2, ceil

class TrieCell:
    def __init__(self, val, is_last=False):
        self.val = val
        self.child = None
        self.is_last = is_last
    
    def print_trie_cell(self, op):
        op.append(str(self.val))
        if self.is_last:
            print(''.join(op))
        if self.child: self.child.print_trie_node(op)
        op.pop()

class TrieNode:
    
    size = 2
    
    def __init__(self, size=2):
        self.data = [None, None] # [trieCell, trieCell]
    
    def print_trie_node(self, op):
        for i in range(TrieNode.size):
            if self.data[i]:
                self.data[i].print_trie_cell(op)
    
    def insert_data(node, num, i_bit_set):
        if i_bit_set==0: return node
        if not node: node = TrieNode()
        num_i_bit = 0 if (num&i_bit_set)==0 else 1
        cell = node.data[num_i_bit]
        if not cell:
            cell = TrieCell(num_i_bit)
            node.data[num_i_bit] = cell
        cell.is_last = (i_bit_set==1)
        cell.child = TrieNode.insert_data(cell.child, num, i_bit_set>>1)
        return node

class Trie:
    def __init__(self, max_bit_needed):
        self.root = None
        Trie.max_bit_needed = max_bit_needed
    
    def insert_in_trie(self, num):
        i_bit_set = 1<<(Trie.max_bit_needed-1) # setting the MSB bit
        self.root = TrieNode.insert_data(self.root, num, i_bit_set)
    
    def print_trie(self):
        op = list()
        self.root.print_trie_node(op)

class Solution:
           
    # O(n2) - will timeout
    def findMaximumXOR1(self, nums: List[int]) -> int:
        max_xor = 0
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i, nums_len):
                max_xor = max(max_xor, nums[i]^nums[j])
        return max_xor
    
    def to_decimal(self, op):
        num = 0
        max_bit = len(op)
        # print(max_bit)
        for i in range(max_bit):
            if op[i]==1:
                num|=(1<<(max_bit-1-i))
                # print(op, i, num)
        return num
    
    def get_max_xor(self, op, node1, node2=None):
        if not node1 and not node2:
            self.max_xor = max(self.max_xor, self.to_decimal(op))
            return
        elif not node2:
            if node1.data[0] and node1.data[1]:
                op.append(1)
                self.get_max_xor(op, node1.data[0].child, node1.data[1].child)
            else:
                op.append(0)
                self.get_max_xor(op, node1.data[0].child if node1.data[0] else node1.data[1].child)
        else: # both node1 and node2 is not None
            if node1.data[0] and node1.data[1] and node2.data[0] and node2.data[1]:
                op.append(1)
                self.get_max_xor(op, node1.data[0].child, node2.data[1].child)
                self.get_max_xor(op, node1.data[1].child, node2.data[0].child)
            elif node1.data[0] and node2.data[1]:
                op.append(1)
                self.get_max_xor(op, node1.data[0].child, node2.data[1].child)
            elif node1.data[1] and node2.data[0]:
                op.append(1)
                self.get_max_xor(op, node1.data[1].child, node2.data[0].child)
            elif node1.data[0] and node2.data[0]:
                op.append(0)
                self.get_max_xor(op, node1.data[0].child, node2.data[0].child)
            elif node1.data[1] and node2.data[1]:
                op.append(0)
                self.get_max_xor(op, node1.data[1].child, node2.data[1].child)
        op.pop() 
                
    # Based on trie - O(n) as max of 32 bit in any number
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num==0: return 0
        trie = Trie(int(log2(max_num))+1)
        for num in nums:
            trie.insert_in_trie(num)
        # trie.print_trie()
        # print(max_num, trie.max_bit_needed)
        op = list()
        self.max_xor = 0
        self.get_max_xor(op, trie.root)
        return self.max_xor