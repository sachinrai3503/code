# https://leetcode.com/problems/process-tasks-using-servers
"""
You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​
​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the
 time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are
 free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task
 being inserted at second 0). As long as there are free servers and the queue is
 not empty, the task in the front of the queue will be assigned to a free server
 with the smallest weight, and in case of a tie, it is assigned to a free server
 with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server
 becomes free and immediately assign the next task. If multiple servers become
 free at the same time, then multiple tasks from the queue will be assigned in
 order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th
 task will be assigned to.

Return the array ans​​​​.

Example 1:
Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

Example 2:
Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.

Constraints:
servers.length == n
tasks.length == m
1 <= n, m <= 2 * 105
1 <= servers[i], tasks[j] <= 2 * 105
"""

from sys import maxsize

class Heap:
    def __init__(self, size , use_weight=True):
        self.data = list()
        self.next_ele_index = 0
        self.cur_size = 0
        self.max_size = size
        self.use_weight = use_weight
    
    def print_heap(self, size=None):
        if not size: size = self.cur_size
        else: size = min(size, self.cur_size)
        print(self.data[:size])
    
    def is_full(self):
        return self.next_ele_index==self.max_size
    
    def is_empty(self):
        return self.next_ele_index==0
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    def compare(self, i, j):
         pass
        
    def heapify(self, index):
        pass
    
    def get_top(self):
        return self.data[0]
    
    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
            return
        else:
            if self.next_ele_index==self.cur_size:
                self.data.append(None)
                self.cur_size+=1
            index = self.next_ele_index
            self.next_ele_index+=1
            self.data[index] = node
            parent_index = (index-1)//2
            while index>0 and self.compare(index, parent_index)==-1:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
                parent_index=(index-1)//2

    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.next_ele_index-=1
            self.data[0] = self.data[self.next_ele_index]
            self.heapify(0)
            return temp
                
class MinHeap(Heap):
    def __init__(self, maxsize, use_weight=True):
        Heap.__init__(self, maxsize, use_weight)
    
    def compare(self, i, j):
        a, b = self.data[i], self.data[j]
        if not self.use_weight:
            if a[2]<b[2]: return -1
            if a[2]>b[2]: return 1
        if a[1]<b[1]: return -1
        if a[1]>b[1]: return 1
        if a[0]<b[0]: return -1
        if a[0]>b[0]: return 1
        return 0
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.next_ele_index and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.next_ele_index and self.compare(right, min_index)==-1:
            min_index = right
        if min_index!=index:
            self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
            self.heapify(min_index)
        
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        op = list()
        heap1 = MinHeap(n, True) # Free server
        heap2 = MinHeap(n, False) # Occupied ones
        for i in range(n):
            heap1.insert_in_heap([i, servers[i], 0])
        # heap1.print_heap()
        t = 0
        i = 0
        while i<m:
            t = max(t, i)
            if heap1.is_empty():
                t = heap2.data[0][2]
            while not heap2.is_empty() and heap2.data[0][2]<=t:
                heap1.insert_in_heap(heap2.delete_top())
            temp = heap1.delete_top()
            temp[2] = t+tasks[i]
            op.append(temp[0])
            heap2.insert_in_heap(temp)
            # print(i, t, tasks[i] ,op[-5::1])
            # heap1.print_heap(5)
            # heap2.print_heap(5)
            i+=1
        return op