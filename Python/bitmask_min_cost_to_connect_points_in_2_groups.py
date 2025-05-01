# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points
"""
You are given two groups of points where the first group has size1 points, the second group has size2 points,
 and size1 >= size2.

The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of
 connecting point i of the first group and point j of the second group. The groups are connected if each point in both
 groups is connected to one or more points in the opposite group. In other words, each point in the first group must be
 connected to at least one point in the second group, and each point in the second group must be connected to at least 
 one point in the first group.

Return the minimum cost it takes to connect the two groups.

Example 1:
Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

Example 2:
Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. 
 This does not matter as there is no limit to the number of points that can be connected. We only care about 
 the minimum total cost.

Example 3:
Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
Output: 10

Constraints:
size1 == cost.length
size2 == cost[i].length
1 <= size1, size2 <= 12
size1 >= size2
0 <= cost[i][j] <= 100
"""

from sys import maxsize
from typing import List

class Solution:

    # This is wrong
    # TC: [[93,56,92],[53,44,18],[86,44,69],[54,60,30]]
    def connectTwoGroups1(self, cost: List[List[int]]) -> int:
        n = len(cost)
        m = len(cost[0])
        visited_2_group = set()
        min_cost = 0
        for i in range(n):
            min_index = 0
            for j in range(1, m):
                if cost[i][j]<cost[i][min_index]:
                    min_index = j
            min_cost+=cost[i][min_index]
            visited_2_group.add(min_index)
        for j in range(m):
            if j in visited_2_group: continue
            t_cost = maxsize
            for i in range(n):
                t_cost = min(t_cost, cost[i][j])
            min_cost+=t_cost
        return min_cost
    
    def find_min_cost_to_connect(self, cost, i, mask):
        if (i, mask) in self.cost_map:
            return self.cost_map[(i, mask)]
        ans = 0 if i==self.row else float('inf')
        # All the points in group1 are assigned. Now do the same for unassigned points in group2
        if i==self.row:
            for j in range(self.col):
                if mask & (1<<j)==0:
                    ans+=self.g2_to_g1_cost[j]
        else:
            for j in range(self.col):
                ans = min(ans, cost[i][j] + self.find_min_cost_to_connect(cost, i+1, mask|(1<<j)))
        self.cost_map[(i, mask)] = ans
        return ans

    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        self.cost = cost
        self.row = len(cost)
        self.col = len(cost[0]) if self.row>0 else 0
        self.g2_to_g1_cost = [min({cost[i][j] for i in range(self.row)}) for j in range(self.col)]
        # print(f'{self.g2_to_g1_cost=}')
        self.cost_map = dict()
        return self.find_min_cost_to_connect(cost, 0, 0)