# https://leetcode.com/problems/maximum-subsequence-score
"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n
 and a positive integer k. You must choose a subsequence of indices from nums1 
 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the
 selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * 
 min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set
 {0, 1, ..., n-1} by deleting some or no elements.

Example 1:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Example 2:
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum
 possible score.

Constraints:
n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[j] <= 105
1 <= k <= n
"""

from sys import maxsize
from typing import List

class Heap:
    def __init__(self, size, arr2):
        self.cur_size = size
        self.max_size = size
        self.data = [(i, arr2[i]) for i in range(size)]

    def __repr__(self):
        return f'{self.data[:self.cur_size]}'

    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0
    
    def compare(self, i, j):
        pass
    
    def heapify(self, i):
        pass
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.heapify(0)
            return temp
        
    def build_heap(self):
        parent_index = (self.cur_size-2)//2
        while parent_index>=0:
            self.heapify(parent_index)
            parent_index-=1

    def get_top(self):
        if self.is_empty():
            print('None')
            return None
        return self.data[0]

class MinHeap(Heap):

    def heapify(self, i):
        left = i*2+1
        right = i*2+2
        min_index = i
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if min_index!=i:
            self.swap(min_index, i)
            self.heapify(min_index)

    def compare(self, i, j):
        if self.data[i][1]<self.data[j][1]: return -1
        if self.data[i][1]>self.data[j][1]: return 1
        return 0

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_score = 0
        nums_len = len(nums1)
        nums1_index = [i for i in range(nums_len)]
        nums1_index.sort(key = lambda i : nums1[i])
        # print(f'{nums1=} {nums1_index=}')
        minHeap = MinHeap(nums_len, nums2)
        minHeap.build_heap()
        # print(f'{minHeap=}')
        visited = set()
        count = 0
        t_sum = 0
        i = nums_len-1
        while not minHeap.is_empty():
            # print(f'{minHeap=}')
            min_index, min_num = minHeap.delete_top()
            req_sum=nums1[min_index]
            if min_index in visited:
                count-=1
                t_sum-=nums1[min_index]
            nums1[min_index] = -maxsize
            while count<(k-1) and i>=0:
                if nums1[nums1_index[i]]!=-maxsize:
                    t_sum+=nums1[nums1_index[i]]
                    count+=1
                visited.add(nums1_index[i])
                i-=1
            req_sum+=t_sum
            # print(f'{min_index=} {min_num=} {req_sum=} {count=} {t_sum=} {i=} {min_num*req_sum=} {visited=}')
            if count==(k-1):
                max_score = max(max_score, min_num*req_sum)
            else:
                break
        return max_score