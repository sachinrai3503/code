# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
"""
Given an array of events where events[i] = [startDayi, endDayi]. Every event i 
starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. 
Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:
Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Example 4:
Input: events = [[1,100000]]
Output: 1

Example 5:
Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7

Constraints:
1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
"""

class MinHeap:
    def __init__(self, maxsize):
        self.data = [None for i in range(maxsize)]
        self.maxsize = maxsize
        self.cur_size = 0
        self.start_at = -1
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def is_full(self):
        return self.cur_size==self.maxsize
    
    def is_empty(self):
        return self.cur_size==0
    
    def compare(self, i, j):
        eve_i, eve_j = self.data[i], self.data[j]
        ss_i, se_i = max(self.start_at, eve_i[0]), eve_i[1]
        es_j, ee_j = max(self.start_at, eve_j[0]), eve_j[1]
        # if ss_i>se_i: return 1 # Expired event
        if ss_i<es_j: return -1
        if ss_i>es_j: return 1
        if se_i<ee_j: return -1
        if se_i>ee_j: return 1
        return 0
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.compare(min_index, left)==1:
            min_index = left
        if right<self.cur_size and self.compare(min_index, right)==1:
            min_index = right
        if min_index!=index:
            self.swap(index, min_index)
            self.heapify(min_index)
            
    def insert(self, data):
        if self.is_full():
            print('Full')
            return
        else:
            self.data[self.cur_size] = data
            self.cur_size+=1
            parent_index = (self.cur_size-2)//2
            while parent_index>0:
                self.heapify(parent_index)
                parent_index = (parent_index-1)//2
            if parent_index==0:
                self.heapify(parent_index)
    
    def delete(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.data[0] = self.data[self.cur_size]
            self.heapify(0)
            return temp
        
class Solution:
    
    def is_expired_event(self, event, start_at):
        return max(event[0], start_at)>event[1]
    
    def maxEvents(self, events: list[list[int]]) -> int:
        count = 0
        event_to_do = list()
        length = len(events)
        events.sort(key = lambda x : x[0])
        heap = MinHeap(length)
        heap.start_at = events[0][0]
        i = 0
        while i<length or not heap.is_empty():
            while i<length and events[i][0]==heap.start_at:
                heap.insert(events[i])
                i+=1
            if heap.is_empty(): heap.start_at = events[i][0]
            else:
                while not heap.is_empty() and self.is_expired_event(heap.data[0], heap.start_at):
                    heap.delete()
                if not heap.is_empty():
                    t_event = heap.delete()
                    event_to_do.append(t_event)
                    count+=1
                    heap.start_at = max(heap.start_at, t_event[0]) + 1
        return count