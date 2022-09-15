# https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
There are n cities connected by some number of flights. You are given an array
 flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight
 from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src
 to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked
 red in the picture.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked
 blue in the picture.
 
Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""
from sys import maxsize
from collections import deque

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
    
    def __repr__(self):
        return str(self.vertex) + ":" + str(self.weight)

class Graph:
    def __init__(self, n, edges):
        self.edges = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for edge in edges:
            u, v, w = edge
            self.add_edge(u,v,w)
    
    def add_edge(self, u, v, w):
        edges_list = self.edges.get(u, list())
        edges_list.append(Edge(v, w))
        self.edges[u] = edges_list

    def get_edges(self, u):
        return self.edges.get(u, None)

class Solution:
    
    def get_min_price_with_k_stops(self, graph, src, dest, k, cur_stop, cur_cost, in_stack):
        if src in in_stack: return maxsize
        if cur_stop>=k: return maxsize
        if src==dest: return cur_cost
        in_stack.add(src)
        adj_edge_list = graph.get_edges(src)
        if adj_edge_list is None: return maxsize
        min_price = maxsize
        for adj_edge in adj_edge_list:
            v, w = adj_edge.vertex, adj_edge.weight
            t_price = self.get_min_price_with_k_stops(graph, v, dest, k, cur_stop+1, cur_cost + w, in_stack)
            min_price = min(t_price, min_price)
        in_stack.remove(src)
        return min_price
    
    def findCheapestPrice_DFS(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # return 0
        graph = Graph(n, flights)
        # print(graph.edges)
        in_stack = set()
        min_price = self.get_min_price_with_k_stops(graph, src, dst, k+2, 0, 0, in_stack)
        return min_price if min_price!=maxsize else -1
    
    # BFS
    # Note - Here not using visited but using prices:List to avoid adding unnecessary edges to que
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        que = deque()
        graph = Graph(n, flights)
        prices = [maxsize for i in range(n)]
        que.append([src, 0]) # [u, u_price]
        que.append(None)
        k+=1
        while k>0 and que[0]!=None:
            while que[0]!=None:
                u, u_price = que.popleft()
                if u==dst: continue
                adj_vertex = graph.get_edges(u)
                if adj_vertex is None: continue
                for adj in adj_vertex:
                    v, w = adj.vertex, adj.weight
                    t_price = u_price + w
                    if t_price<prices[v]:
                        prices[v] = t_price
                        que.append([v, t_price])
            que.popleft()
            k-=1
            que.append(None)
        return prices[dst] if prices[dst]!=maxsize else -1

    # Same as above but using BellmanFord technique
    def findCheapestPrice_BellmanFord(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [maxsize for i in range(n)]
        prices[src] = 0
        t_k = -1
        i = 0
        while t_k<k and i<(n-1):
            t_prices = list(prices)
            for flight in flights:
                u, v, w = flight
                if prices[u] is not None and t_prices[v]>prices[u] + w:
                    t_prices[v] = prices[u]+w
            # print(t_prices)
            prices = t_prices
            t_k+=1
            i+=1
        return prices[dst] if prices[dst]!=maxsize else -1