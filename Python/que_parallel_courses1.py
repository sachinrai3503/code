# https://www.lintcode.com/problem/3673
# https://leetcode.com/problems/parallel-courses
"""
In this problem, there are n courses. They are numbered 1 to n.

There is also a two-dimensional array relations. Inside each array contains two courses. 
 The first course is a pre-requisite for the second course. That is, you must learn the first course in the array before 
 learning the second course in the array.

You may study any number of courses in a semester, provided you have completed all prerequisites for that course in
 the previous semester.

Return minimum semester of full coursework, or -1 if full coursework cannot be completed.

Example
Example 1
Input:
4
[[1,2],[2,3],[2,4]]
Output:
3
Explanation:
Semester 1: Study 1
Semester 2: Study 2
Semester 3: Study 3, 4

Example 2
Input:
4
[[1,2],[2,3],[2,4],[3,4]]
Output:
4

Example 3
Input:
2
[[1,2],[2,1]]
Output:
-1
"""

from typing import (
    List,
)

from collections import deque

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.data = dict()
        self.in_degree = [0 for i in range(n+1)]
        self.in_degree[0] = None
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for u, v in edges:
            adj_edges = self.data.get(u, [])
            adj_edges.append(v)
            self.data[u] = adj_edges
            self.in_degree[v]+=1

    def get_all_vertex_with_0_indegree(self):
        op = list()
        for i in range(1, self.n+1):
            if self.in_degree[i]==0:
                op.append(i)
        return op
    
    def get_adj_vertexs(self, u):
        return self.data.get(u, [])

class Solution:
    """
    @param n: the number of courses
    @param relations: the relationship between all courses
    @return: ehe minimum number of semesters required to complete all courses
    """
    def minimum_semesters(self, n: int, relations: List[List[int]]) -> int:
        semester_count = 0
        graph = Graph(n, relations)
        que = deque()
        for v in graph.get_all_vertex_with_0_indegree():
            que.append(v)
        que.append(None)
        completed_courses = 0
        while que[0]:
            while que[0]:
                u = que.popleft()
                completed_courses+=1
                for v in graph.get_adj_vertexs(u):
                    graph.in_degree[v]-=1
                    if graph.in_degree[v]==0:
                        que.append(v)
            que.popleft()
            semester_count+=1
            que.append(None)
        return semester_count if completed_courses==n else -1