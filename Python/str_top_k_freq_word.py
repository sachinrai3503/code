# https://leetcode.com/problems/top-k-frequent-words
"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words
 with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, 
 with the number of occurrence being 4, 3, 2 and 1 respectively.
 
Constraints:
1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space
"""

from typing import List

class HeapNode:
    def __init__(self, word, freq, index=-1):
        self.word = word
        self.freq = freq
        self.index = index

    def compare(self, node2):
        if self.freq<node2.freq: return -1
        if self.freq>node2.freq: return 1
        if self.word>node2.word: return -1
        if self.word<node2.word: return 1
        return 0

    def __repr__(self):
        return f'{self.word=} {self.freq=} {self.index=}'

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
        self.data[i].index = i
        self.data[j].index = j

    def heapify(self, index):
        pass
    
    def get_top(self):
        if self.is_empty():
            print('Empty')
            return None
        return self.data[0]

    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.data[index] = node
            node.index = index
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
            temp.index = -1
            return temp

    def update_node(self, node):
        if node is None:
            print('None node given')
        else:
            self.heapify(node.index)

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
    
    def sort_decending(self):
        for i in range(self.cur_size-1, 0, -1):
            self.swap(0, i)
            self.cur_size-=1
            self.heapify(0)

class Solution:
    def topKFrequent_heap(self, words: List[str], k: int) -> List[str]:
        min_heap = MinHeap(k)
        heap_node_map = dict()
        for word in words:
            word_heap_node = heap_node_map.get(word, HeapNode(word, 0))
            word_heap_node.freq+=1
            if word_heap_node.index!=-1:
                min_heap.update_node(word_heap_node)
            elif min_heap.cur_size<k:
                min_heap.insert_in_heap(word_heap_node)
            elif word_heap_node.compare(min_heap.get_top())==1:
                min_heap.delete_top()
                min_heap.insert_in_heap(word_heap_node)
            heap_node_map[word] = word_heap_node
            # print(min_heap.data)
            # print(heap_node_map)
        min_heap.sort_decending()
        return [node.word for node in min_heap.data]
    
    def _get_word_freq(self, words):
        word_freq_map = dict()
        for word in words:
            freq = word_freq_map.get(word, 0)
            freq+=1
            word_freq_map[word] = freq
        # print(f'{word_freq_map=}')
        return word_freq_map

    def _map_word_to_freq(self, max_freq, word_freq_map):
        freq_word_map = [[] for i in range(max_freq)]
        for word in word_freq_map:
            freq = word_freq_map.get(word)
            freq_word_map[freq].append(word)
        # print(f'{freq_word_map=}')
        return freq_word_map

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        op = list()
        op_len = 0
        words_len = len(words)
        word_freq_map = self._get_word_freq(words)
        freq_word_map = self._map_word_to_freq(words_len+1, word_freq_map)
        for i in range(words_len, 0, -1):
            words_len = len(freq_word_map[i])
            if words_len>0:
                freq_word_map[i].sort()
                if words_len+op_len<=k:
                    op.extend(freq_word_map[i])
                    op_len+=words_len
                else:
                    op.extend(freq_word_map[i][:k-op_len])
                    op_len+=(k-op_len)
            if op_len==k: return op
        return None