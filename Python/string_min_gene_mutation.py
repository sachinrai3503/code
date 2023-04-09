# https://leetcode.com/problems/minimum-genetic-mutation
"""
A gene string can be represented by an 8-character long string, with choices from 
 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene
 string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene
 must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return
 the minimum number of mutations needed to mutate from startGene to endGene. If 
 there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included 
 in the bank.

Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
 
Constraints:
0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        path_len = 0
        bank_set = set(bank)
        char_list = ['A', 'C', 'G', 'T']
        que = deque()
        que.append(startGene)
        que.append(None)
        while que[0]:
            while que[0]:
                temp = que.popleft()
                if temp == endGene: return path_len
                for i in range(8):
                    for char in char_list:
                        if char==temp[i]: continue
                        t_word = temp[:i] + char + temp[i+1:]
                        if t_word in bank_set:
                            que.append(t_word)
                            bank_set.remove(t_word)
            que.popleft()
            path_len+=1
            que.append(None)
        return -1