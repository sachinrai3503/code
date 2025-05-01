# https://leetcode.com/problems/longest-increasing-subsequence-ii
"""
You are given an integer array nums and an integer k.

Find the longest subsequence of nums that meets the following requirements:

The subsequence is strictly increasing and
The difference between adjacent elements in the subsequence is at most k.
Return the length of the longest subsequence that meets the requirements.

A subsequence is an array that can be derived from another array by deleting some 
 or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation:
The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger than 3.

Example 2:
Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation:
The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.

Example 3:
Input: nums = [1,5], k = 1
Output: 1
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.
 
Constraints:
1 <= nums.length <= 105
1 <= nums[i], k <= 105
"""

from typing import List

class TreeNode:
    def __init__(self, num, lis_len):
        self.num = num
        self.lis_len = lis_len
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f'{self.num=} {self.lis_len=}'# {self.left=} {self.right=}' 

class SegementTree:
    def __init__(self, s, e):
        self.root = None
        self.s = s
        self.e = e
    
    def get_lis_len(self, node):
        if node:
            return node.lis_len
        else:
            return 0

    def _insert_node(self, root, s, e, node):
        if s==e and s==node.num:
            if root:
                node.lis_len = max(node.lis_len, root.lis_len)
            return node
        mid = s + (e-s)//2
        if not root:
            root = TreeNode(-1, 0)
        if node.num<=mid:
            root.left = self._insert_node(root.left, s, mid, node)
        else:
            root.right = self._insert_node(root.right, mid+1, e, node)
        root.lis_len = max(root.lis_len, max(self.get_lis_len(root.left), self.get_lis_len(root.right)))
        return root

    def insert_data(self, num, lis_len):
        self.root = self._insert_node(self.root, self.s, self.e, TreeNode(num, lis_len))

    def _query_between_range(self, root, s, e, l, r):
        if s>e or l>r: return None
        if l>e: return 0
        if r<s: return 0
        if not root: return 0
        if s==l and e==r: return root.lis_len
        if s==e: return root.lis_len
        mid = s + (e-s)//2
        if l>mid:
            return self._query_between_range(root.right, mid+1, e, l, r)
        elif r<=mid:
            return self._query_between_range(root.left, s, mid, l, r)
        else:
            return max( self._query_between_range(root.left, s, mid, l, mid), 
                        self._query_between_range(root.right, mid+1, e,  mid+1, r,))

    def query_range(self, l, r):
        return self._query_between_range(self.root, self.s, self.e, l, r)
    
    def pre_order(self, root):
        if root:
            print(f'{root}')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def print(self):
        self.pre_order(self.root)

class Solution:

    # Will time out
    def lengthOfLIS_dp(self, nums: List[int], k: int) -> int:
        max_len = 0
        nums_len = len(nums)
        dp = [None for i in range(nums_len)]
        for i in range(nums_len-1, -1, -1):
            num_i = nums[i]
            t_len = 0
            for j in range(i+1, nums_len):
                if (nums[j]>num_i) and (nums[j]-num_i)<=k:
                    t_len = max(t_len, dp[j])
            dp[i] = t_len + 1
            max_len = max(max_len, dp[i])
        # print(f'{dp=}')
        return max_len
    
    # This is segment tree method
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_len = 0
        nums_len = len(nums)
        min_num, max_num = min(nums), max(nums)
        seg_tree = SegementTree(min_num, max_num)
        for num in nums:
            lis_within_k = seg_tree.query_range(num-k, num-1)
            seg_tree.insert_data(num, lis_within_k+1)
            # print(f'{num=} {lis_within_k=} {num-k=} {num-1=}')
            # seg_tree.print()
        return seg_tree.query_range(min_num, max_num)