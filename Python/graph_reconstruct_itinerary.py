# https://leetcode.com/problems/reconstruct-itinerary
# https://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets
"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the
 departure and the arrival airports of one flight. Reconstruct the itinerary in order
 and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin 
 with "JFK". If there are multiple valid itineraries, you should return the itinerary that 
 has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets 
 once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 
Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""

from typing import List

class Graph:
    def __init__(self, edges):
        self.data = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for u,v in edges:
            adj_ver = self.data.get(u, list())
            adj_ver.append(v)
            self.data[u] = adj_ver
        
    def get_adj_vertexs(self, u):
        return self.data.get(u, [])

class Solution:

    def hierholzer(self, start, circuit, graph):
        path = list()
        path.append(start)
        while path:
            u = path[-1]
            if graph.get_adj_vertexs(u):
                v = graph.get_adj_vertexs(u).pop()
                path.append(v)
            else:
                circuit.append(path.pop())

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key = lambda x : x[1], reverse = True)
        graph = Graph(tickets)
        circuit = list()
        self.hierholzer('JFK', circuit, graph)
        # print(f'{circuit=}')
        return circuit[::-1]