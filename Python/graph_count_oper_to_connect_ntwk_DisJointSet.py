# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""
There are n computers numbered from 0 to n-1 connected by ethernet cables
 connections forming a network where connections[i] = [a, b] represents a
 connection between computers a and b. Any computer can reach any other
 computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables
 between two directly connected computers, and place them between any pair of
 disconnected computers to make them directly connected. 

Return the minimum number of times you need to do this in order to make all the
 computers connected. If it's not possible, return -1. 

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between
             computers 1 and 3.

Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Example 4:
Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
 
Constraints:
1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
There are no repeated connections.
No two computers are connected by more than one cable
"""

class DisJointSet:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
    
    def find_parent(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find_parent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        p1 = self.find_parent(u)
        p2 = self.find_parent(v)
        if p1==p2:
            return 1 # Means cycle on adding edge from u to v
        r1 = self.rank[p1]
        r2 = self.rank[p2]
        if r1>r2:
            self.parent[p2] = p1
        elif r1<r2:
            self.parent[p1] = p2
        else:
            self.rank[p1]+=1
            self.parent[p2] = p1
        return 0

    def get_unique_set_count(self):
        count = 0
        for i in range(self.size):
            if self.parent[i] == i: count+=1
        return count
    
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        cycle_count = 0
        component_count = 0
        dj_set = DisJointSet(n)
        for connection in connections:
            cycle_count += dj_set.union(connection[0], connection[1])
        component_count = dj_set.get_unique_set_count()
        # print('parent =',dj_set.parent)
        # print('rank =',dj_set.rank)
        # print('çycle count =',cycle_count)
        # print('components count =',component_count)
        if cycle_count < (component_count-1): return -1
        return (component_count-1)