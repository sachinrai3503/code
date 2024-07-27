# https://leetcode.com/problems/smallest-number-in-infinite-set
"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",
 "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""

from sys import maxsize

class Heap:
    def __init__(self, size):
        self.cur_size = 0
        self.max_size = size
        self.data = [None for i in range(size)]

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

    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.cur_size+=1
            self.data[index] = data
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(parent_index, index)==1:
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
        
    def get_top(self):
        if self.is_empty():
            print('None')
            return None
        return self.data[0]

class MinHeap(Heap):
    def compare(self, i, j):
        if self.data[i]<self.data[j]: return -1
        if self.data[i]>self.data[j]: return 1
        return 0
    
    def heapify(self, i):
        left = i*2+1
        right = i*2+2
        min_index = i
        if left<self.cur_size and self.compare(min_index, left)==1:
            min_index = left
        if right<self.cur_size and self.compare(min_index, right)==1:
            min_index = right
        if min_index!=i:
            self.swap(min_index, i)
            self.heapify(min_index)

class SmallestInfiniteSet:

    def __init__(self):
        self.addNumMinHeap = MinHeap(1001)
        self.lastPopNum = 1
        self.added = set()
        
    def popSmallest(self) -> int:
        if self.addNumMinHeap.is_empty():
            temp = self.lastPopNum
            self.lastPopNum+=1
            return temp
        else:
            temp = self.addNumMinHeap.delete_top()
            self.added.remove(temp)
            return temp

    def addBack(self, num: int) -> None:
        if num<self.lastPopNum and num not in self.added:
            self.addNumMinHeap.insert_in_heap(num)
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)