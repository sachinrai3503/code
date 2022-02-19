# https://leetcode.com/problems/count-of-range-sum
"""
Given an integer array nums and two integers lower and upper, return the number
 of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices
 i and j inclusive, where i <= j.

Example 1:
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

Example 2:
Input: nums = [0], lower = 0, upper = 0
Output: 1
 
Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
The answer is guaranteed to fit in a 32-bit integer.
"""

from sys import maxsize

class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.mid = (low+high)//2
        self.count = 0
        self.left = self.right = None
    
    def __str__(self):
        return ":".join([str(self.low), str(self.high), str(self.mid), str(self.count)])

    def __repr__(self):
        return self.__str__()
    
    # This method is meant for leaf nodes. Handles multiple occ. of same prefix sum
    def increase_count(self):
        self.count+=1
    
    def update_count(self):
        left_count = self.left.count if self.left else 0
        right_count = self.right.count if self.right else 0
        self.count = left_count + right_count
    
    
class SegmentTree:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.root = None
    
    def _pre(self, root):
        if root:
            print(root, end=' ')
            self._pre(root.left)
            self._pre(root.right)
    
    def print_seg_tree(self):
        self._pre(self.root)
        print()
    
    def _update_segment_tree(self, root, low, high, index):
        if index<low or index>high: return
        if root is None:
            root = SegmentTreeNode(low, high)
        if high==low:
            root.increase_count()
            return root
        if root.mid>=index:
            root.left = self._update_segment_tree(root.left, low, root.mid, index)
        elif root.mid<index:
            root.right = self._update_segment_tree(root.right, root.mid+1, high, index)
        root.update_count()
        return root
        
    def update_node(self, index):
        self.root = self._update_segment_tree(self.root, self.low, self.high, index)
    
    def _query_seg_tree(self, root, s, e):
        if root is None:
            return 0
        low, high = root.low, root.high
        if s>e or not (s>=low and e<=high):
            print('Fatal')
            return None
        if low==s and high==e:
            return root.count
        if e<=root.mid:
            return self._query_seg_tree(root.left, s, e)
        elif s>root.mid:
            return self._query_seg_tree(root.right, s, e)
        else:
            left = self._query_seg_tree(root.left, s, root.mid)
            right = self._query_seg_tree(root.right, root.mid+1, e)
            return left+right
    
    def query_range(self, s, e):
        return self._query_seg_tree(self.root, s, e)
    
class BSTNode:
    def __init__(self, data, subtree_node_count=1):
        self.data = data
        self.subtree_node_count = subtree_node_count
        self.extra = 0
        self.height = 1
        self.left, self.right = None, None

    def __str__(self):
        return ':'.join([str(self.data), str(self.extra) ,str(self.subtree_node_count), str(self.height)])
        
    def __repr__(self):
        return self.__str__()
    
    def set_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        self.height = max(left_height, right_height) + 1
    
    def get_height(self):
        return self.height

    def get_balance_factor(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return left_height - right_height
    
    def set_subtree_node_count(self):
        left_count = self.left.subtree_node_count if self.left else 0
        right_count = self.right.subtree_node_count if self.right else 0
        self.subtree_node_count = left_count + right_count + 1 + self.extra
    
    def get_left_subtree_node_count(self):
        return self.subtree_node_count - (self.right.subtree_node_count if self.right else 0)
    
# This is height balanced BST
class BST:
    
    def __init__(self):
        self.root = None
    
    def _pre(self, node):
        if node:
            print(node, end = ' ')
            self._pre(node.left)
            self._pre(node.right)
    
    def print_BST(self):
        self._pre(self.root)
        print()
    
    def right_rotate(self, root):
        a = root
        b = root.left
        c = b.right
        b.right = a
        a.left = c
        a.set_height()
        a.set_subtree_node_count()
        b.set_height()
        b.set_subtree_node_count()
        return b
    
    def left_rotate(self, root):
        a = root
        b = root.right
        c = b.left
        b.left = a
        a.right = c
        a.set_height()
        a.set_subtree_node_count()
        b.set_height()
        b.set_subtree_node_count()
        return b

    def _insert_node(self, root, node):
        if root==None: return node
        if root.data<node.data:
            root.right = self._insert_node(root.right, node)
        elif root.data>node.data:
            root.left = self._insert_node(root.left, node)
        else:
            root.extra+=1
        root.set_height()
        root.set_subtree_node_count()
        balance_factor = root.get_balance_factor()
        if balance_factor>1 and node.data<root.left.data:
            return self.right_rotate(root)
        elif balance_factor>1 and node.data>root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        elif balance_factor<-1 and node.data>root.right.data:
            return self.left_rotate(root)
        elif balance_factor<-1 and node.data<root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
        
    def insert(self, data):
        self.root = self._insert_node(self.root, BSTNode(data))

    def get_count_of_nodes_wiht_val_less_k(self, k):
        count = 0
        _root = self.root
        while _root:
            if _root.data==k:
                return count + _root.get_left_subtree_node_count()
            if _root.data<k:
                count+=_root.get_left_subtree_node_count()
                _root = _root.right
            elif _root.data>k:
                _root = _root.left
        return count
        
class BIT:
    def __init__(self, length):
        self.data = [0 for i in range(length)]
        self.length = length
    
    def update(self, index, value):
        while index<self.length:
            # print(index)
            self.data[index]+=value
            index+=(index&-index)
    
    def query(self, index):
        count = 0
        while index>0:
            count+=self.data[index]
            index-=(index&-index)
        return count    
        
class Solution:
    
    def get_prefix_sum(self, nums, length):
        pre_sum = [0 for i in range(length)]
        t_sum = 0
        for i in range(length):
            t_sum+=nums[i]
            pre_sum[i] = t_sum
        return pre_sum
    
    # This is not time efficient solution
    def countRangeSum1(self, nums: list[int], lower: int, upper: int) -> int:
        length = len(nums)
        pre_sum = self.get_prefix_sum(nums, length)
        count = 0
        for i in range(length):
            t_sum = 0 if i==0 else pre_sum[i-1]
            for j in range(i, length):
                if lower<=(pre_sum[j]-t_sum)<=upper:
                    count+=1
        return count

    # Uses BIT using below concept. Note - This will lead to out of memory exception
    # L<=Sum[i,j]<=U 
    # L<=preSum[j]-preSum[i-1]<=U 
    # (preSum[j]-upper)<=preSum[i-1]<=(preSum[j]-lower) for all 0<i<=j
    def countRangeSum_BIT(self, nums: list[int], lower: int, upper: int) -> int:
        count = 0
        length = len(nums)
        pre_sum = [0 for i in range(length)]
        num_max, num_min = -maxsize, maxsize
        pre_max, pre_min = -maxsize, maxsize
        t_sum = 0
        for i in range(length):
            t_sum+=nums[i]
            num_max = max(num_max, nums[i])
            num_min = min(num_min, nums[i])
            pre_max = max(pre_max, t_sum)
            pre_min = min(pre_min, t_sum)
            pre_sum[i] = t_sum
        if (num_max<=0 and num_max<lower) or (num_min>=0 and num_min>upper): return 0
        min_v, max_v = min(pre_min, pre_min - upper), max(pre_max, pre_max - lower)
        bit_len = max_v - min_v + 2
        base_index = -min_v + 1
        # print(pre_sum, num_max, num_min, pre_max, pre_min, min_v, max_v, bit_len, base_index)
        bit = BIT(bit_len)
        for i in range(length):
            t_index = base_index + pre_sum[i]
            # bit.update(t_index, 1) # This is wrong. Note - (i-1) in (x<=p[i-1]<=y) for 0<i<=j.
            if lower<=pre_sum[i]<=upper: count+=1
            count+=(bit.query(t_index-lower) - bit.query(t_index-upper-1))
            bit.update(t_index, 1)
            # print(t_index, t_index-lower, t_index-upper,  bit.data, count)
        return count
    
    # Uses BST using below concept. This too will take lot of time.
    # L<=Sum[i,j]<=U 
    # L<=preSum[j]-preSum[i-1]<=U for all 0<=i<=j
    # (preSum[j]-upper)<=preSum[i-1]<=(preSum[j]-lower) for all 0<i<=j
    def countRangeSum_BST(self, nums: list[int], lower: int, upper: int) -> int:
        count = 0
        length = len(nums)
        pre_sum = list()
        # num_max, num_min = -maxsize, maxsize # Commented min max to make it fast. Logic is relevant.
        t_sum = 0
        for i in range(length):
            t_sum+=nums[i]
            # num_max = max(num_max, nums[i])
            # num_min = min(num_min, nums[i])
            pre_sum.append(t_sum)
        # print(pre_sum)
        # if (num_max<=0 and num_max<lower) or (num_min>=0 and num_min>upper): return 0
        bst = BST()
        for i in range(length):
            pre_sum_i = pre_sum[i]
            if lower<=pre_sum_i<=upper: count+=1
            count+=(bst.get_count_of_nodes_wiht_val_less_k(pre_sum_i-lower) - bst.get_count_of_nodes_wiht_val_less_k(pre_sum_i-upper-1))
            bst.insert(pre_sum_i)
            # print(count)
            # bst.print_BST()
        return count
    
    # Uses Segment tree using below concept. Note - This seg. tree is not implemented using arr.
    # NOTE - This too will run out of time
    # L<=Sum[i,j]<=U 
    # L<=preSum[j]-preSum[i-1]<=U for all 0<=i<=j
    # (preSum[j]-upper)<=preSum[i-1]<=(preSum[j]-lower) for all 0<i<=j
    def countRangeSum_SEG(self, nums: list[int], lower: int, upper: int) -> int:
        count = 0
        length = len(nums)
        pre_sum = list()
        num_max, num_min = -maxsize, maxsize
        pre_max, pre_min = -maxsize, maxsize
        t_sum = 0
        for i in range(length):
            t_sum+=nums[i]
            num_max = max(num_max, nums[i])
            num_min = min(num_min, nums[i])
            pre_max = max(pre_max, t_sum)
            pre_min = min(pre_min, t_sum)
            pre_sum.append(t_sum)
        if (num_max<=0 and num_max<lower) or (num_min>=0 and num_min>upper): return 0
        min_v, max_v = min(pre_min, pre_min - upper), max(pre_max, pre_max - lower)
        # print(pre_sum, num_max, num_min, pre_max, pre_min, min_v, max_v)
        seg_tree = SegmentTree(min_v, max_v)
        for i in range(length):
            pre_sum_i = pre_sum[i]
            if lower<=pre_sum_i<=upper: count+=1
            count+=seg_tree.query_range(pre_sum_i-upper, pre_sum_i-lower)
            seg_tree.update_node(pre_sum_i)
            # print(count)
            # seg_tree.print_seg_tree()
        return count
    
    def floor_count(self, arr, s, e, k):
        t_s = s
        _floor = s-1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]<=k:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor - t_s + 1
    
    def merge_count(self, arr, s, e, mid, lower, upper):
        count = 0
        j = mid+1
        while j<=e:
            low, high = arr[j]-upper, arr[j]-lower
            count+=(self.floor_count(arr, s, mid, high) - self.floor_count(arr, s, mid, low-1))
            # print('==', arr[j], low, high, count)
            j+=1
        temp = list()
        i, j = s, mid+1
        while i<=mid and j<=e:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=e:
            temp.append(arr[j])
            j+=1
        arr[s:e+1] = temp
        # print('--', arr[s:e+1], s, e, count)
        return count
    
    def merge_sort_and_count(self, pre_sum, s, e, lower, upper):
        if s>e:
            print('Fatal')
            return None
        if s==e:
            return 1 if lower<=pre_sum[s]<=upper else 0
        mid = s + (e-s)//2
        left_count = self.merge_sort_and_count(pre_sum, s, mid, lower, upper)
        right_count = self.merge_sort_and_count(pre_sum, mid+1, e, lower, upper)
        # print(pre_sum[s:e+1], s, e, left_count, right_count)
        return left_count + right_count + self.merge_count(pre_sum, s, e, mid, lower, upper)
    
    # Uses merge sort using below concept. 
    # L<=Sum[i,j]<=U 
    # L<=preSum[j]-preSum[i-1]<=U for all 0<=i<=j
    # (preSum[j]-upper)<=preSum[i-1]<=(preSum[j]-lower) for all 0<i<=j
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        length = len(nums)
        pre_sum = list()
        num_max, num_min = -maxsize, maxsize
        t_sum = 0
        for i in range(length):
            t_sum+=nums[i]
            num_max = max(num_max, nums[i])
            num_min = min(num_min, nums[i])
            pre_sum.append(t_sum)
        if (num_max<=0 and num_max<lower) or (num_min>=0 and num_min>upper): return 0
        # print(pre_sum)
        return self.merge_sort_and_count(pre_sum, 0, length-1, lower, upper)