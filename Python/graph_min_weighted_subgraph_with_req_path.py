# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths
"""
You are given an integer n denoting the number of nodes of a weighted directed graph. 
 The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes
 that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct
 nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest
 from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does 
 not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight
 of a subgraph is the sum of weights of its constituent edges.

Example 1:
Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], 
 src1 = 0, src2 = 1, dest = 5
Output: 9
Explanation:
The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible
 to get a subgraph with less weight satisfying all the constraints.

Example 2:
Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
Output: -1
Explanation:
The above figure represents the input graph.
It can be seen that there does not exist any path from node 1 to node 2, hence there 
 are no subgraphs satisfying all the constraints.

Constraints:
3 <= n <= 105
0 <= edges.length <= 105
edges[i].length == 3
0 <= fromi, toi, src1, src2, dest <= n - 1
fromi != toi
src1, src2, and dest are pairwise distinct.
1 <= weight[i] <= 105
"""
from typing import List
from sys import maxsize

class HeapNode:
    def __init__(self, vertex, dist, index=-1):
        self.vertex = vertex
        self.dist = dist
        self.index = index
    
    def __repr__(self):
        return f'vertex={self.vertex} dist={self.dist} index={self.index}'
        
class MinHeap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.cur_size = 0
        self.max_size = size
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index
    
    def compare(self, i, j):
        if self.data[i].dist>self.data[j].dist: return 1
        return -1
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.heapify(min_index)
    
    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
        else:
            t_index = self.cur_size
            self.data[t_index] = node
            node.index = t_index
            self.cur_size+=1
            p_index = (t_index-1)//2
            while t_index>0 and self.compare(p_index, t_index)==1:
                self.swap(p_index, t_index)
                t_index = p_index
                p_index = (t_index-1)//2
        
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
        if not node:
            print(f'Node passed as {node} is invalid.')
            return
        else:
            t_index = node.index
            p_index = (t_index-1)//2
            while t_index>0 and self.compare(p_index, t_index)==1:
                self.swap(p_index, t_index)
                t_index = p_index
                p_index = (t_index-1)//2
    
class Graph:
    
    class EdgeInfo:
        def __init__(self, v, w):
            self.v = v
            self.w = w
        
        def __repr__(self):
            return f'v={self.v} w={self.w}'
    
    def __init__(self, n, edges, reverse_edges=False):
        self.n = n
        self.data = dict()
        if not reverse_edges:
            self.add_edges(edges)
        else:
            self.add_reverse_edges(edges)
    
    def add_reverse_edges(self, edges):
        for edge in edges:
            u, v, w = edge
            self.add_edge(v,Graph.EdgeInfo(u,w))
    
    def add_edges(self, edges):
        for edge in edges:
            u, v, w = edge
            self.add_edge(u,Graph.EdgeInfo(v,w))

    def add_edge(self, u, edge_info):
        adj_vertexs = self.data.get(u, [])
        adj_vertexs.append(edge_info)
        self.data[u] = adj_vertexs

    def get_adj_vertexs(self, u):
        return self.data.get(u, None)

    def find_minpath_from_src_to_dest(self, src, dest):
        is_path_present = False
        vertex_parent_map = dict() # used to find path
        heap = MinHeap(self.n)
        visited = set()
        heap_node_map = dict()
        src_node = HeapNode(src, 0)
        heap.insert_in_heap(src_node)
        heap_node_map[src] = src_node
        vertex_parent_map[src] = [-1, 0]
        while not heap.is_empty():
            temp_node = heap.delete_top()
            u, dist = temp_node.vertex, temp_node.dist
            visited.add(u)
            if u==dest: 
                is_path_present = True
                break
            adj_vers = self.get_adj_vertexs(u)
            if not adj_vers: continue
            for adj_ver in adj_vers:
                v, w = adj_ver.v, adj_ver.w
                if v in visited: continue
                v_heap_node = heap_node_map.get(v, None)
                if v_heap_node:
                    if v_heap_node.dist>(dist+w):
                        v_heap_node.dist = dist+w
                        heap.update_node(v_heap_node)
                        vertex_parent_map[v] = [u, w]
                else:
                    v_heap_node = HeapNode(v, dist+w)
                    heap.insert_in_heap(v_heap_node)
                    heap_node_map[v] = v_heap_node
                    vertex_parent_map[v] = [u, w]
        return None if not is_path_present else vertex_parent_map
                
    def get_min_src_dest_path(self, src, dest):
        vertex_parent_map = self.find_minpath_from_src_to_dest(src, dest)
        # print("src=%s dest=%s vertex_parent_map=%s"%(src, dest, vertex_parent_map))
        if vertex_parent_map is None: return None, None
        path_edge_set = set()
        path_dist = 0
        v = dest
        while v!=src:
            u, w = vertex_parent_map.get(v)
            path_edge_set.add((u, v, w))
            path_dist+=w
            v = u
        print("src=%s dest=%s path_edge_set=%s path_dist=%s"%(src, dest, path_edge_set, path_dist))
        return path_edge_set, path_dist
    
    def get_min_dist_from(self, src):
        dist_from_src = dict()
        heap = MinHeap(self.n)
        heap_node_map = dict()
        src_node = HeapNode(src, 0)
        heap.insert_in_heap(src_node)
        heap_node_map[src] = src_node
        while not heap.is_empty():
            temp_node = heap.delete_top()
            u, dist = temp_node.vertex, temp_node.dist
            dist_from_src[u] = dist
            adj_vertexs = self.get_adj_vertexs(u)
            if not adj_vertexs: continue
            for vertex_info in adj_vertexs:
                v, w = vertex_info.v, vertex_info.w
                if v in dist_from_src: continue # using as visited
                v_heap_node = heap_node_map.get(v, None)
                if v_heap_node is not None:
                    if v_heap_node.dist>dist+w:
                        v_heap_node.dist = dist+w
                        heap.update_node(v_heap_node)
                else:
                    v_heap_node = HeapNode(v, dist+w)
                    heap.insert_in_heap(v_heap_node)
                    heap_node_map[v] = v_heap_node
        return dist_from_src
    
class Solution:
    
    def is_path_via_vertex(self, path_edge_set, vertex):
        for u, v, w in path_edge_set:
            if u==vertex or v==vertex: return True
        return False
    
    def get_unique_edges_weight(self, path_edge_set1, path_edge_set2):
        paths_edge_set = set.union(path_edge_set1, path_edge_set2)
        weight = 0
        for u,v,w in paths_edge_set:
            weight+=w
        return weight
    
    """
    This won't work because this solution doesn't takes into account multiple path with same dist from src to dest.
    So, s1->d => p1 and s2->d => p2 might not overlap even when there is an overlapping path.
    Eg - 5
         [[0,3,1],[3,4,1],[1,3,10],[1,2,1],[0,2,1],[2,4,1]]
         0
         1
         4
    """
    def minimumWeight_1(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = Graph(n, edges)
        # print(f'{graph.data=}')
        s1_dest_path_edges, s1_dest_dist = graph.get_min_src_dest_path(src1, dest)
        s2_dest_path_edges, s2_dest_dist = graph.get_min_src_dest_path(src2, dest)
        if s1_dest_path_edges is None or s2_dest_path_edges is None: return -1
        s1_dest_path_via_s2 = self.is_path_via_vertex(s1_dest_path_edges, src2)
        s2_dest_path_via_s1 = self.is_path_via_vertex(s2_dest_path_edges, src1)
        if s1_dest_path_via_s2 and s2_dest_path_via_s1: # this condition will never occur but still kept it
            print('v12')
            return min(s1_dest_dist, s2_dest_dist)
        elif s1_dest_path_via_s2:
            print('v2')
            return s1_dest_dist
        elif s2_dest_path_via_s1:
            print('v1')
            return s2_dest_dist
        else: # Now the path s1->dest & s2-> dest don't go via s2 & s1 respectively.
            sub_graph1_weight = self.get_unique_edges_weight(s1_dest_path_edges, s2_dest_path_edges)
            s1_s2_path_edges, s1_s2_dist = graph.get_min_src_dest_path(src1, src2)
            s2_s1_path_edges, s2_s1_dist = graph.get_min_src_dest_path(src2, src1)
            if s1_s2_path_edges and s2_s1_path_edges:
                print('c1')
                return min(sub_graph1_weight, min(s1_s2_dist+s2_dest_dist, s2_s1_dist+s1_dest_dist))
            elif s1_s2_path_edges:
                print('c2')
                return min(sub_graph1_weight, s1_s2_dist+s2_dest_dist)
            elif s2_s1_path_edges:
                print('c3')
                return min(sub_graph1_weight, s2_s1_dist+s1_dest_dist)
            else:
                print('c4')
                return sub_graph1_weight
    
    # https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/discuss/1844091/C%2B%2B-Dijkstra-3-times-with-illustration
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        min_weight = maxsize
        graph1 = Graph(n, edges)
        graph2 = Graph(n, edges, True)
        dist_from_s1 = graph1.get_min_dist_from(src1)
        dist_from_s2 = graph1.get_min_dist_from(src2)
        dist_from_dest = graph2.get_min_dist_from(dest)
        # print(f'{dist_from_s1=}')
        # print(f'{dist_from_s2=}')
        # print(f'{dist_from_dest=}')
        for i in range(n):
            min_weight = min(min_weight, dist_from_s1.get(i, maxsize)+dist_from_s2.get(i, maxsize)+dist_from_dest.get(i, maxsize))
        return min_weight if min_weight!=maxsize else -1