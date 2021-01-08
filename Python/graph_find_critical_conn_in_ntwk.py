# https://leetcode.com/problems/critical-connections-in-a-network
# https://www.geeksforgeeks.org/bridge-in-a-graph/
"""
There are n servers numbered from 0 to n-1 connected by undirected
 server-to-server connections forming a network where connections[i] = [a, b]
 represents a connection between servers a and b. Any server can reach any other
 server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server
 unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:
1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""

from sys import maxsize

class Graph:
    def __init__(self, n, edges):
        self.map = dict()
        self.node_count = n
        self._add_edges(edges)
        self.visited = [False]*n
        self.stack_index = [-1]*n
        
    def _add_edges(self, edges):
        for edge in edges:
            self._add_edge(edge[0], edge[1])
            self._add_edge(edge[1], edge[0])
            
    def _add_edge(self, x, y):
        if not self.map.__contains__(x):
            self.map[x] = list()
        self.map[x].append(y)
    
    def get_adjacent(self, x):
        return self.map[x]

    def is_visited(self, x):
        return self.visited[x]
    
    def toggle_visited(self, x):
        self.visited[x] = False if self.visited[x] else True
    
    def get_index_in_stack(self, x):
        return self.stack_index[x]
    
    def set_index_in_stack(self, x, index):
        self.stack_index[x] = index
    
def find_critical_connections(graph, parent, node, cur_stack_index, critical_con):
    stack_index = graph.get_index_in_stack(node)
    if stack_index != -1:
        return stack_index
    if graph.is_visited(node): return maxsize
    graph.toggle_visited(node)
    graph.set_index_in_stack(node, cur_stack_index)
    min_stack_index = cur_stack_index
    for adj in graph.get_adjacent(node):
        if adj != parent:
            t_index = find_critical_connections(graph, node, adj, 
                                                cur_stack_index+1, critical_con)
            if t_index!=maxsize and t_index>cur_stack_index:
                critical_con.append([node, adj])
            if min_stack_index>t_index:
                min_stack_index = t_index
    graph.set_index_in_stack(node, -1)
    return min_stack_index

class Solution:
    def criticalConnections(self, n: int,
                               connections: list[list[int]]) -> list[list[int]]:
        critical_con = list()
        graph = Graph(n, connections)
        find_critical_connections(graph, -1, 0, 0, critical_con)
        return critical_con
        