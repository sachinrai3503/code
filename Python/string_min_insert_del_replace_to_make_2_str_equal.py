# https://leetcode.com/problems/edit-distance/
# https://www.geeksforgeeks.org/edit-distance-dp-5/
"""
Given two strings word1 and word2, return the minimum number of operations
 required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

# Note - Here using LCA won't work for below test case - 
# word1 = "intention", word2 = "execution" :: Output: 5
# But this LCA can be used where only insert or delete is allowed.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if l1==0: return l2
        elif l2==0: return l1
        l1, l2 = len(word1), len(word2)
        op = [0]*l2
        for i in range(l1-1, -1, -1):
            prev = 0
            for j in range(l2-1, -1, -1):
                diagonal, right, down = 0, 0, 0
                if i!=l1-1 and j!=l2-1: diagonal = prev
                elif i==l1-1 and j!=l2-1: diagonal = l2 - (j+1)
                elif j==l2-1 and i!=l1-1: diagonal = l1 - (i+1)
                if j==l2-1: right = l1 - i
                else: right = op[j+1]
                if i==l1-1: down = l2 - j
                else: down = op[j]
                prev = op[j]
                if word1[i]==word2[j]:
                    op[j] = diagonal
                else: op[j] = 1 + min(diagonal, right, down)
        return op[0]