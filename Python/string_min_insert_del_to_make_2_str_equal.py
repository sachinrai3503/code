# https://www.geeksforgeeks.org/minimum-number-deletions-insertions-transform-one-string-another/
# https://leetcode.com/problems/delete-operation-for-two-strings/
"""
Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is
 to remove/delete and insert the minimum number of characters from/in str1 to
 transform it into str2. It could be possible that the same character needs to
 be removed/deleted from one point of str1 and inserted to some another point.

Example 1: 

Input : 
str1 = "heap", str2 = "pea" 
Output : 
Minimum Deletion = 2 and
Minimum Insertion = 1

Example 2: 
Input : 
str1 = "geeksforgeeks", str2 = "geeks"
Output : 
Minimum Deletion = 8
Minimum Insertion = 0       
"""

# Note - This can be solved using Longest common subseq concept also as shown in
#        GFG link.

from sys import maxsize


class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        l1, l2 = len(str1), len(str2)
        if l1 == 0:
            return l2
        elif l2 == 0:
            return l1
        op = [0]*l2
        for i in range(l1-1, -1, -1):
            prev = maxsize
            for j in range(l2-1, -1, -1):
                if str1[i] == str2[j]:
                    diagonal = 0
                    if i != l1-1 and j != l2-1:
                        diagonal = prev
                    elif i == l1-1 and j != l2-1:
                        diagonal = (l2-(j+1))
                    elif j == l2-1 and i != l1-1:
                        diagonal = (l1-(i+1))
                    prev = op[j]
                    op[j] = diagonal
                else:
                    right, down = 0, 0
                    if j == (l2-1):
                        right = l1 - i
                    else:
                        right = op[j+1]
                    if i == (l1-1):
                        down = l2 - j
                    else:
                        down = op[j]
                    prev = op[j]
                    op[j] = min(right, down) + 1
        return op[0]
