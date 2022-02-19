# https://leetcode.com/problems/validate-binary-tree-nodes/
"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two
 children leftChild[i] and rightChild[i], return true if and only if all
 the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for
 the right child.
Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:
Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

Constraints:
1 <= n <= 104
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

class DJSet:
    
    def __init__(self, length):
        self.parent = [i for i in range(length)]
    
    def get_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i]=self.get_parent(self.parent[i])
        return self.parent[i]

    def union(self, parent, child):
        p1 = self.get_parent(parent)
        p2 = self.get_parent(child)
        if child!=p2: return False
        if p1==p2: return False
        self.parent[child] = p1
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        dj_set = DJSet(n)
        for i in range(n):
            if leftChild[i]!=-1: 
                if not dj_set.union(i, leftChild[i]): return False
            if rightChild[i]!=-1:
                if not dj_set.union(i, rightChild[i]): return False
        root = dj_set.get_parent(0)
        for i in range(n):
            if dj_set.get_parent(i)!=root: return False
        return True