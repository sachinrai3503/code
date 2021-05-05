# https://leetcode.com/problems/critical-connections-in-a-network/
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

class Graph:
    def __init__(self, n, edges):
        self.rec_stack = [-1 for i in range(n)]
        self.map = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])
            self.add_edge(edge[1], edge[0])
        
    def add_edge(self, a, b):
        adj_list = self.map.get(a, None)
        if adj_list is None:
            adj_list = list()
        adj_list.append(b)
        self.map[a] = adj_list
        
def find_critical_connection(graph, cur_node, parent_node, index, op_list):
    graph.rec_stack[cur_node]  = index
    min_index = index
    adj_list = graph.map.get(cur_node)
    for adj in adj_list:
        if graph.rec_stack[adj]==-1:
            t_index = find_critical_connection(graph, adj, cur_node, index+1, op_list)
            if t_index>index: op_list.append([cur_node, adj])
            if min_index>t_index: min_index = t_index
        elif adj!=parent_node and min_index>graph.rec_stack[adj]:
            min_index = graph.rec_stack[adj]
    return min_index
            
class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = Graph(n, connections)
        # print(graph.map)
        op_list = list()
        find_critical_connection(graph, 0, -1, 0, op_list)
        return op_list