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
    
from sys import maxsize
    
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

    def _compare(self, num1, num2):
        n1_len = len(num1)
        n2_len = len(num2)
        i, j = 0, 0
        while i<n1_len and j<n2_len:
            if num1[i]>num2[j]: return 1
            elif num1[i]<num2[j]: return -1
            i+=1
            j+=1
        if i==n1_len and j==n2_len: return 0
        is_swapped = False
        if n1_len<n2_len:
            k = n1_len
            num1, num2 = num2, num1 # num1 is longest digit
            n1_len, n2_len = n2_len, n1_len
            is_swapped = True
        else:
            k = n2_len
        # Compare the (k+1) digit onwards
        i, j = 0, k
        total_len = n1_len + n2_len
        while j<total_len:
            if j<n1_len:
                if num1[i]<num1[j]: return 1 if not is_swapped else -1
                elif num1[i]>num1[j]: return -1 if not is_swapped else 1
            else:
                if num1[i]<num2[j-n1_len]: return 1 if not is_swapped else -1
                elif num1[i]>num2[j-n1_len]: return -1 if not is_swapped else 1
            i+=1
            j+=1
        return 0 
    
    def min_heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self._compare(self.data[left], self.data[min_index])==-1:
            min_index = left
        if right<self.cur_size and self._compare(self.data[right], self.data[min_index])==-1:
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
       
    def largestNumber(self, nums: List[int]) -> str:
        nums_len = len(nums)
        nums = [str(num) for num in nums]
        # print(nums)
        heap = Heap(nums, nums_len)
        heap.sort()
        num_op = ''.join(nums)
        num_op_len = len(num_op)
        for i in range(num_op_len):
            if num_op[i]!='0': return num_op[i:]
        return '0'