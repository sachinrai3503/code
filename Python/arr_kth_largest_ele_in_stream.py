# https://leetcode.com/problems/kth-largest-element-in-a-stream
"""
Design a class to find the kth largest element in a stream. Note that it is the 
 kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the 
 stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element 
 representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 
Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when
 you search for the kth element.
"""

from typing import List

class HeapNode:
    def __init__(self, num):
        self.num = num
    
    def compare(self, node2):
        if self.num<node2.num: return -1
        if self.num>node2.num: return 1
        return 0

    def __repr__(self):
        return f'{self.num=}'

class Heap:
    def __init__(self, max_size):
        self.data = [None for i in range(max_size)]
        self.cur_size = 0
        self.max_size = max_size

    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def heapify(self, index):
        pass
    
    def get_top(self):
        if self.is_empty():
            print('Empty')
            return None
        return self.data[0].num

    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.data[index] = node
            self.cur_size+=1
            parent_index = (index-1)//2
            while index>0 and node.compare(self.data[parent_index])==-1:
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
            self.swap(0, self.cur_size)
            self.heapify(0)
            return temp

class MinHeap(Heap):
    def __init__(self, max_size):
        Heap.__init__(self, max_size)
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.data[left].compare(self.data[min_index])==-1:
            min_index = left
        if right<self.cur_size and self.data[right].compare(self.data[min_index])==-1:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.heapify(min_index)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = MinHeap(k)
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.min_heap.cur_size>=self.min_heap.max_size and val>self.min_heap.get_top():
            self.min_heap.delete_top()
        self.min_heap.insert_in_heap(HeapNode(val))
        return self.min_heap.get_top()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)