# https://leetcode.com/problems/parallel-courses-ii
"""
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array
 relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course
   prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are 
   given the integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous 
semesters for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it 
 is possible to take every course.

Example 1:
Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.

Example 2:
Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph.
In the first semester, you can only take courses 2 and 3 since you cannot take more than two per semester.
In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.
 
Constraints:
1 <= n <= 15
1 <= k <= n
0 <= relations.length <= n * (n-1) / 2
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
The given graph is a directed acyclic graph.
"""

import heapq
from sys import maxsize
from typing import List
from collections import defaultdict

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.data = dict()
        # self.height = [None for i in range(n+1)]
        self.out_degree = [0 for i in range(n+1)]
        self.in_degree = [0 for i in range(n+1)]
        self.out_degree[0] = self.in_degree[0] = None
        self.add_edges(edges)
        # self.set_height()
    
    def add_edges(self, edges):
        for u, v in edges:
            adj_vertexs = self.data.get(u, [])
            adj_vertexs.append(v)
            self.data[u] = adj_vertexs
            self.out_degree[u]+=1
            self.in_degree[v]+=1
    
    def get_all_vertex_with_0_indegree(self):
        op = list()
        for i in range(self.n+1):
            if self.in_degree[i]==0:
                op.append(i)
        return op
    
    def get_adj_vertex(self, u):
        return self.data.get(u, None)

    # def _get_height(self, i):
    #     if self.height[i]!=None: return self.height[i]
    #     if self.out_degree[i]==0:
    #         return 1
    #     temp = -1
    #     for v in self.get_adj_vertex(i):
    #         temp = max(temp, self._get_height(v))
    #     return temp+1

    # def set_height(self):
    #     for i in range(1, self.n+1):
    #         self.height[i] = self._get_height(i)

class DPInfo:
    def __init__(self, semester, course_count, available_course, in_degree):
        self.semester = semester
        self.course_count = course_count
        self.available_course = available_course
        self.in_degree = in_degree
    
    def __repr__(self):
        return f'({self.semester} {self.course_count} {self.available_course} {self.in_degree})'
    
    def compare(self, dp_info):
        if self.semester<dp_info.semester: return True
        if self.course_count<dp_info.course_count: return True
        # if len(self.available_course)>len(dp_info.available_course): return True
        return False

class Solution:

    # This won't work for disjoint graphs.
    # 12
    # [[11,10],[6,3],[2,5],[9,2],[4,12],[8,7],[9,5],[6,2],[7,2],[7,4],[9,3],[11,1],[4,3]]
    # 3
    def minNumberOfSemesters_1(self, n: int, relations: List[List[int]], k: int) -> int:
        semester_count = 0
        graph = Graph(n, relations)
        print(f'{graph.data=} {graph.in_degree=} {graph.out_degree=} {graph.height=}')
        heap = graph.get_all_vertex_with_0_indegree()
        heapq.heapify(heap)
        print(f'{heap=}')
        while heap:
            semester_count+=1
            subjects_taken = 0
            next_semester = list()
            print(f'{heap=} {semester_count=}')
            while heap and subjects_taken<k:
                height, out_degree, u = heapq.heappop(heap)
                print(f'{height=} {out_degree=} {u=}')
                adj_subjects = graph.get_adj_vertex(u)
                subjects_taken+=1
                if not adj_subjects: continue
                for v in adj_subjects:
                    graph.in_degree[v]-=1
                    if graph.in_degree[v]==0:
                        heapq.heappush(next_semester, (-graph.height[v], -graph.out_degree[v], v))
            print(f'{next_semester=}')
            heap.extend(next_semester)
            heapq.heapify(heap)
            next_semester.clear()
        return semester_count
    
    # This will fail for 
    # 12
    # [[11,10],[6,3],[2,5],[9,2],[4,12],[8,7],[9,5],[6,2],[7,2],[7,4],[9,3],[11,1],[4,3]]
    # 3
    def minNumberOfSemesters_2(self, n: int, relations: List[List[int]], k: int) -> int:
        semester_count = 0
        graph = Graph(n, relations)
        print(f'{graph.data=} {graph.in_degree=} {graph.out_degree=}')
        dp_len = 1<<n
        dp = [None for i in range(dp_len)]
        available_courses = graph.get_all_vertex_with_0_indegree()
        dp[0] = DPInfo(0, 0, [[course, 1] for course in available_courses], list(graph.in_degree))
        for i in range(dp_len):
            if dp[i]==None: continue
            print(f'{i=} {dp=}')
            current_sem, cur_course_count, available_courses, cur_in_degree = dp[i].semester, dp[i].course_count, dp[i].available_course, dp[i].in_degree
            # Looping over all the courses which can be taken
            for j in range(len(available_courses)):
                course, req_sem = available_courses[j]
                # For each such course determine which sem can it be taken
                t_sem, t_course_count, t_availabe_courses, t_in_degree = None, None, None, list(cur_in_degree)
                if req_sem<=current_sem:
                    if cur_course_count==k:
                        t_sem = current_sem+1
                        t_course_count = 1
                    else:
                        t_sem = current_sem
                        t_course_count = cur_course_count + 1
                else:
                    t_sem = req_sem # check with current_sem+1
                    t_course_count = 1
                # If course 'course' is taken then what other courses are getting available
                next_available_course = list()
                next_courses = graph.get_adj_vertex(course)
                if next_courses:
                    for next_course in next_courses:
                        t_in_degree[next_course]-=1
                        if t_in_degree[next_course]==0:
                            next_available_course.append((next_course, t_sem+1))
                t_availabe_courses = available_courses[:j] + available_courses[j+1:] + next_available_course
                dp_info = DPInfo(t_sem, t_course_count, t_availabe_courses, t_in_degree)
                if dp[i|1<<(course-1)] == None or dp_info.compare(dp[i|1<<(course-1)]):
                    dp[i|1<<(course-1)] = dp_info
            print(f'{i=} {dp=}')
        return dp[-1].semester
    
    def count_set_bit(self, n):
        count = 0
        while n>0:
            count+=1
            n = n - (n&(-n))
        return count

    # For n gives the list of digits with k bit set
    def get_nums_with_k_bit_set(self, n, k):
        t_n = 1<<n
        op = [None for i in range(t_n)]
        op[0] = []
        for i in range(1, t_n):
            op[i] = list(op[i-1])
            if self.count_set_bit(i)==k:
                op[i].append(i)
        # print(f'{n=} {k=} {op=}')
        return op

    def get_k_courses_comb(self, courses, k):
        op = list()
        count = len(courses)
        if count<=k:
            op.append(courses)
        else:
            for num in self.nums_with_k_set_bit[(1<<count) - 1]:
                comb = list()
                for i in range(count):
                    if num & (1<<i): comb.append(courses[i])
                op.append(comb)
        # print(f'{courses=} {k=} {op=}')
        return op

    def get_semester_count(self, taken_courses : int) -> int:
        semester_count = maxsize
        # print(f'{taken_courses=} {self.visited=} {self.in_degree=}')
        if taken_courses == ((1<<self.n)-1): return 0 # all courses taken
        if taken_courses in self.visited: return self.visited.get(taken_courses)
        available_courses = list()
        for i in range(self.n):
            if not taken_courses & (1<<i) and self.in_degree[i]==0:
                available_courses.append(i)
        # print(f'{available_courses=}')
        for course_comb in self.get_k_courses_comb(available_courses, self.k):
            new_taken_courses = taken_courses
            for course in course_comb:
                new_taken_courses = new_taken_courses | (1<<course)
                for next_course in self.data[course]:
                    self.in_degree[next_course]-=1
            # print(f'{course_comb=} {new_taken_courses=}')
            semester_count = min(semester_count, 1 + self.get_semester_count(new_taken_courses))
            for course in course_comb:
                for next_course in self.data[course]:
                    self.in_degree[next_course]+=1
        self.visited[taken_courses] = semester_count
        return semester_count

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # no graph created && using courses with 0 index
        self.k = k
        self.n = n
        self.data = defaultdict(list)
        self.in_degree = [0 for _ in range(self.n)]
        for u, v in relations:
            self.data[u-1].append(v-1)
            self.in_degree[v-1]+=1
        self.visited = dict()
        self.nums_with_k_set_bit = self.get_nums_with_k_bit_set(n, k)
        return self.get_semester_count(0)