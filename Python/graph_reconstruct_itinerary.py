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

class Graph:
    def __init__(self, tickets):
        self.data = dict()
        self.add_edges(tickets)
        self.sort_values()
    
    def add_edges(self, tickets):
        for ticket in tickets:
            src, dest = ticket
            dest_list = self.data.get(src, list())
            dest_list.append(dest)
            self.data[src] = dest_list
    
    def sort_values(self):
        for src in self.data:
            self.data.get(src).sort()

class Solution:
    
    def get_itinerary(self, src, ticket_used, cur_op, op):
        if ticket_used==self.ticket_count:
            op.extend(cur_op)
            return True
        dests = self.graph.data.get(src, None)
        if dests is None: return False
        dests_len = len(dests)
        for i in range(dests_len):
            dest = dests[i]
            cur_op.append(dests.pop(i))
            # print(dests, cur_op)
            if self.get_itinerary(dest, ticket_used+1, cur_op, op): return True
            dests.insert(i, dest)
            cur_op.pop()
            # print("--",dests, cur_op)
        return False
    
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        op = list()
        self.graph = Graph(tickets)
        # print(self.graph.data)
        self.ticket_count = len(tickets)
        op.append('JFK')
        self.get_itinerary('JFK', 0, [], op)
        # print(self.graph.data)
        return op