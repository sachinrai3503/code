# https://leetcode.com/problems/stock-price-fluctuation
"""
You are given a stream of records about a particular stock. Each record contains a
 timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. 
Even worse, some records may be incorrect. Another record with the same timestamp may appear later in 
 the stream correcting the price of the previous wrong record.

Design an algorithm that:
Updates the price of the stock at a particular timestamp, correcting the price from any previous
 records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest 
 timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.

Implement the StockPrice class:
- StockPrice() Initializes the object with no price records.
- void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
- int current() Returns the latest price of the stock.
- int maximum() Returns the maximum price of the stock.
- int minimum() Returns the minimum price of the stock.

Example 1:
Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]

Output
[null, null, null, 5, 10, null, 5, null, 2]
Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
 

Constraints:
1 <= timestamp, price <= 109
At most 105 calls will be made in total to update, current, maximum, and minimum.
current, maximum, and minimum will be called only after update has been called at least once.
"""

class HeapNode:
    def __init__(self, data, index = -1):
        self.data = data
        self.index = index
    
    def __repr__(self):
        return f'{self.data}:{self.index} '

class Heap:
    def __init__(self, size):
        self.cur_size = 0
        self.max_size = size
        self.data = [None for i in range(self.max_size)]
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = i, j
    
    def compare(self, i, j):
        pass
    
    def heapify(self, i):
        pass
    
    def insert_in_heap(self, heap_node: HeapNode):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.cur_size+=1
            self.data[index] = heap_node
            heap_node.index = index
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2

    def update(self, index):
        pass

class MinHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def heapify(self, i):
        left = i*2+1
        right = i*2 + 2
        min_index = i
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if min_index!=i:
            self.swap(min_index, i)
            self.heapify(min_index)
    
    def update(self, index):
        parent_index = (index-1)//2
        while parent_index>=0 and self.compare(index, parent_index)==-1:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index-1)//2
    
    def compare(self, i, j):
        if self.data[i].data<self.data[j].data: return -1
        if self.data[i].data>self.data[j].data: return 1
        return 0

class MaxHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def heapify(self, i):
        left = i*2+1
        right = i*2 + 2
        max_index = i
        if left<self.cur_size and self.compare(left, max_index)==-1:
            max_index = left
        if right<self.cur_size and self.compare(right, max_index)==-1:
            max_index = right
        if max_index!=i:
            self.swap(max_index, i)
            self.heapify(max_index)
    
    def update(self, index):
        parent_index = (index-1)//2
        while parent_index>=0 and self.compare(index, parent_index)==-1:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index-1)//2
    
    def compare(self, i, j):
        if self.data[i].data>self.data[j].data: return -1
        if self.data[i].data<self.data[j].data: return 1
        return 0

class StockPrice:

    def __init__(self):
        self.min_heap = MinHeap(10**5)
        self.max_heap = MaxHeap(10**5)
        self.current_price = [-1, None]
        self.timestamp_map = dict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp>=self.current_price[0]:
            self.current_price = [timestamp, price]
        if timestamp not in self.timestamp_map:
            self.timestamp_map[timestamp] = [HeapNode(price), HeapNode(price)] # [minNode, maxNode]
            self.min_heap.insert_in_heap(self.timestamp_map[timestamp][0])
            self.max_heap.insert_in_heap(self.timestamp_map[timestamp][1])
        elif price<self.timestamp_map[timestamp][0].data:
            min_node, max_node = self.timestamp_map[timestamp]
            min_node.data = price
            max_node.data = price
            self.min_heap.update(min_node.index)
            self.max_heap.heapify(max_node.index)
        elif price>self.timestamp_map[timestamp][0].data:
            min_node, max_node = self.timestamp_map[timestamp]
            min_node.data = price
            max_node.data = price
            self.min_heap.heapify(min_node.index)
            self.max_heap.update(max_node.index)
        # print(self.min_heap.data[:self.min_heap.cur_size])
        # print(self.max_heap.data[:self.max_heap.cur_size])

    def current(self) -> int:
        return self.current_price[1]
        

    def maximum(self) -> int:
        return self.max_heap.data[0].data

    def minimum(self) -> int:
        return self.min_heap.data[0].data


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()