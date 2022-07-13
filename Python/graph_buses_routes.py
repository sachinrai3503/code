# https://leetcode.com/problems/bus-routes/
"""
You are given an array routes representing bus routes where routes[i] is a bus
 route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the
 sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want
 to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target.
 Return -1 if it is not possible.

Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take 
 the second bus to the bus stop 6.

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 
Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""

from collections import deque

class Graph:
    def __init__(self, edges_list):
        self.edges = dict()
        for edges in edges_list:
            self.add_edges(edges)
    
    def add_edges(self, edges):
        length = len(edges)
        for i in range(length):
            for j in range(i+1, length):
                self.add_edge(edges[i], edges[j])
                self.add_edge(edges[j], edges[i])
    
    def add_edge(self, a, b):
        adj_edges_list = self.edges.get(a, list())
        adj_edges_list.append(b)
        self.edges[a] = adj_edges_list
    
    def get_edges(self, v):
        return self.edges.get(v, None)

class Graph2:
    def __init__(self, routes):
        self.stop_to_bus = dict()
        self.bus_count = len(routes)
        for i in range(self.bus_count):
            self.add_buses(i, routes[i])
    
    def add_buses(self, bus_index, stops):
        for stop in stops:
            bus_list = self.stop_to_bus.get(stop, list())
            bus_list.append(bus_index)
            self.stop_to_bus[stop] = bus_list
    
    def get_buses(self, stop):
        return self.stop_to_bus.get(stop, None)

class Solution:

    # This takes stops nodes and timesout
    def numBusesToDestination1(self, routes: list[list[int]], source: int, target: int) -> int:
        graph = Graph(routes)
        # print(graph.edges)
        bus_count = 0
        visited = set()
        que = deque()
        que.append(source)
        visited.add(source)
        que.append(None)
        while que[0]!=None:
            # print(que)
            while que[0]!=None:
                temp = que.popleft()
                if temp==target: return bus_count
                adj_stops = graph.get_edges(temp)
                for stops in adj_stops:
                    if stops not in visited:
                        que.append(stops)
                        visited.add(stops)
            que.popleft()
            bus_count+=1
            que.append(None)
        return -1

    # This takes buses as nodes
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source==target: return 0
        graph = Graph2(routes)
        # print(graph.stop_to_bus)
        bus_count = 1
        visited_buses = set()
        que = deque()
        for bus in graph.get_buses(source):
            que.append(bus)
            visited_buses.add(bus)
        que.append(None)
        while que[0]!=None:
            # print(que)
            while que[0]!=None:
                temp_bus = que.popleft()
                for stop in routes[temp_bus]:
                    if stop==target: return bus_count
                    for bus in graph.get_buses(stop):
                        if bus not in visited_buses:
                            que.append(bus)
                            visited_buses.add(bus)
            que.popleft()
            bus_count+=1
            que.append(None)
        return -1