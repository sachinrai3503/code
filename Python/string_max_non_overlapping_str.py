# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
"""
Given a string s of lowercase letters, you need to find the maximum number of
 non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l],
 either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. 
If there are multiple solutions with the same number of substrings, return the
 one with minimum total length. It can be shown that there exists a unique
 solution of minimum total length.

Notice that you can return the substrings in any order.

Example 1:
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1.
 If we choose "adefadda", we are left with "ccc" which is the only one that
 doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal 
 to choose "ef" since it can be split into two. Therefore, the optimal way is to
 choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the
 same number of substrings exist.

Example 2:
Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has
 length 3, it's considered incorrect since it has larger total length.

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""

"""
Some Test cases - 
"cbbcaabbac"
"dcadaadcc"
"bbcacbaba"
"adefaddaccc"
"abbaccd"
"abcdefghijklmnopqrstuvwxyz"
"""

from sys import maxsize

def get_all_valid_range(_str, limits):
    for i in range(26):
        if limits[i] is None: continue
        limit = limits[i]
        loop  = True
        while loop:
            loop = False
            s, e = limit[0], limit[1]
            for i in range(s,e+1):
                t_index = ord(_str[i])-97
                t_limit = limits[t_index]
                if t_limit[0]>=s and t_limit[1]<=e: continue
                limit[0] = min(s, t_limit[0])
                limit[1] = max(e, t_limit[1])
                loop = True
                break
        
def get_substr(sorted_substr_limit):
    op_list = list()
    for limit in sorted_substr_limit:
        if len(op_list)==0 or op_list[-1][1]<limit[0]:
            op_list.append(limit)
        else:
            op_list.pop()
            op_list.append(limit)
    return op_list
            
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        limits = [None for i in range(26)]
        for i in range(len(s)):
            chr_index = ord(s[i])-97
            if limits[chr_index] is None: limits[chr_index] = [i,i]
            else: limits[chr_index][1] = i
        # print(limits)
        get_all_valid_range(s, limits)
        # print(limits)
        substr_limit_set = set()
        for limit in limits:
            if limit is not None:
                substr_limit_set.add((limit[0], limit[1]))
        # print(substr_limit_set)
        sorted_substr_limit = sorted(substr_limit_set)
        # print(sorted_substr_limit)
        op_substrs = get_substr(sorted_substr_limit)
        substr = list()
        for limit in op_substrs:
            substr.append(s[limit[0]:limit[1]+1])
        return substr