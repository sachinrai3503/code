# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs
"""
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum
 difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| 
 represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

Example 1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Example 2:
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 
Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= p <= (nums.length)/2
"""

from sys import maxsize
from typing import List

class Heap:
    def __init__(self, size):
        self.cur_size = 0
        self.max_size = size
        self.data = [None for i in range(size)]
    
    def is_empty(self):
        return self.cur_size==0
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def compare(self, i, j):
        pass
    
    def heapify(self, i):
        pass
    
    def get_top(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.data[0]
    
    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.cur_size+=1
            self.data[index] = data
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2

    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.data[0] = self.data[self.cur_size]
            self.heapify(0)
            return temp

class MaxHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def compare(self, i, j):
        if self.data[i]>self.data[j]: return -1
        if self.data[j]>self.data[i]: return 1
        return 0
    
    def heapify(self, index):
        left = (index*2)+1
        right = (index*2)+2
        max_index = index
        if left<self.cur_size and self.compare(left, max_index)==-1:
            max_index = left
        if right<self.cur_size and self.compare(right, max_index)==-1:
            max_index = right
        if index!=max_index:
            self.swap(max_index, index)
            self.heapify(max_index)

class Solution:

    # This is wrong. Doesn't factor in index appearing only in 1 pair requirement,
    def minimizeMax1(self, nums: List[int], p: int) -> int:
        if p<=0: return 0
        nums_len = len(nums)
        max_heap = MaxHeap(p)
        nums.sort()
        prev = nums[0]
        print(f'{nums=}')
        for i in range(1, nums_len):
            diff = nums[i] - prev
            if max_heap.is_empty() or not max_heap.is_full():
                max_heap.insert_in_heap(diff)
            elif diff<max_heap.get_top():
                max_heap.delete_top()
                max_heap.insert_in_heap(diff)
            prev = nums[i]
            print(f'loop {max_heap.data[:max_heap.cur_size]}')
        print(f'{max_heap.data[:max_heap.cur_size]}')
        op = max_heap.get_top()
        return op if op!=None else 0

    # This will time out
    def minimizeMax2(self, nums: List[int], p: int) -> int:
        if p<=0: return 0
        nums_len = len(nums)
        nums.sort()
        # diff_arr = [nums[i+1] - nums[i] for i in range(nums_len-1)]
        diff_arr_len = nums_len - 1
        dp = [[0 for i in range(diff_arr_len)] for j in range(2)]
        # print(f'{nums=}')
        # print(f'{diff_arr=} {diff_arr_len=}')
        # print(f'{dp=}')
        for tp in range(p):
            cur_row = tp%2
            prev_row = 0 if cur_row==1 else 1
            start_from = diff_arr_len - tp*2 -1
            # print(f'{tp=} {cur_row=} {prev_row=} {start_from=}')
            for i in range(start_from, -1, -1):
                # print(f'{i=}')
                # print(f'{diff_arr[i]=}')
                # print(f'{dp[prev_row][i+2]=}')
                t_diff = nums[i+1]-nums[i]
                t_val = max(t_diff, dp[prev_row][i+2]) if (i+2)<diff_arr_len else t_diff
                dp[cur_row][i] = min(t_val, dp[cur_row][i+1]) if i<start_from else t_val
            # print(f'{dp[cur_row]=}')
        return dp[(p-1)%2][0]

    def count_valid_pairs(self, nums, nums_len, max_diff):
        count = 0
        i = 1
        while i<nums_len:
            if (nums[i]-nums[i-1])<=max_diff:
                count+=1
                i+=2
            else:
                i+=1
        return count

    def minimizeMax(self, nums: List[int], p: int) -> int:
        op = maxsize
        if p<=0: return 0
        nums_len = len(nums)
        nums.sort()
        s, e = 0, nums[-1] - nums[0]
        while s<=e:
            mid = s + (e-s)//2
            # print(f'{s=} {e=} {mid=}')
            if self.count_valid_pairs(nums, nums_len, mid)>=p:
                op = mid
                e = mid-1
            else:
                s = mid+1
        return op