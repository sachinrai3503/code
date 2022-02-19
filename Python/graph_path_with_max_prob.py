# https://leetcode.com/problems/path-with-maximum-probability
"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by
 an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes
 a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success
 to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it
 differs from the correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2
 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:
2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""

# Below sol use Dijkstras

from sys import maxsize

class Edge:
    def __init__(self, vertex, prob):
        self.vertex = vertex
        self.prob = prob
    
    def __repr__(self):
        return str(self.vertex) + ":" + str(self.prob)

class Graph:
    def __init__(self, n, edges, succ_prob):
        self.edges = dict()
        self.add_edges(edges, succ_prob)
    
    def add_edges(self, edges, succ_prob):
        for i in range(len(edges)):
            u, v = edges[i]
            w = succ_prob[i]
            self.add_edge(u,v,w)
            self.add_edge(v,u,w)
    
    def add_edge(self, u, v, w):
        edges_list = self.edges.get(u, list())
        edges_list.append(Edge(v, w))
        self.edges[u] = edges_list

    def get_edges(self, u):
        return self.edges.get(u, None)
        
class HeapData:
    def __init__(self, vertex, prob, index=-1):
        self.vertex = vertex
        self.prob = prob
        self.index = index
    
    def __repr__(self):
        return str(self.vertex) + ":" + str(self.prob) + ":" + str(self.index)
        
class Heap:
    def __init__(self, n):
        self.data = [None for i in range(n)]
        self.cur_size = 0
        self.max_size = n
    
    def is_full(self):
        return self.cur_size==self.max_size

    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index = i
        self.data[j].index = j
        
    def maxHeapify(self, index):
        left = index*2+1
        right = index*2+2
        max_index = index
        if left<self.cur_size and self.data[left].prob>self.data[max_index].prob:
            max_index = left
        if right<self.cur_size and self.data[right].prob>self.data[max_index].prob:
            max_index = right
        if max_index!=index:
            self.swap(max_index, index)
            self.maxHeapify(max_index)
            
    def insert(self, data):
        if self.is_full():
            print('Full')
            return
        data.index = self.cur_size
        self.data[self.cur_size] = data
        self.cur_size+=1
        index = self.cur_size-1
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].prob<self.data[index].prob:
            self.swap(parent_index, index)
            index = parent_index
            parent_index=(parent_index-1)//2
        if parent_index==0 and self.data[parent_index].prob<self.data[index].prob:
            self.swap(parent_index, index)
    
    def delete(self):
        if self.is_empty():
            print('Empty')
            return None
        temp = self.data[0]
        self.cur_size-=1
        self.swap(0, self.cur_size)
        self.maxHeapify(0)
        temp.index = -1
        return temp
    
    def update(self, index):
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].prob<self.data[index].prob:
            self.swap(parent_index, index)
            index = parent_index
            parent_index=(parent_index-1)//2
        if parent_index==0 and self.data[parent_index].prob<self.data[index].prob:
            self.swap(parent_index, index)


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        graph = Graph(n, edges, succProb)
        heap = Heap(n)
        heap_nodes = [None for i in range(n)]
        visited = [False for i in range(n)]
        for i in range(n):
            heap_node = None
            if i==start: heap_node = HeapData(i, 1)
            else: heap_node = HeapData(i, 0)
            heap.insert(heap_node)
            heap_nodes[i] = heap_node
        while not heap.is_empty():
            temp = heap.delete()
            visited[temp.vertex] = True
            if temp.vertex==end:
                return temp.prob
            adj_vertexs = graph.get_edges(temp.vertex)
            if adj_vertexs is not None:
                for adj in adj_vertexs:
                    if visited[adj.vertex] is True: continue
                    t_prob = temp.prob*adj.prob
                    t_heap_node = heap_nodes[adj.vertex]
                    if t_heap_node.prob<t_prob:
                        t_heap_node.prob = t_prob
                        heap.update(t_heap_node.index)
        return -1