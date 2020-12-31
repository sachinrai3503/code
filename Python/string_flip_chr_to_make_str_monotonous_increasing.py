# https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""
A string of '0's and '1's is monotone increasing if it consists of some number 
of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or 
a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

Example 1:
Input: "00110"
Output: 1

Example 2:
Input: "010110"
Output: 2

Example 3:
Input: "00011000"
Output: 2

Note:
1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""

# Better implementaion of same logic in C - arr_flip_chr_to_make_str_monotonous_increasing.c

def to_num(char):
    if char=='0': return 0
    if char=='1': return 1

def get_min(a, b):
    return a if a<b else b

def get_cost(target, cur):
    return (target-cur) if target>cur else (cur-target)

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        prev_0_cost, prev_1_cost = 0, 0
        for i in range(len(S)-1, -1, -1):
            cur_1_cost = get_cost(1, to_num(S[i])) + prev_1_cost
            cur_0_cost = get_cost(0, to_num(S[i])) + get_min(prev_0_cost, prev_1_cost)
            prev_0_cost, prev_1_cost = cur_0_cost, cur_1_cost
        return get_min(prev_0_cost, prev_1_cost)