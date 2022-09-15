# https://leetcode.com/problems/largest-number/
# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
# https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/
"""
Given a list of non-negative integers nums, arrange them such that they form the 
 largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
    
class Heap:
    def __init__(self, data, length):
        self.data = data
        self.cur_size = length
        self.max_size = length
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _compare(self, i, j):
        num1, num2 = self.data[i], self.data[j]
        t_num1_num2 = num1+num2
        t_num2_num1 = num2+num1
        t_len = len(t_num1_num2)
        i, j = 0, 0
        while i<t_len:
            if t_num1_num2[i]>t_num2_num1[j]: return 1
            elif t_num1_num2[i]<t_num2_num1[j]: return -1
            i+=1
            j+=1
        return 0

    def min_heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self._compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self._compare(right, min_index)==-1:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.min_heapify(min_index)
    
    def heapify(self):
        parent_index = (self.cur_size-2)//2
        while parent_index>=0:
            self.min_heapify(parent_index)
            parent_index-=1
    
    def sort(self):
        self.heapify()
        while self.cur_size>1:
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.min_heapify(0)

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_len = len(nums)
        nums_str = [str(num) for num in nums]
        heap = Heap(nums_str, nums_len)
        heap.sort()
        t_op = heap.data
        while len(t_op)>1 and t_op[0]=='0': t_op.pop(0)
        return ''.join(t_op)