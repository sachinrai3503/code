# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional
 edge of type typei between nodes ui and vi, find the maximum number of edges you
 can remove so that after removing the edges, the graph can still be fully traversed
 by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from
 any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible
 for the graph to be fully traversed by Alice and Bob.

Example 1:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully
 traversable by Alice and Bob. Removing any additional edge will not make it so. So the
 maximum number of edges we can remove is 2.

Example 2:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable
 by Alice and Bob.

Example 3:
Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes.
 Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 
Constraints:
1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.
"""


class HeapNode:
    
    # Assuming - vertex color as below number in heap
    # Blue, RedGreen, Red, Green, No = 0, 1, 2, 3, 4
    
    def __init__(self, vertex, color, index=-1):
        self.vertex = vertex
        self.color = color
        self.index = index # index in heap
    
    def get_count(self, v_color, edge_color):
        if edge_color == 3: # Blue
            self.color = 0
            if v_color == 4: return 0
            if v_color in [0, 2, 3]: return 1
            else: return 2
        if edge_color == 2: # Green
            if v_color in [2, 4]: 
                self.color = 3 if v_color is 4 else 1
                return 0
            if v_color in [0, 3]: return 1
            else: return 2
        if edge_color == 1: # Red
            if v_color in [3, 4]:
                self.color = 2 if v_color is 4 else 1
                return 0
            if v_color in [0, 2]: return 1
            else: return 2
    
    def update_color(self, edge_color):
        extra_count = self.get_count(self.color, edge_color)
        return extra_count

    def __str__(self):
        return ":".join([str(self.vertex), str(self.color), str(self.index)])
    
    def __repr__(self):
        return self.__str__()
    
class Heap:
    def __init__(self, max_size):
        self.data = [None for i in range(max_size)]
        self.cur_size = 0
        self.max_size = max_size
        
    def print_heap(self):
        print(self.data[:self.cur_size])
    
    def is_empty(self):
        return self.cur_size==0

    def is_full(self):
        return self.cur_size==self.max_size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index
        
    def min_heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.data[left].color<self.data[min_index].color:
            min_index = left
        if right<self.cur_size and self.data[right].color<self.data[min_index].color:
            min_index = right
        if min_index!=index:
            self.swap(index, min_index)
            self.min_heapify(min_index)
        
    def insert_node(self, data):
        if self.is_full():
            print('Full')
            return
        else:
            data.index = self.cur_size
            self.data[data.index] = data
            self.cur_size+=1
            index = data.index
            parent_index = (self.cur_size-2)//2
            while parent_index>0 and self.data[parent_index].color>self.data[index].color:
                self.swap(parent_index, index)
                index = parent_index
                parent_index = (index-1)//2
            if parent_index==0 and self.data[parent_index].color>self.data[index].color:
                self.swap(parent_index, index)
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
            self.min_heapify(0)
            temp.index = -1
            return temp
    
    def update_node(self, index):
        if index>=self.cur_size:
            print('Invalid node update')
            return
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].color>self.data[index].color:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = (index-1)//2
        if parent_index==0 and self.data[parent_index].color>self.data[index].color:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = (index-1)//2
            
class Graph:
    def __init__(self, n, edges):
        self.vertex_count = n
        self.edges = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        length = len(edges)
        for i in range(length):
            edge = edges[i]
            w, u, v = edge[0], edge[1]-1, edge[2]-1 # since vertex are 1 based
            self.add_edge(u, v, w, i)
            self.add_edge(v, u, w, i)
    
    def add_edge(self, u, v, w, index):
        adj_list = self.edges.get(u, list())
        adj_list.append([v, w, index]) # from [typei, ui, vi] keeping [vi, typei]
        self.edges[u] = adj_list
    
    def get_adj_edges(self, u):
        return self.edges.get(u, None)
    
class DJSet:
    def __init__(self, n, parent = None, rank = None):
        self.n = n
        self.parent = [i for i in range(n)] if parent==None else parent
        self.rank = [1 for i in range(n)] if rank==None else rank
        
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        p_u = self.find_parent(u)
        p_v = self.find_parent(v)
        if p_u==p_v: return False
        if self.rank[p_u]>self.rank[p_v]:
            self.parent[p_v] = p_u
        elif self.rank[p_u]<self.rank[p_v]:
            self.parent[p_u] = p_v
        else:
            self.parent[p_v] = p_u
            self.rank[p_u]+=1
        return True
    
    def get_cloned_djset(self):
        return DJSet(self.n, list(self.parent), list(self.rank))
    
class Solution:
    # MST using Prim won't work. See TC in Ex. 1, start from node 4 and it would fail.
    def maxNumEdgesToRemove_prim(self, n: int, edges:list[list[int]]) -> int:
        count = 0
        graph = Graph(n, edges)
        heap = Heap(n)
        heap_nodes = [None for i in range(n)]
        for i in range(n):
            color = 0 if i==0 else 4
            node = HeapNode(i, color)
            heap.insert_node(node)
            heap_nodes[i] = node
        print(graph.edges)
        heap.print_heap()
        while not heap.is_empty():
            t_node = heap.delete_top()
            heap_nodes[t_node.vertex] = None
            if t_node.color in [2,3,4]: return -1
            adj_edges = graph.get_adj_edges(t_node.vertex)
            print(t_node, adj_edges)
            if adj_edges is None: continue
            for adj_edge in adj_edges:
                v, edge_color = adj_edge[0], adj_edge[1]
                v_heap_node = heap_nodes[v]
                if v_heap_node is not None:
                    count+=v_heap_node.update_color(edge_color)
                    heap.update_node(v_heap_node.index)
            heap.print_heap()
            print('----------')
        return count
    
    def visit_all_nodes_dfs(self, graph, src, visited, ignore_edge_index, color_code):
        if src in visited: return
        visited.add(src)
        adj_edges = graph.get_adj_edges(src)
        if adj_edges is None: return
        for adj_edge in adj_edges:
            v, color, index = adj_edge
            if index==ignore_edge_index or color not in [3, color_code]: continue
            self.visit_all_nodes_dfs(graph, v, visited, ignore_edge_index, color_code)
    
    # This is using DFS
    # Will not work for - TC: [[3,1,2],[3,2,3],[3,1,3]]
    def maxNumEdgesToRemove_DFS(self, n: int, edges:list[list[int]]) -> int:
        count = 0
        graph = Graph(n, edges)
        print(graph.edges)
        edge_count = len(edges)
        for i in range(edge_count+1): # Extra 1, case graph may not be traversal even with all edge
            if i!=edge_count and edges[i][0]==3: continue
            visited_Alice, visited_bob = set(), set()
            self.visit_all_nodes_dfs(graph, 0, visited_Alice, i, 1)
            self.visit_all_nodes_dfs(graph, 0, visited_bob, i, 2)
            if len(visited_Alice)==n and len(visited_bob)==n:count+=1
            print(i, visited_Alice, visited_bob, count)
        return count-1
    
    
    def connect_graph_vertex(self, n, edges, dj_set, pre_add_edge_count):
        extra = 0
        edge_count = len(edges)
        i, j = 0, pre_add_edge_count
        max_edge_to_add = n-1
        while i<edge_count and j<max_edge_to_add:
            u, v = edges[i][1], edges[i][2]
            is_cycle = not dj_set.union(u-1, v-1)
            if is_cycle: extra+=1
            else: j+=1
            i+=1
        return j, extra + (edge_count-i)
    
    # Uses MST based on Kruskal
    def maxNumEdgesToRemove(self, n: int, edges:list[list[int]]) -> int:
        blue_edge, red_edge, green_edge = list(), list(), list()
        for edge in edges:
            if edge[0]==3: blue_edge.append(edge)
            elif edge[0]==1: red_edge.append(edge)
            else: green_edge.append(edge)
        # print(blue_edge, red_edge, green_edge)
        
        blue_dj_set = DJSet(n)
        blue_edge_added_count, blue_edge_extra = self.connect_graph_vertex(n, blue_edge, blue_dj_set, 0)
        if blue_edge_added_count==(n-1): # connected all vertices with only blue edges
            return blue_edge_extra + len(red_edge) + len(green_edge)
        
        red_dj_set = blue_dj_set.get_cloned_djset()
        red_edge_added_count, red_edge_extra = self.connect_graph_vertex(n, red_edge, red_dj_set, blue_edge_added_count)
        if red_edge_added_count<(n-1): return -1
        
        green_dj_set = blue_dj_set.get_cloned_djset()
        green_edge_added_count, green_edge_extra = self.connect_graph_vertex(n, green_edge, green_dj_set, blue_edge_added_count)
        if green_edge_added_count<(n-1): return -1
        
        # print(blue_edge_added_count, blue_edge_extra,red_edge_added_count, red_edge_extra, green_edge_added_count, green_edge_extra)
        # print(blue_dj_set.parent, red_dj_set.parent, green_dj_set.parent)
        return blue_edge_extra + red_edge_extra + green_edge_extra