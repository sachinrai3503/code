# https://www.geeksforgeeks.org/maximized-partitions-of-a-string-such-that-each-character-of-the-string-appears-in-one-substring/
# https://leetcode.com/problems/partition-labels/

"""
Given a string S, split the given string into as many substrings as possible
 such that each character from the given string appears in a single substring 
 and print all these possible parts. The task is to print those substrings.

Examples:

Input: S = “ababcbacadefegdehijhklij” 
Output: 
ababcbaca defegde hijhklij 

Input: S = “acbbcc” 
Output: 
a cbbcc 
"""


def to_index(char):
    _ord = ord(char)
    if 65 <= _ord <= 90:
        return _ord-65
    if 97 <= _ord <= 122:
        return _ord-97
    return -1


def get_last_occ_index(string):
    occ = [-1]*26
    for i in range(len(string)):
        occ[to_index(string[i])] = i
    return occ


class Solution:
    def partitionLabels(self, S: str) -> list[int]:
        op = list()
        last_occ = get_last_occ_index(S)
        length = len(S)
        i = 0
        while i < length:
            last_index = last_occ[to_index(S[i])]
            j = 0
            while j <= last_index:
                t_index = last_occ[to_index(S[j])]
                if t_index > last_index:
                    last_index = t_index
                j += 1
            # print(S[i:j])
            op.append(j-i)
            i = j
        return op
