# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16
"""
There are n cities numbered from 0 to n-1. Given the array edges where
 edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge
 between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through
 some path and whose distance is at most distanceThreshold, If there are multiple
 such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of
 the edges' weights along that path.

Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

Constraints:
2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""

from sys import maxsize

def is_symmetric(grid, n):
    for i in range(n):
        for j in range(i, n):
            if grid[i][j]!=grid[j][i]: return False
    return True

class Graph:
    def __init__(self, n, edges):
        self.edges_mat = self.get_edges_mat(n)
        self.set_weight(edges)
    
    def get_edges_mat(self, n):
        mat = [None for i in range(n)]
        for i in range(n):
            mat[i] = [maxsize for j in range(n)]
            mat[i][i] = 0
        return mat
    
    def set_weight(self, edges):
        for edge in edges:
            u, v, w = edge
            self.edges_mat[u][v] = w
            self.edges_mat[v][u] = w

class Solution:
    
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        graph = Graph(n, edges)
        # print(graph.edges_mat)
        req_city_count = [set() for i in range(n)]
        for k in range(n):
            for i in range(n):
                dist_ik = graph.edges_mat[i][k]
                if i==k or dist_ik==maxsize: continue
                # Since our graph is undirected dist[i][j] == dist[j][i] via any node k 
                for j in range(i, n):
                    dist_kj = graph.edges_mat[k][j]
                    if i==j or dist_kj==maxsize: continue
                    if graph.edges_mat[i][j]>(dist_ik+dist_kj):
                        graph.edges_mat[i][j] = graph.edges_mat[j][i] = (dist_ik+dist_kj)
                    if graph.edges_mat[i][j]<=distanceThreshold:
                        req_city_count[i].add(j)
                        req_city_count[j].add(i) # Since undirected graph so.
        # print(graph.edges_mat)
        # print(req_city_count)
        # print(is_symmetric(graph.edges_mat, n))
        min_reachable_city_count = maxsize
        req_city = -1
        for i in range(n):
            # print(i, len(req_city_count[i]))
            if len(req_city_count[i])<=min_reachable_city_count:
                min_reachable_city_count = len(req_city_count[i])
                req_city = i
        return req_city