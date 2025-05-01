# https://leetcode.com/problems/satisfiability-of-equality-equations
"""
You are given an array of strings equations that represent relationships between variables where each string 
 equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase 
 letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example 1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Constraints:
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""

from typing import List

class DJSet:
    def __init__(self, size = 26):
        self.size = size
        self.parent = [i for i in range(self.size)]
        self.rank = [1 for i in range(self.size)]
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj: return
        r_i = self.rank[pi]
        r_j = self.rank[pj]
        if r_i>r_j:
            self.parent[pj] = pi
        elif r_i<r_j:
            self.parent[pi] = pj
        else:
            self.parent[pj] = pi
            self.rank[pi]+=1
        
    def is_in_same_set(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj: return True
        return False

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dj_set = DJSet()
        for equ in equations:
            if equ[1]=='=':
                dj_set.union(ord(equ[0])-97, ord(equ[3])-97)
        for equ in equations:
            if equ[1]=='!':
                if dj_set.is_in_same_set(ord(equ[0])-97, ord(equ[3])-97): return False
        return True