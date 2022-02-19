# https://leetcode.com/problems/longest-happy-prefix/
# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix
 (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string ""
 if no such prefix exists.

Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Constraints:
1 <= s.length <= 105
s contains only lowercase English letters.
"""

# Below sol. uses roling hash. This would time out. Use LPS from KMP.

class Solution:
    
    def compare(self, s, i, j, com_len):
        k = 0
        for k in range(com_len):
            if s[i+k]!=s[j+k]: return False
        return True
    
    def longestPrefix(self, s: str) -> str:
        op_len = 0
        d = 26
        q = 10**9 + 7
        h = None # This won't be needed as no need to subtract 
        s_len = len(s)
        hash_lr = 0
        hash_rl = 0
        i, j = 0, s_len-1
        while i<s_len-1:
            hash_lr = (hash_lr*d + (ord(s[i])-97))%q
            hash_rl = (pow(d,i,q)*(ord(s[j])-97) + hash_rl)%q
            if hash_lr==hash_rl:
                if self.compare(s, 0, j, i+1):
                    op_len = i+1
            i+=1
            j-=1
        return s[0:op_len] if op_len!=0 else ""