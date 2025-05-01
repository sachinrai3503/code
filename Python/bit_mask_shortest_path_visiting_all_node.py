# https://leetcode.com/problems/shortest-path-visiting-all-nodes
"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an 
 array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node,
 you may revisit nodes multiple times, and you may reuse edges.

Example 1:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Constraints:
n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
"""

from typing import List
from collections import deque

class Solution:
    # Time = N*(2^N), Space = N*(2^N)
    # https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/4053514/94-74-bfs-bitmask
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited = (1<<n)-1
        que = deque()
        visited = set()
        for i in range(n):
            que.append((i, 0, 1<<i)) # (cur_node, dist, mask_visited)
            visited.add((1<<i, i))
        # print(f'{que=}')
        # print(f'{visited=}')
        # print(f'{all_visited=}')
        while que:
            u, dist, u_mask = que.popleft()
            if u_mask == all_visited:
                return dist
            for v in graph[u]:
                v_mask = u_mask | (1<<v)
                if (v_mask, v) not in visited:
                    que.append((v, dist+1, v_mask))
                    visited.add((v_mask, v))
        return None