# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities
"""
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] 
 represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities.
 In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path 
 between each pair passes through only the cities from the subset. Two subtrees are different if there is a city 
 in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in
 the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum
 distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

Example 1:
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:
Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:
Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]

Constraints:
2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
"""

from collections import defaultdict
from math import log2
from typing import List

class Solution:

    def get_max_depth_node(self, graph, root, visited_mask : List[int], cur_depth):
        if not visited_mask[0]&(1<<root): return
        if cur_depth>=self.max_depth:
            self.max_depth = cur_depth
            self.max_depth_node = root
        visited_mask[0]-=(1<<root)
        for adj_ver in graph.get(root):
            self.get_max_depth_node(graph, adj_ver, visited_mask, cur_depth+1)
    
    def get_tree_diameter(self, graph, root, visited_mask: List[int]):
        if not visited_mask[0]&(1<<root): return 0
        visited_mask[0]-=(1<<root)
        depth = 0
        for adj_ver in graph.get(root):
            depth = max(depth, self.get_tree_diameter(graph, adj_ver, visited_mask))
        return depth+1

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        # print(f'{graph=}')
        op = [0 for i in range(n-1)]
        for i in range(1, 1<<n):
            last_set_bit = int(log2(i&(-i)))
            # print(f'{i=} {last_set_bit=}')
            visited_mask = [i]
            self.max_depth_node, self.max_depth = None, 0
            self.get_max_depth_node(graph, last_set_bit, visited_mask, 0)
            # print(f'{i=} {self.max_depth_node=}')
            if visited_mask[0]==0: # all nodes visited
                diameter = self.get_tree_diameter(graph, self.max_depth_node, [i]) - 1
                # print(f'{i=} {diameter=}')
                if diameter>0:
                    op[diameter-1]+=1
        return op