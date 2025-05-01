# https://leetcode.com/problems/detonate-the-maximum-bombs
"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.
 This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote
 the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its
 range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate
 only one bomb.

Example 1:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example 2:
Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

Example 3:
Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.

Constraints:
1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
"""

from collections import deque
from typing import List

class DJSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj: return
        rank_i = self.rank[pi]
        rank_j = self.rank[pj]
        if rank_i < rank_j:
            self.parent[pi] = pj
            self.rank[pj]+=self.rank[pi]
        elif rank_i >= rank_j:
            self.parent[pj] = pi
            self.rank[pi]+=self.rank[pj]

class Graph:
    def __init__(self, n):
        self.n = n
        self.data = dict()
    
    def add_directed_edge(self, u, v):
        adj_ver = self.data.get(u, [])
        adj_ver.append(v)
        self.data[u] = adj_ver
    
    def get_adj_vertexs(self, u):
        return self.data.get(u, [])

class Solution:

    def get_dist(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    # This is wrong.
    # [[278,609,82],[542,865,377],[330,402,270]]
    def maximumDetonation1(self, bombs: List[List[int]]) -> int:
        max_count = 0
        bombs_count = len(bombs)
        dj_set = DJSet(bombs_count)
        for i in range(bombs_count):
            for j in range(i+1, bombs_count):
                dist_ij = self.get_dist(bombs[i], bombs[j])
                print(f'{i=} {j=} {dist_ij=}')
                if dist_ij<=bombs[i][2] or dist_ij<=bombs[j][2]:
                    dj_set.union(i, j)
        for i in range(bombs_count):
            max_count = max(max_count, dj_set.rank[i])
        return max_count
    
    def visit_from_dfs(self, graph, i, visited):
        if i in visited: return 0
        visited.add(i)
        count = 1
        adj_vertex = graph.get_adj_vertexs(i)
        for v in adj_vertex:
            count+=self.visit_from(graph, v, visited)
        return count

    def visit_from_bfs(self, graph, i):
        count = 0
        visited = set()
        que = deque()
        que.append(i)
        visited.add(i)
        while que:
            u = que.popleft()
            count+=1
            for v in graph.get_adj_vertexs(u):
                if v in visited: continue
                que.append(v)
                visited.add(v)
        return count

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        count = 0
        bombs_count = len(bombs)
        graph = Graph(bombs_count)
        for i in range(bombs_count):
            for j in range(i+1, bombs_count):
                dist_ij = self.get_dist(bombs[i], bombs[j])
                if dist_ij<=bombs[i][2]:
                    graph.add_directed_edge(i, j)
                if dist_ij<=bombs[j][2]:
                    graph.add_directed_edge(j, i)
        # print(f'{graph.data=}')
        # visited = set() # need with DFS
        for i in range(bombs_count):
            # count = max(count, self.visit_from_dfs(graph, i, visited))
            count = max(count, self.visit_from_bfs(graph, i))
            # visited.clear() # need with DFS
        return count