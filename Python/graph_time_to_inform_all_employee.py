#https://leetcode.com/problems/time-needed-to-inform-all-employees
"""
A company has n employees with a unique ID for each employee from 0 to n - 1. 
 The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the
 direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the
 subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news.
 He will inform his direct subordinates, and they will inform their subordinates, and so on 
 until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates 
 (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.


Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

Constraints:
1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""

class Graph:
    def __init__(self, n, head_id, manager, inform_time):
        self.n = n
        self.head_id = head_id
        self.edges = self._set_edges(manager)
        self.inform_time = inform_time
    
    def _set_edges(self, manager):
        edges = dict()
        for i in range(self.n):
            if manager[i]!=-1:
                childs = edges.get(manager[i], list())
                childs.append(i)
                edges[manager[i]] = childs
        return edges

    def get_childs(self, i):
        return self.edges.get(i, None)
        
class Solution:
    
    def count_time(self, graph, headID):
        time = graph.inform_time[headID]
        childs = graph.get_childs(headID)
        if childs is None: return time
        child_time = 0
        for child in childs:
            child_time = max(child_time, self.count_time(graph, child))
        return time+child_time
    
    def numOfMinutes1(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = Graph(n, headID, manager, informTime)
        # print(graph.edges)
        return self.count_time(graph, headID)
    
    # Get the time by which node i will be informed and will inform its child
    def count_time_for_node(self, manager, informTime, i):
        if manager[i]==-1: return informTime[i]
        informTime[i]+=self.count_time_for_node(manager, informTime, manager[i])
        manager[i]=-1
        return informTime[i]
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        max_min = 0
        for i in range(n):
            max_min = max(max_min, self.count_time_for_node(manager, informTime, i))
        return max_min
                    