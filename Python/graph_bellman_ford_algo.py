# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
"""
Given a graph and a source vertex src in graph, find shortest paths from src to
 all vertices in the given graph. The graph may contain negative weight edges.
"""

from sys import maxsize
        
class BellmanFord:
    
    def get_shortest_path_from_source(self, n, edges, weight, source):
        dp = [maxsize for i in range(n)]
        dp[source] = 0
        for i in range(n-1):
            for j in range(len(edges)):
                u, v = edges[j]
                w = weight[j]
                if dp[v]>(dp[u]+w):
                    dp[v]= dp[u] + w
        for j in range(len(edges)):
            u, v = edges[j]
            w = weight[j]
            if dp[v]>(dp[u] + w):
                print('Graph has -ve weight cycle')
                return None
        return dp

def main():
    # n = 5
    # edges = [[0,1],[0,2],[1,2],[1,3],[1,4],[3,2],[3,1],[4,3]]
    # weight = [-1,4,3,2,2,5,1,-3]
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    weight = [-6,2,3]
    src = 0
    bellmanFord = BellmanFord()
    print(bellmanFord.get_shortest_path_from_source(n, edges, weight, src))

if __name__ == '__main__':
    main()