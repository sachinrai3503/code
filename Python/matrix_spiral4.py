# https://leetcode.com/problems/spiral-matrix-iv
"""
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in
 spiral order (clockwise), starting from the top-left of the matrix. If there are 
 remaining empty spaces, fill them with -1.

Return the generated matrix.

Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 
Constraints:
1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def fill_matrix(self, matrix, top_left, bottom_right, head):
        if head is None: return None
        si, sj = top_left
        ei, ej = bottom_right
        # Fill 1st row
        for j in range(sj, ej+1):
            if head is None: return None
            matrix[si][j] = head.val
            head = head.next
        # Fill last col
        for i in range(si+1, ei+1):
            if head is None: return None
            matrix[i][ej] =  head.val
            head = head.next
        # Fill last row
        for j in range(ej-1, sj-1, -1):
            if head is None: return None
            matrix[ei][j] =  head.val
            head = head.next
        # Fill 1st col
        for i in range(ei-1, si, -1):
            if head is None: return None
            matrix[i][sj] =  head.val
            head = head.next
        return head
    
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        matrix = [[-1 for j in range(n)] for i in range(m)]
        index = 0
        si, sj = 0, 0
        ei, ej = m-1, n-1
        while si<=ei and sj<=ej:
            head = self.fill_matrix(matrix, (si, sj), (ei, ej), head)
            if head is None: break
            si+=1
            sj+=1
            ei-=1
            ej-=1
        return matrix